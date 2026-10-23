# nba_scraper

Pulls player minutes, rotation stints and shot locations for an NBA season from the NBA stats API (`stats.nba.com`, via [`nba_api`](https://github.com/swar/nba_api)). Every field the endpoints return is kept.

```bash
pip install -r requirements.txt
python scrape_season.py                 # 2026-27 regular season
python scrape_season.py --season-type Playoffs
```

## Data sources

| Endpoint | Calls | Used for |
|---|---|---|
| `leaguegamelog` (`PlayerOrTeam=T`) | 1 | list of final games (in-progress games, with no `WL`, are skipped) |
| `leaguegamelog` (`PlayerOrTeam=P`) | 1 | player box score lines, `MIN` rounded to whole minutes |
| `boxscoretraditionalv3` | 1 per game | exact `MM:SS` minutes, starters, DNP/inactive players and reasons, starter/bench team splits |
| `gamerotation` | 1 per game | every stint a player was on court (`IN_TIME_REAL` / `OUT_TIME_REAL`, tenths of a second of elapsed game time) |
| `shotchartdetail` (`PlayerID=0`, `TeamID=0`, `ContextMeasure=FGA`) | 1 | every field goal attempt league-wide, with court location; plus league averages by zone |

For every other endpoint the API offers, and the tables and columns each returns, see [docs/ENDPOINTS.md](docs/ENDPOINTS.md).

Raw per-game JSON responses are cached in `data/<season>/cache/` (git-ignored), so re-runs only fetch new games. The output CSVs are committed.

## Output (`data/<season>/`)

- `games.csv`: one row per team-game, all `leaguegamelog` columns.
- `player_game_log.csv`: one row per player-game that played, all `leaguegamelog` columns.
- `box_players.csv`: one row per rostered player-game (DNP and inactive players included), all `boxscoretraditionalv3` player fields and statistics, in snake_case. Added columns: `seconds` (parsed from `minutes`), `starter` (the box score only gives starters a `position`), `played`, `player_name`.
- `box_teams.csv`: three rows per team-game (`split` = `total` / `starters` / `bench`). The API's bench `minutes` repeats the starters' value, so for bench rows `seconds` is total minus starters. Use `seconds`, not `minutes`, for bench.
- `stints.csv`: one row per stint, with all raw `gamerotation` columns (`in_time_real`, `out_time_real`, `stint_pts` = `PLAYER_PTS`, `stint_plus_minus` = `PT_DIFF`, `stint_usg_pct` = `USG_PCT`, team city/name, first/last name) plus `stint_num`, `start_period`/`end_period` (5+ = OT), `in_clock`/`out_clock` (game clock), `in_time_s`/`out_time_s`/`duration_s` (elapsed game seconds) and `rotation_ok`.
- `shots.csv`: one row per field goal attempt, with all `shotchartdetail` columns in lowercase: `loc_x`/`loc_y` (tenths of a foot, hoop at 0,0), `shot_distance` (ft), `action_type`, `shot_type`, `shot_zone_basic`/`_area`/`_range`, `shot_made_flag`, `period`, `minutes_remaining`/`seconds_remaining`, `game_event_id`. Added columns: `clock`, `time_s` (elapsed game seconds, comparable with `stints.csv` `in_time_s`/`out_time_s`), `home_away`, `shots_complete`.
- `shot_zone_averages.csv`: league FGA, FGM and FG% for each shot zone.
- `player_minutes.csv`: one row per rostered player-game. Box score: `box_clock`, `box_seconds`, `box_min`, `starter`, `played`, `comment` (e.g. `DNP - Coach's Decision`, `Inactive - Injury/Illness`), `jersey_num`, `position`. Game log: `log_min`. Rotation: `n_stints`, `stint_seconds`, `stint_min`, `first_in_s`, `last_out_s`, summed `stint_pts`/`stint_plus_minus`, and seconds per period (`sec_q1`..`sec_q4`, `sec_ot1`, ...). Also `rotation_ok`.

Game IDs start with `00`, so read them as strings: `pd.read_csv(path, dtype={"game_id": str})`.

### `rotation_ok`

Early in a season `gamerotation` sometimes returns broken data for a game: stints that end before they start, and null points. A game gets `rotation_ok = False` when any stint has a negative duration, or when any player's stint total is more than 5 seconds off their box score minutes. For valid games the two agree to within 0.5 s. A flagged game's response is not cached, so the next run fetches it again. Filter on `rotation_ok` before using stint data.

### `shots_complete`

The shot chart can lag the box score for a game that just finished, and it sometimes drops a few attempts. A game is `shots_complete = False` when its shot count differs from the team FGA in `games.csv`. A game with no shots yet has no rows at all, and the run logs a warning for it. The shot chart is fetched in full on every run, so these gaps fill in on later runs.

## Network

The machine running the scraper needs access to `stats.nba.com`. The scraper sends a full set of browser headers (`HEADERS` in `scrape_season.py`), because the host resets the connection without them. It also often blocks or times out requests from cloud/datacenter IPs, so run it from a residential connection if requests hang.
