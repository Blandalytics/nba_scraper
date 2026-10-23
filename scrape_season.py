"""Pull player minutes and rotation stints for an NBA season from stats.nba.com.

Every field the endpoints return is kept. Outputs (under data/<season>/):
  games.csv                one row per team-game (leaguegamelog, all columns)
  player_game_log.csv      one row per player-game that played (leaguegamelog, all columns)
  box_players.csv          one row per rostered player-game, DNP/inactive included
                           (boxscoretraditionalv3, all player fields + statistics)
  box_teams.csv            one row per team-game per split: total / starters / bench
  stints.csv               one row per player stint (gamerotation, all columns + derived)
  player_minutes.csv       one row per rostered player-game: exact box score minutes,
                           starter/DNP status, stint counts and minutes per period

Raw per-game JSON responses are cached in data/<season>/cache/, so re-running only
fetches games that have not been pulled yet.

Usage:
  python scrape_season.py                      # 2026-27 regular season
  python scrape_season.py --season 2026-27 --season-type Playoffs
"""

import argparse
import json
import logging
import re
import time
from pathlib import Path

import pandas as pd
from nba_api.stats.endpoints import leaguegamelog
from nba_api.stats.library.http import NBAStatsHTTP

log = logging.getLogger("nba_scraper")

QUARTER_SECONDS = 12 * 60
OT_SECONDS = 5 * 60
REGULATION_SECONDS = 4 * QUARTER_SECONDS

# stats.nba.com resets the connection unless the request looks like it came from
# nba.com in a browser. "br" is left out of Accept-Encoding because requests can't
# decode brotli without an extra package.
HEADERS = {
    "Host": "stats.nba.com",
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"),
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Referer": "https://www.nba.com/",
    "Origin": "https://www.nba.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}


def snake(name):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def period_at(seconds):
    """Return the period number that contains elapsed game time `seconds`."""
    if seconds < REGULATION_SECONDS:
        return int(seconds // QUARTER_SECONDS) + 1
    return int((seconds - REGULATION_SECONDS) // OT_SECONDS) + 5


def period_bounds(period):
    """Return (start, end) elapsed game seconds of a period."""
    if period <= 4:
        return (period - 1) * QUARTER_SECONDS, period * QUARTER_SECONDS
    start = REGULATION_SECONDS + (period - 5) * OT_SECONDS
    return start, start + OT_SECONDS


def clock_at(seconds, period):
    """Game clock (MM:SS remaining in `period`) at elapsed game time `seconds`."""
    remaining = round(period_bounds(period)[1] - seconds)
    return f"{remaining // 60}:{remaining % 60:02d}"


def clock_to_seconds(clock):
    """'33:15' -> 1995. Blank / missing (DNP) -> 0."""
    if not isinstance(clock, str) or ":" not in clock:
        return 0
    minutes, seconds = clock.split(":")
    return int(minutes) * 60 + int(float(seconds))


def call_with_retries(fn, retries=4, pause=1.0, **kwargs):
    for attempt in range(retries + 1):
        try:
            result = fn(**kwargs)
            time.sleep(pause)
            return result
        except Exception as exc:  # stats.nba.com times out / resets / 500s often
            if attempt == retries:
                raise
            wait = 2 ** (attempt + 1)
            log.warning("%s failed (%s); retrying in %ss", getattr(fn, "__name__", fn), exc, wait)
            time.sleep(wait)


def fetch_game_log(season, season_type, player_or_team):
    resp = call_with_retries(
        leaguegamelog.LeagueGameLog,
        season=season,
        season_type_all_star=season_type,
        player_or_team_abbreviation=player_or_team,
        headers=HEADERS,
        timeout=60,
    )
    return resp.get_data_frames()[0]


def _get_json(endpoint, parameters):
    resp = NBAStatsHTTP().send_api_request(
        endpoint=endpoint, parameters=parameters, headers=HEADERS, timeout=60
    )
    return resp.get_dict()  # raises on the non-JSON bodies of 500s, triggering a retry


def fetch_cached(endpoint, parameters, cache_file, is_empty):
    """Return the raw JSON for one game, from the cache when possible."""
    if cache_file.exists():
        return json.loads(cache_file.read_text(encoding="utf-8"))
    data = call_with_retries(_get_json, endpoint=endpoint, parameters=parameters)
    if not is_empty(data):
        # Don't cache empty responses; the game may not be processed yet.
        cache_file.parent.mkdir(parents=True, exist_ok=True)
        cache_file.write_text(json.dumps(data), encoding="utf-8")
    return data


def fetch_rotation(game_id, cache_dir):
    return fetch_cached(
        "gamerotation",
        {"GameID": game_id, "LeagueID": "00"},
        cache_dir / "gamerotation" / f"{game_id}.json",
        lambda d: not any(rs["rowSet"] for rs in d.get("resultSets", [])),
    )


def fetch_boxscore(game_id, cache_dir):
    return fetch_cached(
        "boxscoretraditionalv3",
        {"GameID": game_id, "LeagueID": "00", "StartPeriod": 0, "EndPeriod": 0,
         "StartRange": 0, "EndRange": 0, "RangeType": 0},
        cache_dir / "boxscoretraditionalv3" / f"{game_id}.json",
        lambda d: not d.get("boxScoreTraditional", {}).get("homeTeam", {}).get("players"),
    )


def parse_rotation(data):
    """Raw GameRotation rows (all columns) for both teams."""
    frames = []
    for rs in data["resultSets"]:
        side = "away" if rs["name"] == "AwayTeam" else "home"
        frames.append(pd.DataFrame(rs["rowSet"], columns=rs["headers"]).assign(HOME_AWAY=side))
    return pd.concat(frames, ignore_index=True)


def parse_boxscore(data):
    """Return (players, teams) DataFrames with every field in a BoxScoreTraditionalV3 response."""
    box = data["boxScoreTraditional"]
    players, teams = [], []
    for side in ("home", "away"):
        team = box[f"{side}Team"]
        team_info = {
            "game_id": box["gameId"],
            "home_away": side,
            **{snake(k): v for k, v in team.items() if not isinstance(v, (dict, list))},
        }
        for split in ("statistics", "starters", "bench"):
            row = {**team_info, "split": "total" if split == "statistics" else split}
            row.update({snake(k): v for k, v in team.get(split, {}).items()})
            teams.append(row)
        for p in team["players"]:
            row = {**team_info}
            row.update({snake(k): v for k, v in p.items() if k != "statistics"})
            row.update({snake(k): v for k, v in p["statistics"].items()})
            players.append(row)
    players = pd.DataFrame(players)
    teams = pd.DataFrame(teams)
    for df in (players, teams):
        df["seconds"] = df["minutes"].map(clock_to_seconds)
    # The API's bench "minutes" repeats the starters' value, so derive bench seconds.
    totals = teams[teams["split"] == "total"].set_index("team_id")["seconds"]
    starters = teams[teams["split"] == "starters"].set_index("team_id")["seconds"]
    bench = teams["split"] == "bench"
    teams.loc[bench, "seconds"] = teams.loc[bench, "team_id"].map(totals - starters)
    # Starters are the only players with a position in the box score.
    players["starter"] = players["position"].fillna("").ne("")
    players["played"] = players["seconds"] > 0
    players["player_name"] = (players["first_name"].fillna("") + " " + players["family_name"].fillna("")).str.strip()
    return players, teams


def build_stints(rotation):
    """Convert raw GameRotation rows into a tidy stints table, keeping every raw column.

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
    df["in_clock"] = [clock_at(t, p) for t, p in zip(df["in_time_s"], df["start_period"])]
    df["out_clock"] = [clock_at(t, p) for t, p in zip(df["out_time_s"], df["end_period"])]
    df = df.sort_values(["GAME_ID", "TEAM_ID", "PERSON_ID", "in_time_s"])
    df["stint_num"] = df.groupby(["GAME_ID", "PERSON_ID"]).cumcount() + 1
    df["player_name"] = (df["PLAYER_FIRST"].fillna("") + " " + df["PLAYER_LAST"].fillna("")).str.strip()
    df = df.rename(
        columns={
            "GAME_ID": "game_id",
            "TEAM_ID": "team_id",
            "TEAM_CITY": "team_city",
            "TEAM_NAME": "team_name",
            "PERSON_ID": "player_id",
            "PLAYER_FIRST": "player_first",
            "PLAYER_LAST": "player_last",
            "HOME_AWAY": "home_away",
            "IN_TIME_REAL": "in_time_real",
            "OUT_TIME_REAL": "out_time_real",
            "PLAYER_PTS": "stint_pts",
            "PT_DIFF": "stint_plus_minus",
            "USG_PCT": "stint_usg_pct",
        }
    )
    first = [
        "game_id", "team_id", "team_city", "team_name", "home_away", "player_id", "player_name",
        "player_first", "player_last", "stint_num", "start_period", "end_period", "in_clock", "out_clock",
        "in_time_s", "out_time_s", "duration_s", "in_time_real", "out_time_real",
        "stint_pts", "stint_plus_minus", "stint_usg_pct",
    ]
    # Keep any column the API adds later, after the known ones.
    return df[first + [c for c in df.columns if c not in first]].reset_index(drop=True)


def stint_seconds_by_period(stints):
    """Seconds on court per player-game per period, splitting stints that span periods."""
    rows = []
    for s in stints.itertuples(index=False):
        for period in range(s.start_period, s.end_period + 1):
            lo, hi = period_bounds(period)
            seconds = min(s.out_time_s, hi) - max(s.in_time_s, lo)
            if seconds > 0:
                rows.append((s.game_id, s.player_id, period, seconds))
    long = pd.DataFrame(rows, columns=["game_id", "player_id", "period", "seconds"])
    long["col"] = long["period"].map(lambda p: f"sec_q{p}" if p <= 4 else f"sec_ot{p - 4}")
    wide = long.pivot_table(index=["game_id", "player_id"], columns="col", values="seconds",
                            aggfunc="sum", fill_value=0)
    order = sorted(wide.columns, key=lambda c: (c.startswith("sec_ot"), int(re.sub(r"\D", "", c))))
    return wide[order].round(1).reset_index()


def rotation_ok_by_game(stints, box_players, tolerance_s=5):
    """True for games whose rotation data is internally consistent and matches the box score.

    Early in a season gamerotation sometimes returns stints that end before they start
    and null points; those games get False and should be re-fetched later.
    """
    # Zero-length stints are real (subbed in and out with no clock run); negative ones aren't.
    sane = stints.groupby("game_id")["duration_s"].min() >= 0
    if box_players.empty:
        return sane
    on_court = stints.groupby(["game_id", "player_id"])["duration_s"].sum()
    box = box_players[box_players["played"]].set_index(["game_id", "person_id"])["seconds"]
    box.index.names = ["game_id", "player_id"]
    diff = (box - on_court.reindex(box.index).fillna(0)).abs()
    matches = (diff <= tolerance_s).groupby("game_id").all()
    return (sane & matches.reindex(sane.index).fillna(True)).rename("rotation_ok")


def build_player_minutes(box_players, player_log, games, stints):
    """One row per rostered player-game combining box score, game log and rotation minutes."""
    log_cols = player_log.rename(columns={"GAME_ID": "game_id", "PLAYER_ID": "player_id", "MIN": "log_min"})
    log_cols = log_cols[["game_id", "player_id", "TEAM_ID", "PLAYER_NAME", "log_min"]]
    if box_players.empty:
        base = log_cols.rename(columns={"TEAM_ID": "team_id", "PLAYER_NAME": "player_name"})
    else:
        base = box_players.rename(columns={"person_id": "player_id", "team_tricode": "team",
                                           "minutes": "box_clock", "seconds": "box_seconds"})
        base = base[["game_id", "team_id", "team", "home_away", "player_id", "player_name", "jersey_num",
                     "position", "starter", "played", "comment", "box_clock", "box_seconds"]]
        base = base.merge(log_cols, on=["game_id", "player_id"], how="outer")
        # Players in the game log but not in a box score (box not fetched yet).
        base["team_id"] = base["team_id"].fillna(base["TEAM_ID"])
        base["player_name"] = base["player_name"].fillna(base["PLAYER_NAME"])
        base["box_min"] = (base["box_seconds"] / 60).round(2)
    base = base.drop(columns=["TEAM_ID", "PLAYER_NAME"])

    game_info = games.rename(columns={"GAME_ID": "game_id", "TEAM_ID": "team_id", "GAME_DATE": "game_date",
                                      "MATCHUP": "matchup", "WL": "wl"})
    if "team" not in base:
        game_info = game_info.rename(columns={"TEAM_ABBREVIATION": "team"})
        game_info = game_info[["game_id", "team_id", "team", "game_date", "matchup", "wl"]]
    else:
        game_info = game_info[["game_id", "team_id", "game_date", "matchup", "wl"]]
    base["team_id"] = base["team_id"].astype("int64")
    base = game_info.merge(base, on=["game_id", "team_id"], how="right")

    if stints.empty:
        return base.assign(rotation_ok=pd.NA, stint_seconds=pd.NA, stint_min=pd.NA, n_stints=pd.NA)
    base = base.merge(stints.groupby("game_id")["rotation_ok"].first().reset_index(), on="game_id", how="left")
    by_player = (
        stints.groupby(["game_id", "player_id"])
        .agg(
            n_stints=("stint_num", "max"),
            stint_seconds=("duration_s", "sum"),
            first_in_s=("in_time_s", "min"),
            last_out_s=("out_time_s", "max"),
            stint_pts=("stint_pts", "sum"),
            stint_plus_minus=("stint_plus_minus", "sum"),
        )
        .reset_index()
    )
    by_player["stint_min"] = (by_player["stint_seconds"] / 60).round(2)
    out = base.merge(by_player, on=["game_id", "player_id"], how="left")
    out = out.merge(stint_seconds_by_period(stints), on=["game_id", "player_id"], how="left")
    out["n_stints"] = out["n_stints"].fillna(0).astype("int64")
    return out.sort_values(["game_date", "game_id", "home_away", "team_id", "starter", "box_seconds"],
                           ascending=[True, True, True, True, False, False], na_position="last")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--season", default="2026-27")
    parser.add_argument("--season-type", default="Regular Season",
                        choices=["Regular Season", "Pre Season", "Playoffs", "PlayIn"])
    parser.add_argument("--out-dir", default="data", type=Path)
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    out_dir = args.out_dir / args.season
    cache_dir = out_dir / "cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    suffix = "" if args.season_type == "Regular Season" else "_" + args.season_type.lower().replace(" ", "_")

    games = fetch_game_log(args.season, args.season_type, "T")
    # Games in progress show up with no W/L; skip them so partial box scores aren't cached.
    games = games[games["WL"].notna()]
    if games.empty:
        log.info("No completed %s %s games yet", args.season, args.season_type)
        return
    games.to_csv(out_dir / f"games{suffix}.csv", index=False)
    game_ids = sorted(games["GAME_ID"].unique())
    log.info("%d completed games", len(game_ids))

    player_log = fetch_game_log(args.season, args.season_type, "P")
    player_log.to_csv(out_dir / f"player_game_log{suffix}.csv", index=False)

    rotations, box_players, box_teams = [], [], []
    for i, game_id in enumerate(game_ids, 1):
        try:
            rotations.append(parse_rotation(fetch_rotation(game_id, cache_dir)))
        except Exception as exc:
            log.error("Skipping rotation for %s: %s", game_id, exc)
        try:
            data = fetch_boxscore(game_id, cache_dir)
            if data.get("boxScoreTraditional", {}).get("homeTeam", {}).get("players"):
                players, teams = parse_boxscore(data)
                box_players.append(players)
                box_teams.append(teams)
        except Exception as exc:
            log.error("Skipping box score for %s: %s", game_id, exc)
        if i % 25 == 0:
            log.info("games: %d/%d", i, len(game_ids))

    box_players = pd.concat(box_players, ignore_index=True) if box_players else pd.DataFrame()
    box_teams = pd.concat(box_teams, ignore_index=True) if box_teams else pd.DataFrame()
    box_players.to_csv(out_dir / f"box_players{suffix}.csv", index=False)
    box_teams.to_csv(out_dir / f"box_teams{suffix}.csv", index=False)

    stints = build_stints(pd.concat(rotations, ignore_index=True)) if rotations else pd.DataFrame()
    if not stints.empty:
        ok = rotation_ok_by_game(stints, box_players)
        stints = stints.merge(ok.reset_index(), on="game_id", how="left")
        for game_id in ok.index[~ok]:
            log.warning("Rotation for %s doesn't match the box score; will re-fetch next run", game_id)
            (cache_dir / "gamerotation" / f"{game_id}.json").unlink(missing_ok=True)
    stints.to_csv(out_dir / f"stints{suffix}.csv", index=False)

    minutes = build_player_minutes(box_players, player_log, games, stints)
    minutes.to_csv(out_dir / f"player_minutes{suffix}.csv", index=False)
    log.info("Wrote %d player-games and %d stints to %s", len(minutes), len(stints), out_dir)


if __name__ == "__main__":
    main()
