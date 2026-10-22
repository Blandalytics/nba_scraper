"""Pull player minutes and rotation stints for an NBA season from stats.nba.com.

Outputs (under data/<season>/):
  games.csv           one row per team-game (from leaguegamelog)
  player_minutes.csv  one row per player-game: official box score MIN plus
                      minutes/stint counts derived from the rotation data
  stints.csv          one row per player stint (continuous time on court)

Per-game rotation responses are cached in data/<season>/rotations/, so re-running
only fetches games that have not been pulled yet.

Usage:
  python scrape_season.py                      # 2026-27 regular season
  python scrape_season.py --season 2026-27 --season-type Playoffs
"""

import argparse
import logging
import time
from pathlib import Path

import pandas as pd
from nba_api.stats.endpoints import gamerotation, leaguegamelog

log = logging.getLogger("nba_scraper")

QUARTER_SECONDS = 12 * 60
OT_SECONDS = 5 * 60
REGULATION_SECONDS = 4 * QUARTER_SECONDS


def period_at(seconds):
    """Return the period number that contains elapsed game time `seconds`."""
    if seconds < REGULATION_SECONDS:
        return int(seconds // QUARTER_SECONDS) + 1
    return int((seconds - REGULATION_SECONDS) // OT_SECONDS) + 5


def call_with_retries(fn, retries=4, pause=1.0, **kwargs):
    for attempt in range(retries + 1):
        try:
            result = fn(**kwargs)
            time.sleep(pause)
            return result
        except Exception as exc:  # stats.nba.com times out / resets often
            if attempt == retries:
                raise
            wait = 2 ** (attempt + 1)
            log.warning("%s failed (%s); retrying in %ss", fn.__name__, exc, wait)
            time.sleep(wait)


def fetch_game_log(season, season_type, player_or_team):
    resp = call_with_retries(
        leaguegamelog.LeagueGameLog,
        season=season,
        season_type_all_star=season_type,
        player_or_team_abbreviation=player_or_team,
        timeout=60,
    )
    return resp.get_data_frames()[0]


def fetch_rotation(game_id, cache_dir):
    """Return the raw rotation rows (home + away) for one game, using the cache."""
    cache_file = cache_dir / f"{game_id}.csv"
    if cache_file.exists():
        return pd.read_csv(cache_file, dtype={"GAME_ID": str, "PLAYER_FIRST": str, "PLAYER_LAST": str})
    resp = call_with_retries(gamerotation.GameRotation, game_id=game_id, timeout=60)
    away, home = resp.get_data_frames()
    rotation = pd.concat([away.assign(HOME_AWAY="away"), home.assign(HOME_AWAY="home")])
    if rotation.empty:
        # Don't cache empty responses; the game may not be processed yet.
        return rotation
    rotation.to_csv(cache_file, index=False)
    return rotation


def build_stints(rotation):
    """Convert raw GameRotation rows into a tidy stints table.

    IN_TIME_REAL / OUT_TIME_REAL are tenths of a second of elapsed game time.
    """
    if rotation.empty:
        return rotation
    df = rotation.copy()
    df["in_time_s"] = df["IN_TIME_REAL"] / 10.0
    df["out_time_s"] = df["OUT_TIME_REAL"] / 10.0
    df["duration_s"] = df["out_time_s"] - df["in_time_s"]
    df["start_period"] = df["in_time_s"].map(period_at)
    # A stint that ends exactly on a period boundary belongs to the earlier period.
    df["end_period"] = (df["out_time_s"] - 0.1).clip(lower=0).map(period_at)
    df = df.sort_values(["GAME_ID", "TEAM_ID", "PERSON_ID", "in_time_s"])
    df["stint_num"] = df.groupby(["GAME_ID", "PERSON_ID"]).cumcount() + 1
    df["player_name"] = (df["PLAYER_FIRST"].fillna("") + " " + df["PLAYER_LAST"].fillna("")).str.strip()
    return df.rename(
        columns={
            "GAME_ID": "game_id",
            "TEAM_ID": "team_id",
            "PERSON_ID": "player_id",
            "HOME_AWAY": "home_away",
            "PLAYER_PTS": "stint_pts",
            "PT_DIFF": "stint_plus_minus",
            "USG_PCT": "stint_usg_pct",
        }
    )[
        [
            "game_id", "team_id", "home_away", "player_id", "player_name", "stint_num",
            "start_period", "end_period", "in_time_s", "out_time_s", "duration_s",
            "stint_pts", "stint_plus_minus", "stint_usg_pct",
        ]
    ].reset_index(drop=True)


def build_player_minutes(player_log, stints):
    box = player_log.rename(
        columns={
            "GAME_ID": "game_id",
            "GAME_DATE": "game_date",
            "PLAYER_ID": "player_id",
            "PLAYER_NAME": "player_name",
            "TEAM_ID": "team_id",
            "TEAM_ABBREVIATION": "team",
            "MATCHUP": "matchup",
            "MIN": "box_min",
        }
    )[["game_id", "game_date", "player_id", "player_name", "team_id", "team", "matchup", "box_min"]]
    if stints.empty:
        return box.assign(stint_min=pd.NA, n_stints=pd.NA)
    by_player = (
        stints.groupby(["game_id", "player_id"])
        .agg(stint_seconds=("duration_s", "sum"), n_stints=("stint_num", "max"))
        .reset_index()
    )
    by_player["stint_min"] = (by_player["stint_seconds"] / 60).round(2)
    return box.merge(
        by_player[["game_id", "player_id", "stint_min", "n_stints"]],
        on=["game_id", "player_id"],
        how="left",
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--season", default="2026-27")
    parser.add_argument("--season-type", default="Regular Season",
                        choices=["Regular Season", "Pre Season", "Playoffs", "PlayIn"])
    parser.add_argument("--out-dir", default="data", type=Path)
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    out_dir = args.out_dir / args.season
    cache_dir = out_dir / "rotations"
    cache_dir.mkdir(parents=True, exist_ok=True)
    suffix = "" if args.season_type == "Regular Season" else "_" + args.season_type.lower().replace(" ", "_")

    games = fetch_game_log(args.season, args.season_type, "T")
    if games.empty:
        log.info("No completed %s %s games yet", args.season, args.season_type)
        return
    games.to_csv(out_dir / f"games{suffix}.csv", index=False)
    game_ids = sorted(games["GAME_ID"].unique())
    log.info("%d completed games", len(game_ids))

    player_log = fetch_game_log(args.season, args.season_type, "P")

    rotations = []
    for i, game_id in enumerate(game_ids, 1):
        try:
            rotations.append(fetch_rotation(game_id, cache_dir))
        except Exception as exc:
            log.error("Skipping rotation for %s: %s", game_id, exc)
        if i % 25 == 0:
            log.info("rotations: %d/%d", i, len(game_ids))

    stints = build_stints(pd.concat(rotations, ignore_index=True)) if rotations else pd.DataFrame()
    stints.to_csv(out_dir / f"stints{suffix}.csv", index=False)

    minutes = build_player_minutes(player_log, stints)
    minutes.to_csv(out_dir / f"player_minutes{suffix}.csv", index=False)
    log.info("Wrote %d player-games and %d stints to %s", len(minutes), len(stints), out_dir)


if __name__ == "__main__":
    main()
