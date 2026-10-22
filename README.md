# nba_scraper

Pulls player minutes and rotation stints for an NBA season from the NBA stats API (`stats.nba.com`, via [`nba_api`](https://github.com/swar/nba_api)).

```bash
pip install -r requirements.txt
python scrape_season.py                 # 2026-27 regular season
python scrape_season.py --season-type Playoffs
```

## Data sources

| Endpoint | Calls | Used for |
|---|---|---|
| `leaguegamelog` (`PlayerOrTeam=T`) | 1 | list of completed games |
| `leaguegamelog` (`PlayerOrTeam=P`) | 1 | official box-score minutes per player-game |
| `gamerotation` | 1 per game | every stint a player was on court (`IN_TIME_REAL` / `OUT_TIME_REAL`, tenths of a second of elapsed game time) |

Rotation responses are cached in `data/<season>/rotations/`, so re-runs only fetch new games.

## Output (`data/<season>/`)

- `games.csv`: one row per team-game.
- `player_minutes.csv`: one row per player-game. `box_min` is the box-score minutes; `stint_min` and `n_stints` come from the rotation data.
- `stints.csv`: one row per stint. Columns: `start_period`/`end_period` (5+ = OT), `in_time_s`/`out_time_s`/`duration_s` (elapsed game seconds), `stint_pts`, `stint_plus_minus`, `stint_usg_pct`.

Game IDs start with `00`, so read them as strings: `pd.read_csv(path, dtype={"game_id": str})`.

## Network

The machine running the scraper needs access to `stats.nba.com`. That host often blocks or times out requests from cloud/datacenter IPs. Run it from a residential connection if requests hang.
