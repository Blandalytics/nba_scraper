# NBA stats API endpoints

Every `stats.nba.com/stats/<endpoint>` endpoint that `nba_api` 1.11.6 wraps: 139 endpoints returning 376 tables. Each table is one result set in the response, and its columns are what `get_data_frames()` returns. Generated from nba_api's own endpoint definitions, so columns can differ slightly from a live response.

Marked **(used)**: endpoints `scrape_season.py` calls. Marked *(new)*: not in nba_api 1.5.2, the version installed with this repo's Python 3.8; call those by name with `NBAStatsHTTP` the way the scraper calls `gamerotation`.

Removed after 1.5.2: `boxscoreplayertrackv2`, `boxscoresimilarityscore`, `playerfantasyprofile`, `scoreboard`.

## Contents

- [Box scores (one game)](#box-scores-one-game) (20)
- [Play-by-play, rotations and win probability (one game)](#play-by-play-rotations-and-win-probability-one-game) (5)
- [Shots and shot locations](#shots-and-shot-locations) (12)
- [Game logs and game finders](#game-logs-and-game-finders) (12)
- [Lineups and on/off](#lineups-and-onoff) (6)
- [Matchups and player comparisons](#matchups-and-player-comparisons) (6)
- [Player and team tracking (passing, rebounding, defense, hustle)](#player-and-team-tracking-passing-rebounding-defense-hustle) (12)
- [League-wide player and team stats](#league-wide-player-and-team-stats) (8)
- [Player splits, profiles and careers](#player-splits-profiles-and-careers) (16)
- [Team splits, rosters and history](#team-splits-rosters-and-history) (11)
- [Leaders](#leaders) (7)
- [Standings, schedules and scoreboards](#standings-schedules-and-scoreboards) (9)
- [Draft and combine](#draft-and-combine) (7)
- [Video](#video) (5)
- [Other](#other) (3)

## Box scores (one game)

### `boxscoreadvancedv2`

Parameters: `game_id`, `end_period`, `end_range`, `range_type`, `start_period`, `start_range`

| Table | Columns |
|---|---|
| `PlayerStats` | GAME_ID, TEAM_ID, TEAM_ABBREVIATION, TEAM_CITY, PLAYER_ID, PLAYER_NAME, START_POSITION, COMMENT, MIN, E_OFF_RATING, OFF_RATING, E_DEF_RATING, DEF_RATING, E_NET_RATING, NET_RATING, AST_PCT, AST_TOV, AST_RATIO, OREB_PCT, DREB_PCT, REB_PCT, TM_TOV_PCT, EFG_PCT, TS_PCT, USG_PCT, E_USG_PCT, E_PACE, PACE, PACE_PER40, POSS, PIE |
| `TeamStats` | GAME_ID, TEAM_ID, TEAM_NAME, TEAM_ABBREVIATION, TEAM_CITY, MIN, E_OFF_RATING, OFF_RATING, E_DEF_RATING, DEF_RATING, E_NET_RATING, NET_RATING, AST_PCT, AST_TOV, AST_RATIO, OREB_PCT, DREB_PCT, REB_PCT, E_TM_TOV_PCT, TM_TOV_PCT, EFG_PCT, TS_PCT, USG_PCT, E_USG_PCT, E_PACE, PACE, PACE_PER40, POSS, PIE |

### `boxscoreadvancedv3`

Parameters: `game_id`, `end_period`, `end_range`, `range_type`, `start_period`, `start_range`

| Table | Columns |
|---|---|
| `PlayerStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, personId, firstName, familyName, nameI, playerSlug, position, comment, jerseyNum, minutes, estimatedOffensiveRating, offensiveRating, estimatedDefensiveRating, defensiveRating, estimatedNetRating, netRating, assistPercentage, assistToTurnover, assistRatio, offensiveReboundPercentage, defensiveReboundPercentage, reboundPercentage, turnoverRatio, effectiveFieldGoalPercentage, trueShootingPercentage, usagePercentage, estimatedUsagePercentage, estimatedPace, pace, pacePer40, possessions, PIE |
| `TeamStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, minutes, estimatedOffensiveRating, offensiveRating, estimatedDefensiveRating, defensiveRating, estimatedNetRating, netRating, assistPercentage, assistToTurnover, assistRatio, offensiveReboundPercentage, defensiveReboundPercentage, reboundPercentage, estimatedTeamTurnoverPercentage, turnoverRatio, effectiveFieldGoalPercentage, trueShootingPercentage, usagePercentage, estimatedUsagePercentage, estimatedPace, pace, pacePer40, possessions, PIE |

### `boxscoredefensivev2`

Parameters: `game_id`

| Table | Columns |
|---|---|
| `PlayerStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, personId, firstName, familyName, nameI, playerSlug, position, comment, jerseyNum, matchupMinutes, partialPossessions, switchesOn, playerPoints, defensiveRebounds, matchupAssists, matchupTurnovers, steals, blocks, matchupFieldGoalsMade, matchupFieldGoalsAttempted, matchupFieldGoalPercentage, matchupThreePointersMade, matchupThreePointersAttempted, matchupThreePointerPercentage |
| `TeamStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, minutes |

### `boxscorefourfactorsv2`

Parameters: `game_id`, `end_period`, `end_range`, `range_type`, `start_period`, `start_range`

| Table | Columns |
|---|---|
| `sqlPlayersFourFactors` | GAME_ID, TEAM_ID, TEAM_ABBREVIATION, TEAM_CITY, PLAYER_ID, PLAYER_NAME, START_POSITION, COMMENT, MIN, EFG_PCT, FTA_RATE, TM_TOV_PCT, OREB_PCT, OPP_EFG_PCT, OPP_FTA_RATE, OPP_TOV_PCT, OPP_OREB_PCT |
| `sqlTeamsFourFactors` | GAME_ID, TEAM_ID, TEAM_NAME, TEAM_ABBREVIATION, TEAM_CITY, MIN, EFG_PCT, FTA_RATE, TM_TOV_PCT, OREB_PCT, OPP_EFG_PCT, OPP_FTA_RATE, OPP_TOV_PCT, OPP_OREB_PCT |

### `boxscorefourfactorsv3`

Parameters: `game_id`, `end_period`, `end_range`, `range_type`, `start_period`, `start_range`

| Table | Columns |
|---|---|
| `PlayerStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, personId, firstName, familyName, nameI, playerSlug, position, comment, jerseyNum, minutes, effectiveFieldGoalPercentage, freeThrowAttemptRate, teamTurnoverPercentage, offensiveReboundPercentage, oppEffectiveFieldGoalPercentage, oppFreeThrowAttemptRate, oppTeamTurnoverPercentage, oppOffensiveReboundPercentage |
| `TeamStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, minutes, effectiveFieldGoalPercentage, freeThrowAttemptRate, teamTurnoverPercentage, offensiveReboundPercentage, oppEffectiveFieldGoalPercentage, oppFreeThrowAttemptRate, oppTeamTurnoverPercentage, oppOffensiveReboundPercentage |

### `boxscorehustlev2`

Parameters: `game_id`

| Table | Columns |
|---|---|
| `PlayerStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, personId, firstName, familyName, nameI, playerSlug, position, comment, jerseyNum, minutes, points, contestedShots, contestedShots2pt, contestedShots3pt, deflections, chargesDrawn, screenAssists, screenAssistPoints, looseBallsRecoveredOffensive, looseBallsRecoveredDefensive, looseBallsRecoveredTotal, offensiveBoxOuts, defensiveBoxOuts, boxOutPlayerTeamRebounds, boxOutPlayerRebounds, boxOuts |
| `TeamStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, minutes, points, contestedShots, contestedShots2pt, contestedShots3pt, deflections, chargesDrawn, screenAssists, screenAssistPoints, looseBallsRecoveredOffensive, looseBallsRecoveredDefensive, looseBallsRecoveredTotal, offensiveBoxOuts, defensiveBoxOuts, boxOutPlayerTeamRebounds, boxOutPlayerRebounds, boxOuts |

### `boxscorematchupsv3`

Parameters: `game_id`

| Table | Columns |
|---|---|
| `PlayerStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, personIdOff, firstNameOff, familyNameOff, nameIOff, playerSlugOff, jerseyNumOff, personIdDef, firstNameDef, familyNameDef, nameIDef, playerSlugDef, positionDef, commentDef, jerseyNumDef, matchupMinutes, matchupMinutesSort, partialPossessions, percentageDefenderTotalTime, percentageOffensiveTotalTime, percentageTotalTimeBothOn, switchesOn, playerPoints, teamPoints, matchupAssists, matchupPotentialAssists, matchupTurnovers, matchupBlocks, matchupFieldGoalsMade, matchupFieldGoalsAttempted, matchupFieldGoalsPercentage, matchupThreePointersMade, matchupThreePointersAttempted, matchupThreePointersPercentage, helpBlocks, helpFieldGoalsMade, helpFieldGoalsAttempted, helpFieldGoalsPercentage, matchupFreeThrowsMade, matchupFreeThrowsAttempted, shootingFouls |

### `boxscoremiscv2`

Parameters: `game_id`, `end_period`, `end_range`, `range_type`, `start_period`, `start_range`

| Table | Columns |
|---|---|
| `sqlPlayersMisc` | GAME_ID, TEAM_ID, TEAM_ABBREVIATION, TEAM_CITY, PLAYER_ID, PLAYER_NAME, START_POSITION, COMMENT, MIN, PTS_OFF_TOV, PTS_2ND_CHANCE, PTS_FB, PTS_PAINT, OPP_PTS_OFF_TOV, OPP_PTS_2ND_CHANCE, OPP_PTS_FB, OPP_PTS_PAINT, BLK, BLKA, PF, PFD |
| `sqlTeamsMisc` | GAME_ID, TEAM_ID, TEAM_NAME, TEAM_ABBREVIATION, TEAM_CITY, MIN, PTS_OFF_TOV, PTS_2ND_CHANCE, PTS_FB, PTS_PAINT, OPP_PTS_OFF_TOV, OPP_PTS_2ND_CHANCE, OPP_PTS_FB, OPP_PTS_PAINT, BLK, BLKA, PF, PFD |

### `boxscoremiscv3`

Parameters: `game_id`, `end_period`, `end_range`, `range_type`, `start_period`, `start_range`

| Table | Columns |
|---|---|
| `PlayerStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, personId, firstName, familyName, nameI, playerSlug, position, comment, jerseyNum, minutes, pointsOffTurnovers, pointsSecondChance, pointsFastBreak, pointsPaint, oppPointsOffTurnovers, oppPointsSecondChance, oppPointsFastBreak, oppPointsPaint, blocks, blocksAgainst, foulsPersonal, foulsDrawn |
| `TeamStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, minutes, pointsOffTurnovers, pointsSecondChance, pointsFastBreak, pointsPaint, oppPointsOffTurnovers, oppPointsSecondChance, oppPointsFastBreak, oppPointsPaint, blocks, blocksAgainst, foulsPersonal, foulsDrawn |

### `boxscoreplayertrackv3`

Parameters: `game_id`

| Table | Columns |
|---|---|
| `PlayerStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, personId, firstName, familyName, nameI, playerSlug, position, comment, jerseyNum, minutes, speed, distance, reboundChancesOffensive, reboundChancesDefensive, reboundChancesTotal, touches, secondaryAssists, freeThrowAssists, passes, assists, contestedFieldGoalsMade, contestedFieldGoalsAttempted, contestedFieldGoalPercentage, uncontestedFieldGoalsMade, uncontestedFieldGoalsAttempted, uncontestedFieldGoalsPercentage, fieldGoalPercentage, defendedAtRimFieldGoalsMade, defendedAtRimFieldGoalsAttempted, defendedAtRimFieldGoalPercentage |
| `TeamStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, minutes, distance, reboundChancesOffensive, reboundChancesDefensive, reboundChancesTotal, touches, secondaryAssists, freeThrowAssists, passes, assists, contestedFieldGoalsMade, contestedFieldGoalsAttempted, contestedFieldGoalPercentage, uncontestedFieldGoalsMade, uncontestedFieldGoalsAttempted, uncontestedFieldGoalsPercentage, fieldGoalPercentage, defendedAtRimFieldGoalsMade, defendedAtRimFieldGoalsAttempted, defendedAtRimFieldGoalPercentage |

### `boxscorescoringv2`

Parameters: `game_id`, `end_period`, `end_range`, `range_type`, `start_period`, `start_range`

| Table | Columns |
|---|---|
| `sqlPlayersScoring` | GAME_ID, TEAM_ID, TEAM_ABBREVIATION, TEAM_CITY, PLAYER_ID, PLAYER_NAME, START_POSITION, COMMENT, MIN, PCT_FGA_2PT, PCT_FGA_3PT, PCT_PTS_2PT, PCT_PTS_2PT_MR, PCT_PTS_3PT, PCT_PTS_FB, PCT_PTS_FT, PCT_PTS_OFF_TOV, PCT_PTS_PAINT, PCT_AST_2PM, PCT_UAST_2PM, PCT_AST_3PM, PCT_UAST_3PM, PCT_AST_FGM, PCT_UAST_FGM |
| `sqlTeamsScoring` | GAME_ID, TEAM_ID, TEAM_NAME, TEAM_ABBREVIATION, TEAM_CITY, MIN, PCT_FGA_2PT, PCT_FGA_3PT, PCT_PTS_2PT, PCT_PTS_2PT_MR, PCT_PTS_3PT, PCT_PTS_FB, PCT_PTS_FT, PCT_PTS_OFF_TOV, PCT_PTS_PAINT, PCT_AST_2PM, PCT_UAST_2PM, PCT_AST_3PM, PCT_UAST_3PM, PCT_AST_FGM, PCT_UAST_FGM |

### `boxscorescoringv3`

Parameters: `game_id`, `end_period`, `end_range`, `range_type`, `start_period`, `start_range`

| Table | Columns |
|---|---|
| `PlayerStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, personId, firstName, familyName, nameI, playerSlug, position, comment, jerseyNum, minutes, percentageFieldGoalsAttempted2pt, percentageFieldGoalsAttempted3pt, percentagePoints2pt, percentagePointsMidrange2pt, percentagePoints3pt, percentagePointsFastBreak, percentagePointsFreeThrow, percentagePointsOffTurnovers, percentagePointsPaint, percentageAssisted2pt, percentageUnassisted2pt, percentageAssisted3pt, percentageUnassisted3pt, percentageAssistedFGM, percentageUnassistedFGM |
| `TeamStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, minutes, percentageFieldGoalsAttempted2pt, percentageFieldGoalsAttempted3pt, percentagePoints2pt, percentagePointsMidrange2pt, percentagePoints3pt, percentagePointsFastBreak, percentagePointsFreeThrow, percentagePointsOffTurnovers, percentagePointsPaint, percentageAssisted2pt, percentageUnassisted2pt, percentageAssisted3pt, percentageUnassisted3pt, percentageAssistedFGM, percentageUnassistedFGM |

### `boxscoresummaryv2`

Parameters: `game_id`

| Table | Columns |
|---|---|
| `AvailableVideo` | GAME_ID, VIDEO_AVAILABLE_FLAG, PT_AVAILABLE, PT_XYZ_AVAILABLE, WH_STATUS, HUSTLE_STATUS, HISTORICAL_STATUS |
| `GameInfo` | GAME_DATE, ATTENDANCE, GAME_TIME |
| `GameSummary` | GAME_DATE_EST, GAME_SEQUENCE, GAME_ID, GAME_STATUS_ID, GAME_STATUS_TEXT, GAMECODE, HOME_TEAM_ID, VISITOR_TEAM_ID, SEASON, LIVE_PERIOD, LIVE_PC_TIME, NATL_TV_BROADCASTER_ABBREVIATION, LIVE_PERIOD_TIME_BCAST, WH_STATUS |
| `InactivePlayers` | PLAYER_ID, FIRST_NAME, LAST_NAME, JERSEY_NUM, TEAM_ID, TEAM_CITY, TEAM_NAME, TEAM_ABBREVIATION |
| `LastMeeting` | GAME_ID, LAST_GAME_ID, LAST_GAME_DATE_EST, LAST_GAME_HOME_TEAM_ID, LAST_GAME_HOME_TEAM_CITY, LAST_GAME_HOME_TEAM_NAME, LAST_GAME_HOME_TEAM_ABBREVIATION, LAST_GAME_HOME_TEAM_POINTS, LAST_GAME_VISITOR_TEAM_ID, LAST_GAME_VISITOR_TEAM_CITY, LAST_GAME_VISITOR_TEAM_NAME, LAST_GAME_VISITOR_TEAM_CITY1, LAST_GAME_VISITOR_TEAM_POINTS |
| `LineScore` | GAME_DATE_EST, GAME_SEQUENCE, GAME_ID, TEAM_ID, TEAM_ABBREVIATION, TEAM_CITY_NAME, TEAM_NICKNAME, TEAM_WINS_LOSSES, PTS_QTR1, PTS_QTR2, PTS_QTR3, PTS_QTR4, PTS_OT1, PTS_OT2, PTS_OT3, PTS_OT4, PTS_OT5, PTS_OT6, PTS_OT7, PTS_OT8, PTS_OT9, PTS_OT10, PTS |
| `Officials` | OFFICIAL_ID, FIRST_NAME, LAST_NAME, JERSEY_NUM |
| `OtherStats` | LEAGUE_ID, TEAM_ID, TEAM_ABBREVIATION, TEAM_CITY, PTS_PAINT, PTS_2ND_CHANCE, PTS_FB, LARGEST_LEAD, LEAD_CHANGES, TIMES_TIED, TEAM_TURNOVERS, TOTAL_TURNOVERS, TEAM_REBOUNDS, PTS_OFF_TO |
| `SeasonSeries` | GAME_ID, HOME_TEAM_ID, VISITOR_TEAM_ID, GAME_DATE_EST, HOME_TEAM_WINS, HOME_TEAM_LOSSES, SERIES_LEADER |

### `boxscoresummaryv3` *(new)*

Parameters: `game_id`

| Table | Columns |
|---|---|
| `GameSummary` | gameId, gameCode, gameStatus, gameStatusText, period, gameClock, gameTimeUTC, gameEt, awayTeamId, homeTeamId, duration, attendance, sellout |
| `GameInfo` | gameId, gameDate, attendance, gameDuration |
| `ArenaInfo` | gameId, arenaId, arenaName, arenaCity, arenaState, arenaCountry, arenaTimezone |
| `Officials` | gameId, personId, name, nameI, firstName, familyName, jerseyNum |
| `LineScore` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, teamWins, teamLosses, period1Score, period2Score, period3Score, period4Score, score |
| `InactivePlayers` | gameId, teamId, personId, firstName, familyName, jerseyNum |
| `LastFiveMeetings` | recencyOrder, gameId, gameTimeUTC, gameEt, gameStatus, gameStatusText, awayTeamId, awayTeamCity, awayTeamName, awayTeamTricode, awayTeamScore, awayTeamWins, awayTeamLosses, homeTeamId, homeTeamCity, homeTeamName, homeTeamTricode, homeTeamScore, homeTeamWins, homeTeamLosses |
| `OtherStats` | gameId, teamId, teamCity, teamName, teamTricode, points, reboundsTotal, assists, steals, blocks, turnovers, fieldGoalsPercentage, threePointersPercentage, freeThrowsPercentage, pointsInThePaint, pointsSecondChance, pointsFastBreak, biggestLead, leadChanges, timesTied, biggestScoringRun, turnoversTeam, turnoversTotal, reboundsTeam, pointsFromTurnovers, benchPoints |
| `AvailableVideo` | gameId, videoAvailableFlag, ptAvailable, ptXYZAvailable, whStatus, hustleStatus, historicalStatus |

### `boxscoretraditionalv2`

Parameters: `game_id`, `end_period`, `end_range`, `range_type`, `start_period`, `start_range`

| Table | Columns |
|---|---|
| `PlayerStats` | GAME_ID, TEAM_ID, TEAM_ABBREVIATION, TEAM_CITY, PLAYER_ID, PLAYER_NAME, START_POSITION, COMMENT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TO, PF, PTS, PLUS_MINUS |
| `TeamStarterBenchStats` | GAME_ID, TEAM_ID, TEAM_NAME, TEAM_ABBREVIATION, TEAM_CITY, STARTERS_BENCH, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TO, PF, PTS |
| `TeamStats` | GAME_ID, TEAM_ID, TEAM_NAME, TEAM_ABBREVIATION, TEAM_CITY, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TO, PF, PTS, PLUS_MINUS |

### `boxscoretraditionalv3` **(used)**

Feeds `box_players.csv, box_teams.csv`.

Parameters: `game_id`, `end_period`, `end_range`, `range_type`, `start_period`, `start_range`

| Table | Columns |
|---|---|
| `PlayerStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, personId, firstName, familyName, nameI, playerSlug, position, comment, jerseyNum, minutes, fieldGoalsMade, fieldGoalsAttempted, fieldGoalsPercentage, threePointersMade, threePointersAttempted, threePointersPercentage, freeThrowsMade, freeThrowsAttempted, freeThrowsPercentage, reboundsOffensive, reboundsDefensive, reboundsTotal, assists, steals, blocks, turnovers, foulsPersonal, points, plusMinusPoints |
| `TeamStarterBenchStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, minutes, fieldGoalsMade, fieldGoalsAttempted, fieldGoalsPercentage, threePointersMade, threePointersAttempted, threePointersPercentage, freeThrowsMade, freeThrowsAttempted, freeThrowsPercentage, reboundsOffensive, reboundsDefensive, reboundsTotal, assists, steals, blocks, turnovers, foulsPersonal, points, startersBench |
| `TeamStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, minutes, fieldGoalsMade, fieldGoalsAttempted, fieldGoalsPercentage, threePointersMade, threePointersAttempted, threePointersPercentage, freeThrowsMade, freeThrowsAttempted, freeThrowsPercentage, reboundsOffensive, reboundsDefensive, reboundsTotal, assists, steals, blocks, turnovers, foulsPersonal, points, plusMinusPoints |

### `boxscoreusagev2`

Parameters: `game_id`, `end_period`, `end_range`, `range_type`, `start_period`, `start_range`

| Table | Columns |
|---|---|
| `sqlPlayersUsage` | GAME_ID, TEAM_ID, TEAM_ABBREVIATION, TEAM_CITY, PLAYER_ID, PLAYER_NAME, START_POSITION, COMMENT, MIN, USG_PCT, PCT_FGM, PCT_FGA, PCT_FG3M, PCT_FG3A, PCT_FTM, PCT_FTA, PCT_OREB, PCT_DREB, PCT_REB, PCT_AST, PCT_TOV, PCT_STL, PCT_BLK, PCT_BLKA, PCT_PF, PCT_PFD, PCT_PTS |
| `sqlTeamsUsage` | GAME_ID, TEAM_ID, TEAM_NAME, TEAM_ABBREVIATION, TEAM_CITY, MIN, USG_PCT, PCT_FGM, PCT_FGA, PCT_FG3M, PCT_FG3A, PCT_FTM, PCT_FTA, PCT_OREB, PCT_DREB, PCT_REB, PCT_AST, PCT_TOV, PCT_STL, PCT_BLK, PCT_BLKA, PCT_PF, PCT_PFD, PCT_PTS |

### `boxscoreusagev3`

Parameters: `game_id`, `end_period`, `end_range`, `range_type`, `start_period`, `start_range`

| Table | Columns |
|---|---|
| `PlayerStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, personId, firstName, familyName, nameI, playerSlug, position, comment, jerseyNum, minutes, usagePercentage, percentageFieldGoalsMade, percentageFieldGoalsAttempted, percentageThreePointersMade, percentageThreePointersAttempted, percentageFreeThrowsMade, percentageFreeThrowsAttempted, percentageReboundsOffensive, percentageReboundsDefensive, percentageReboundsTotal, percentageAssists, percentageTurnovers, percentageSteals, percentageBlocks, percentageBlocksAllowed, percentagePersonalFouls, percentagePersonalFoulsDrawn, percentagePoints |
| `TeamStats` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, minutes, usagePercentage, percentageFieldGoalsMade, percentageFieldGoalsAttempted, percentageThreePointersMade, percentageThreePointersAttempted, percentageFreeThrowsMade, percentageFreeThrowsAttempted, percentageReboundsOffensive, percentageReboundsDefensive, percentageReboundsTotal, percentageAssists, percentageTurnovers, percentageSteals, percentageBlocks, percentageBlocksAllowed, percentagePersonalFouls, percentagePersonalFoulsDrawn, percentagePoints |

### `glalumboxscoresimilarityscore`

Parameters: `person2_id`, `person1_id`, `person1_league_id`, `person1_season_year`, `person1_season_type`, `person2_league_id`, `person2_season_year`, `person2_season_type`

| Table | Columns |
|---|---|
| `GLeagueAlumBoxScoreSimilarityScores` | PERSON_2_ID, PERSON_2, TEAM_ID, SIMILARITY_SCORE |

### `hustlestatsboxscore`

Parameters: `game_id`

| Table | Columns |
|---|---|
| `HustleStatsAvailable` | GAME_ID, HUSTLE_STATUS |
| `PlayerStats` | GAME_ID, TEAM_ID, TEAM_ABBREVIATION, TEAM_CITY, PLAYER_ID, PLAYER_NAME, START_POSITION, COMMENT, MINUTES, PTS, CONTESTED_SHOTS, CONTESTED_SHOTS_2PT, CONTESTED_SHOTS_3PT, DEFLECTIONS, CHARGES_DRAWN, SCREEN_ASSISTS, SCREEN_AST_PTS, OFF_LOOSE_BALLS_RECOVERED, DEF_LOOSE_BALLS_RECOVERED, LOOSE_BALLS_RECOVERED, OFF_BOXOUTS, DEF_BOXOUTS, BOX_OUT_PLAYER_TEAM_REBS, BOX_OUT_PLAYER_REBS, BOX_OUTS |
| `TeamStats` | GAME_ID, TEAM_ID, TEAM_NAME, TEAM_ABBREVIATION, TEAM_CITY, MINUTES, PTS, CONTESTED_SHOTS, CONTESTED_SHOTS_2PT, CONTESTED_SHOTS_3PT, DEFLECTIONS, CHARGES_DRAWN, SCREEN_ASSISTS, SCREEN_AST_PTS, OFF_LOOSE_BALLS_RECOVERED, DEF_LOOSE_BALLS_RECOVERED, LOOSE_BALLS_RECOVERED, OFF_BOXOUTS, DEF_BOXOUTS, BOX_OUT_PLAYER_TEAM_REBS, BOX_OUT_PLAYER_REBS, BOX_OUTS |


## Play-by-play, rotations and win probability (one game)

### `gamerotation` **(used)**

Feeds `stints.csv`.

Parameters: `game_id`, `league_id`

| Table | Columns |
|---|---|
| `AwayTeam` | GAME_ID, TEAM_ID, TEAM_CITY, TEAM_NAME, PERSON_ID, PLAYER_FIRST, PLAYER_LAST, IN_TIME_REAL, OUT_TIME_REAL, PLAYER_PTS, PT_DIFF, USG_PCT |
| `HomeTeam` | GAME_ID, TEAM_ID, TEAM_CITY, TEAM_NAME, PERSON_ID, PLAYER_FIRST, PLAYER_LAST, IN_TIME_REAL, OUT_TIME_REAL, PLAYER_PTS, PT_DIFF, USG_PCT |

### `playbyplay`

Parameters: `game_id`, `end_period`, `start_period`

| Table | Columns |
|---|---|
| `AvailableVideo` | VIDEO_AVAILABLE_FLAG |
| `PlayByPlay` | GAME_ID, EVENTNUM, EVENTMSGTYPE, EVENTMSGACTIONTYPE, PERIOD, WCTIMESTRING, PCTIMESTRING, HOMEDESCRIPTION, NEUTRALDESCRIPTION, VISITORDESCRIPTION, SCORE, SCOREMARGIN |

### `playbyplayv2`

Parameters: `game_id`, `end_period`, `start_period`

| Table | Columns |
|---|---|
| `AvailableVideo` | VIDEO_AVAILABLE_FLAG |
| `PlayByPlay` | GAME_ID, EVENTNUM, EVENTMSGTYPE, EVENTMSGACTIONTYPE, PERIOD, WCTIMESTRING, PCTIMESTRING, HOMEDESCRIPTION, NEUTRALDESCRIPTION, VISITORDESCRIPTION, SCORE, SCOREMARGIN, PERSON1TYPE, PLAYER1_ID, PLAYER1_NAME, PLAYER1_TEAM_ID, PLAYER1_TEAM_CITY, PLAYER1_TEAM_NICKNAME, PLAYER1_TEAM_ABBREVIATION, PERSON2TYPE, PLAYER2_ID, PLAYER2_NAME, PLAYER2_TEAM_ID, PLAYER2_TEAM_CITY, PLAYER2_TEAM_NICKNAME, PLAYER2_TEAM_ABBREVIATION, PERSON3TYPE, PLAYER3_ID, PLAYER3_NAME, PLAYER3_TEAM_ID, PLAYER3_TEAM_CITY, PLAYER3_TEAM_NICKNAME, PLAYER3_TEAM_ABBREVIATION, VIDEO_AVAILABLE_FLAG |

### `playbyplayv3`

Parameters: `game_id`, `end_period`, `start_period`

| Table | Columns |
|---|---|
| `AvailableVideo` | videoAvailable |
| `PlayByPlay` | gameId, actionNumber, clock, period, teamId, teamTricode, personId, playerName, playerNameI, xLegacy, yLegacy, shotDistance, shotResult, isFieldGoal, scoreHome, scoreAway, pointsTotal, location, description, actionType, subType, videoAvailable, actionId |

### `winprobabilitypbp`

Parameters: `game_id`, `run_type`

| Table | Columns |
|---|---|
| `GameInfo` | GAME_ID, GAME_DATE, HOME_TEAM_ID, HOME_TEAM_ABR, HOME_TEAM_PTS, VISITOR_TEAM_ID, VISITOR_TEAM_ABR, VISITOR_TEAM_PTS |
| `WinProbPBP` | GAME_ID, EVENT_NUM, HOME_PCT, VISITOR_PCT, HOME_PTS, VISITOR_PTS, HOME_SCORE_MARGIN, PERIOD, SECONDS_REMAINING, HOME_POSS_IND, HOME_G, DESCRIPTION, LOCATION, PCTIMESTRING, ISVISIBLE |


## Shots and shot locations

### `leaguedashoppptshot`

Parameters: `league_id`, `per_mode_simple`, `season`, `season_type_all_star`, `close_def_dist_range_nullable`, `conference_nullable`, `date_from_nullable`, `date_to_nullable`, `division_nullable`, `dribble_range_nullable`, `game_segment_nullable`, `general_range_nullable`, `last_n_games_nullable`, `location_nullable`, `month_nullable`, `opponent_team_id_nullable`, `outcome_nullable`, `po_round_nullable`, `period_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `shot_dist_range_nullable`, `team_id_nullable`, `touch_time_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `LeagueDashPTShots` | TEAM_ID, TEAM_NAME, TEAM_ABBREVIATION, GP, G, FGA_FREQUENCY, FGM, FGA, FG_PCT, EFG_PCT, FG2A_FREQUENCY, FG2M, FG2A, FG2_PCT, FG3A_FREQUENCY, FG3M, FG3A, FG3_PCT |

### `leaguedashplayerptshot`

Parameters: `league_id`, `per_mode_simple`, `season`, `season_type_all_star`, `close_def_dist_range_nullable`, `college_nullable`, `conference_nullable`, `country_nullable`, `date_from_nullable`, `date_to_nullable`, `division_nullable`, `draft_pick_nullable`, `draft_year_nullable`, `dribble_range_nullable`, `game_segment_nullable`, `general_range_nullable`, `height_nullable`, `last_n_games_nullable`, `location_nullable`, `month_nullable`, `opponent_team_id_nullable`, `outcome_nullable`, `po_round_nullable`, `period_nullable`, `player_experience_nullable`, `player_position_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `shot_dist_range_nullable`, `starter_bench_nullable`, `team_id_nullable`, `touch_time_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`, `weight_nullable`

| Table | Columns |
|---|---|
| `LeagueDashPTShots` | PLAYER_ID, PLAYER_NAME, PLAYER_LAST_TEAM_ID, PLAYER_LAST_TEAM_ABBREVIATION, AGE, GP, G, FGA_FREQUENCY, FGM, FGA, FG_PCT, EFG_PCT, FG2A_FREQUENCY, FG2M, FG2A, FG2_PCT, FG3A_FREQUENCY, FG3M, FG3A, FG3_PCT |

### `leaguedashplayershotlocations`

Parameters: `distance_range`, `last_n_games`, `measure_type_simple`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_all_star`, `college_nullable`, `conference_nullable`, `country_nullable`, `date_from_nullable`, `date_to_nullable`, `division_simple_nullable`, `draft_pick_nullable`, `draft_year_nullable`, `game_scope_simple_nullable`, `game_segment_nullable`, `height_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `player_experience_nullable`, `player_position_abbreviation_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `starter_bench_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`, `weight_nullable`

| Table | Columns |
|---|---|
| `ShotLocations` | PLAYER_ID, PLAYER_NAME, TEAM_ID, TEAM_ABBREVIATION, AGE, then FGM/FGA/FG_PCT for each SHOT_CATEGORY: Restricted Area, In The Paint (Non-RA), Mid-Range, Left Corner 3, Right Corner 3, Above the Break 3, Backcourt |

### `leaguedashteamptshot`

Parameters: `league_id`, `per_mode_simple`, `season`, `season_type_all_star`, `close_def_dist_range_nullable`, `conference_nullable`, `date_from_nullable`, `date_to_nullable`, `division_nullable`, `dribble_range_nullable`, `game_segment_nullable`, `general_range_nullable`, `last_n_games_nullable`, `location_nullable`, `month_nullable`, `opponent_team_id_nullable`, `outcome_nullable`, `po_round_nullable`, `period_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `shot_dist_range_nullable`, `team_id_nullable`, `touch_time_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `LeagueDashPTShots` | TEAM_ID, TEAM_NAME, TEAM_ABBREVIATION, GP, G, FGA_FREQUENCY, FGM, FGA, FG_PCT, EFG_PCT, FG2A_FREQUENCY, FG2M, FG2A, FG2_PCT, FG3A_FREQUENCY, FG3M, FG3A, FG3_PCT |

### `leaguedashteamshotlocations`

Parameters: `distance_range`, `last_n_games`, `measure_type_simple`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_all_star`, `conference_nullable`, `date_from_nullable`, `date_to_nullable`, `division_simple_nullable`, `game_scope_simple_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `player_experience_nullable`, `player_position_abbreviation_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `starter_bench_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `ShotLocations` | TEAM_ID, TEAM_NAME, then FGM/FGA/FG_PCT for each SHOT_CATEGORY: Restricted Area, In The Paint (Non-RA), Mid-Range, Left Corner 3, Right Corner 3, Above the Break 3, Backcourt |

### `playerdashboardbyshootingsplits`

Parameters: `player_id`, `last_n_games`, `measure_type_detailed`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_playoffs`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `AssistedBy` | GROUP_SET, PLAYER_ID, PLAYER_NAME, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, EFG_PCT, BLKA, PCT_AST_2PM, PCT_UAST_2PM, PCT_AST_3PM, PCT_UAST_3PM, PCT_AST_FGM, PCT_UAST_FGM, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, EFG_PCT_RANK, BLKA_RANK, PCT_AST_2PM_RANK, PCT_UAST_2PM_RANK, PCT_AST_3PM_RANK, PCT_UAST_3PM_RANK, PCT_AST_FGM_RANK, PCT_UAST_FGM_RANK, CFID, CFPARAMS |
| `AssitedShotPlayerDashboard` | GROUP_SET, GROUP_VALUE, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, EFG_PCT, BLKA, PCT_AST_2PM, PCT_UAST_2PM, PCT_AST_3PM, PCT_UAST_3PM, PCT_AST_FGM, PCT_UAST_FGM, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, EFG_PCT_RANK, BLKA_RANK, PCT_AST_2PM_RANK, PCT_UAST_2PM_RANK, PCT_AST_3PM_RANK, PCT_UAST_3PM_RANK, PCT_AST_FGM_RANK, PCT_UAST_FGM_RANK, CFID, CFPARAMS |
| `OverallPlayerDashboard` | GROUP_SET, GROUP_VALUE, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, EFG_PCT, BLKA, PCT_AST_2PM, PCT_UAST_2PM, PCT_AST_3PM, PCT_UAST_3PM, PCT_AST_FGM, PCT_UAST_FGM, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, EFG_PCT_RANK, BLKA_RANK, PCT_AST_2PM_RANK, PCT_UAST_2PM_RANK, PCT_AST_3PM_RANK, PCT_UAST_3PM_RANK, PCT_AST_FGM_RANK, PCT_UAST_FGM_RANK, CFID, CFPARAMS |
| `Shot5FTPlayerDashboard` | GROUP_SET, GROUP_VALUE, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, EFG_PCT, BLKA, PCT_AST_2PM, PCT_UAST_2PM, PCT_AST_3PM, PCT_UAST_3PM, PCT_AST_FGM, PCT_UAST_FGM, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, EFG_PCT_RANK, BLKA_RANK, PCT_AST_2PM_RANK, PCT_UAST_2PM_RANK, PCT_AST_3PM_RANK, PCT_UAST_3PM_RANK, PCT_AST_FGM_RANK, PCT_UAST_FGM_RANK, CFID, CFPARAMS |
| `Shot8FTPlayerDashboard` | GROUP_SET, GROUP_VALUE, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, EFG_PCT, BLKA, PCT_AST_2PM, PCT_UAST_2PM, PCT_AST_3PM, PCT_UAST_3PM, PCT_AST_FGM, PCT_UAST_FGM, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, EFG_PCT_RANK, BLKA_RANK, PCT_AST_2PM_RANK, PCT_UAST_2PM_RANK, PCT_AST_3PM_RANK, PCT_UAST_3PM_RANK, PCT_AST_FGM_RANK, PCT_UAST_FGM_RANK, CFID, CFPARAMS |
| `ShotAreaPlayerDashboard` | GROUP_SET, GROUP_VALUE, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, EFG_PCT, BLKA, PCT_AST_2PM, PCT_UAST_2PM, PCT_AST_3PM, PCT_UAST_3PM, PCT_AST_FGM, PCT_UAST_FGM, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, EFG_PCT_RANK, BLKA_RANK, PCT_AST_2PM_RANK, PCT_UAST_2PM_RANK, PCT_AST_3PM_RANK, PCT_UAST_3PM_RANK, PCT_AST_FGM_RANK, PCT_UAST_FGM_RANK, CFID, CFPARAMS |
| `ShotTypePlayerDashboard` | GROUP_SET, GROUP_VALUE, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, EFG_PCT, BLKA, PCT_AST_2PM, PCT_UAST_2PM, PCT_AST_3PM, PCT_UAST_3PM, PCT_AST_FGM, PCT_UAST_FGM, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, EFG_PCT_RANK, BLKA_RANK, PCT_AST_2PM_RANK, PCT_UAST_2PM_RANK, PCT_AST_3PM_RANK, PCT_UAST_3PM_RANK, PCT_AST_FGM_RANK, PCT_UAST_FGM_RANK, CFID, CFPARAMS |
| `ShotTypeSummaryPlayerDashboard` | GROUP_SET, GROUP_VALUE, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, EFG_PCT, BLKA, PCT_AST_2PM, PCT_UAST_2PM, PCT_AST_3PM, PCT_UAST_3PM, PCT_AST_FGM, PCT_UAST_FGM, CFID, CFPARAMS |

### `playerdashptshots`

Parameters: `team_id`, `player_id`, `last_n_games`, `league_id`, `month`, `opponent_team_id`, `per_mode_simple`, `period`, `season`, `season_type_all_star`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `location_nullable`, `outcome_nullable`, `season_segment_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `ClosestDefender10ftPlusShooting` | PLAYER_ID, PLAYER_NAME_LAST_FIRST, SORT_ORDER, GP, G, CLOSE_DEF_DIST_RANGE, FGA_FREQUENCY, FGM, FGA, FG_PCT, EFG_PCT, FG2A_FREQUENCY, FG2M, FG2A, FG2_PCT, FG3A_FREQUENCY, FG3M, FG3A, FG3_PCT |
| `ClosestDefenderShooting` | PLAYER_ID, PLAYER_NAME_LAST_FIRST, SORT_ORDER, GP, G, CLOSE_DEF_DIST_RANGE, FGA_FREQUENCY, FGM, FGA, FG_PCT, EFG_PCT, FG2A_FREQUENCY, FG2M, FG2A, FG2_PCT, FG3A_FREQUENCY, FG3M, FG3A, FG3_PCT |
| `DribbleShooting` | PLAYER_ID, PLAYER_NAME_LAST_FIRST, SORT_ORDER, GP, G, DRIBBLE_RANGE, FGA_FREQUENCY, FGM, FGA, FG_PCT, EFG_PCT, FG2A_FREQUENCY, FG2M, FG2A, FG2_PCT, FG3A_FREQUENCY, FG3M, FG3A, FG3_PCT |
| `GeneralShooting` | PLAYER_ID, PLAYER_NAME_LAST_FIRST, SORT_ORDER, GP, G, SHOT_TYPE, FGA_FREQUENCY, FGM, FGA, FG_PCT, EFG_PCT, FG2A_FREQUENCY, FG2M, FG2A, FG2_PCT, FG3A_FREQUENCY, FG3M, FG3A, FG3_PCT |
| `Overall` | PLAYER_ID, PLAYER_NAME_LAST_FIRST, SORT_ORDER, GP, G, SHOT_TYPE, FGA_FREQUENCY, FGM, FGA, FG_PCT, EFG_PCT, FG2A_FREQUENCY, FG2M, FG2A, FG2_PCT, FG3A_FREQUENCY, FG3M, FG3A, FG3_PCT |
| `ShotClockShooting` | PLAYER_ID, PLAYER_NAME_LAST_FIRST, SORT_ORDER, GP, G, SHOT_CLOCK_RANGE, FGA_FREQUENCY, FGM, FGA, FG_PCT, EFG_PCT, FG2A_FREQUENCY, FG2M, FG2A, FG2_PCT, FG3A_FREQUENCY, FG3M, FG3A, FG3_PCT |
| `TouchTimeShooting` | PLAYER_ID, PLAYER_NAME_LAST_FIRST, SORT_ORDER, GP, G, TOUCH_TIME_RANGE, FGA_FREQUENCY, FGM, FGA, FG_PCT, EFG_PCT, FG2A_FREQUENCY, FG2M, FG2A, FG2_PCT, FG3A_FREQUENCY, FG3M, FG3A, FG3_PCT |

### `shotchartdetail` **(used)**

Feeds `shots.csv, shot_zone_averages.csv`.

Parameters: `team_id`, `player_id`, `context_measure_simple`, `last_n_games`, `league_id`, `month`, `opponent_team_id`, `period`, `season_type_all_star`, `ahead_behind_nullable`, `clutch_time_nullable`, `context_filter_nullable`, `date_from_nullable`, `date_to_nullable`, `end_period_nullable`, `end_range_nullable`, `game_id_nullable`, `game_segment_nullable`, `location_nullable`, `outcome_nullable`, `player_position_nullable`, `point_diff_nullable`, `position_nullable`, `range_type_nullable`, `rookie_year_nullable`, `season_nullable`, `season_segment_nullable`, `start_period_nullable`, `start_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `LeagueAverages` | GRID_TYPE, SHOT_ZONE_BASIC, SHOT_ZONE_AREA, SHOT_ZONE_RANGE, FGA, FGM, FG_PCT |
| `Shot_Chart_Detail` | GRID_TYPE, GAME_ID, GAME_EVENT_ID, PLAYER_ID, PLAYER_NAME, TEAM_ID, TEAM_NAME, PERIOD, MINUTES_REMAINING, SECONDS_REMAINING, EVENT_TYPE, ACTION_TYPE, SHOT_TYPE, SHOT_ZONE_BASIC, SHOT_ZONE_AREA, SHOT_ZONE_RANGE, SHOT_DISTANCE, LOC_X, LOC_Y, SHOT_ATTEMPTED_FLAG, SHOT_MADE_FLAG, GAME_DATE, HTM, VTM |

### `shotchartleaguewide`

Parameters: `league_id`, `season`

| Table | Columns |
|---|---|
| `League_Wide` | GRID_TYPE, SHOT_ZONE_BASIC, SHOT_ZONE_AREA, SHOT_ZONE_RANGE, FGA, FGM, FG_PCT |

### `shotchartlineupdetail`

Parameters: `context_measure_detailed`, `group_id`, `league_id`, `period`, `season`, `season_type_all_star`, `context_filter_nullable`, `date_from_nullable`, `date_to_nullable`, `game_id_nullable`, `game_segment_nullable`, `last_n_games_nullable`, `location_nullable`, `month_nullable`, `opponent_team_id_nullable`, `outcome_nullable`, `season_segment_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `ShotChartLineupDetail` | GRID_TYPE, GAME_ID, GAME_EVENT_ID, GROUP_ID, GROUP_NAME, PLAYER_ID, PLAYER_NAME, TEAM_ID, TEAM_NAME, PERIOD, MINUTES_REMAINING, SECONDS_REMAINING, EVENT_TYPE, ACTION_TYPE, SHOT_TYPE, SHOT_ZONE_BASIC, SHOT_ZONE_AREA, SHOT_ZONE_RANGE, SHOT_DISTANCE, LOC_X, LOC_Y, SHOT_ATTEMPTED_FLAG, SHOT_MADE_FLAG, GAME_DATE, HTM, VTM |
| `ShotChartLineupLeagueAverage` | GRID_TYPE, SHOT_ZONE_BASIC, SHOT_ZONE_AREA, SHOT_ZONE_RANGE, FGA, FGM, FG_PCT |

### `teamdashboardbyshootingsplits`

Parameters: `team_id`, `last_n_games`, `measure_type_detailed_defense`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_all_star`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `AssistedBy` | GROUP_SET, PLAYER_ID, PLAYER_NAME, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, EFG_PCT, BLKA, PCT_AST_2PM, PCT_UAST_2PM, PCT_AST_3PM, PCT_UAST_3PM, PCT_AST_FGM, PCT_UAST_FGM, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, EFG_PCT_RANK, BLKA_RANK, PCT_AST_2PM_RANK, PCT_UAST_2PM_RANK, PCT_AST_3PM_RANK, PCT_UAST_3PM_RANK, PCT_AST_FGM_RANK, PCT_UAST_FGM_RANK, CFID, CFPARAMS |
| `AssitedShotTeamDashboard` | GROUP_SET, GROUP_VALUE, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, EFG_PCT, BLKA, PCT_AST_2PM, PCT_UAST_2PM, PCT_AST_3PM, PCT_UAST_3PM, PCT_AST_FGM, PCT_UAST_FGM, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, EFG_PCT_RANK, BLKA_RANK, PCT_AST_2PM_RANK, PCT_UAST_2PM_RANK, PCT_AST_3PM_RANK, PCT_UAST_3PM_RANK, PCT_AST_FGM_RANK, PCT_UAST_FGM_RANK, CFID, CFPARAMS |
| `OverallTeamDashboard` | GROUP_SET, GROUP_VALUE, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, EFG_PCT, BLKA, PCT_AST_2PM, PCT_UAST_2PM, PCT_AST_3PM, PCT_UAST_3PM, PCT_AST_FGM, PCT_UAST_FGM, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, EFG_PCT_RANK, BLKA_RANK, PCT_AST_2PM_RANK, PCT_UAST_2PM_RANK, PCT_AST_3PM_RANK, PCT_UAST_3PM_RANK, PCT_AST_FGM_RANK, PCT_UAST_FGM_RANK, CFID, CFPARAMS |
| `Shot5FTTeamDashboard` | GROUP_SET, GROUP_VALUE, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, EFG_PCT, BLKA, PCT_AST_2PM, PCT_UAST_2PM, PCT_AST_3PM, PCT_UAST_3PM, PCT_AST_FGM, PCT_UAST_FGM, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, EFG_PCT_RANK, BLKA_RANK, PCT_AST_2PM_RANK, PCT_UAST_2PM_RANK, PCT_AST_3PM_RANK, PCT_UAST_3PM_RANK, PCT_AST_FGM_RANK, PCT_UAST_FGM_RANK, CFID, CFPARAMS |
| `Shot8FTTeamDashboard` | GROUP_SET, GROUP_VALUE, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, EFG_PCT, BLKA, PCT_AST_2PM, PCT_UAST_2PM, PCT_AST_3PM, PCT_UAST_3PM, PCT_AST_FGM, PCT_UAST_FGM, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, EFG_PCT_RANK, BLKA_RANK, PCT_AST_2PM_RANK, PCT_UAST_2PM_RANK, PCT_AST_3PM_RANK, PCT_UAST_3PM_RANK, PCT_AST_FGM_RANK, PCT_UAST_FGM_RANK, CFID, CFPARAMS |
| `ShotAreaTeamDashboard` | GROUP_SET, GROUP_VALUE, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, EFG_PCT, BLKA, PCT_AST_2PM, PCT_UAST_2PM, PCT_AST_3PM, PCT_UAST_3PM, PCT_AST_FGM, PCT_UAST_FGM, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, EFG_PCT_RANK, BLKA_RANK, PCT_AST_2PM_RANK, PCT_UAST_2PM_RANK, PCT_AST_3PM_RANK, PCT_UAST_3PM_RANK, PCT_AST_FGM_RANK, PCT_UAST_FGM_RANK, CFID, CFPARAMS |
| `ShotTypeTeamDashboard` | GROUP_SET, GROUP_VALUE, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, EFG_PCT, BLKA, PCT_AST_2PM, PCT_UAST_2PM, PCT_AST_3PM, PCT_UAST_3PM, PCT_AST_FGM, PCT_UAST_FGM, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, EFG_PCT_RANK, BLKA_RANK, PCT_AST_2PM_RANK, PCT_UAST_2PM_RANK, PCT_AST_3PM_RANK, PCT_UAST_3PM_RANK, PCT_AST_FGM_RANK, PCT_UAST_FGM_RANK, CFID, CFPARAMS |

### `teamdashptshots`

Parameters: `team_id`, `last_n_games`, `league_id`, `month`, `opponent_team_id`, `per_mode_simple`, `period`, `season`, `season_type_all_star`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `location_nullable`, `outcome_nullable`, `season_segment_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `ClosestDefender10ftPlusShooting` | TEAM_ID, TEAM_NAME, SORT_ORDER, G, CLOSE_DEF_DIST_RANGE, FGA_FREQUENCY, FGM, FGA, FG_PCT, EFG_PCT, FG2A_FREQUENCY, FG2M, FG2A, FG2_PCT, FG3A_FREQUENCY, FG3M, FG3A, FG3_PCT |
| `ClosestDefenderShooting` | TEAM_ID, TEAM_NAME, SORT_ORDER, G, CLOSE_DEF_DIST_RANGE, FGA_FREQUENCY, FGM, FGA, FG_PCT, EFG_PCT, FG2A_FREQUENCY, FG2M, FG2A, FG2_PCT, FG3A_FREQUENCY, FG3M, FG3A, FG3_PCT |
| `DribbleShooting` | TEAM_ID, TEAM_NAME, SORT_ORDER, G, DRIBBLE_RANGE, FGA_FREQUENCY, FGM, FGA, FG_PCT, EFG_PCT, FG2A_FREQUENCY, FG2M, FG2A, FG2_PCT, FG3A_FREQUENCY, FG3M, FG3A, FG3_PCT |
| `GeneralShooting` | TEAM_ID, TEAM_NAME, SORT_ORDER, G, SHOT_TYPE, FGA_FREQUENCY, FGM, FGA, FG_PCT, EFG_PCT, FG2A_FREQUENCY, FG2M, FG2A, FG2_PCT, FG3A_FREQUENCY, FG3M, FG3A, FG3_PCT |
| `ShotClockShooting` | TEAM_ID, TEAM_NAME, SORT_ORDER, G, SHOT_CLOCK_RANGE, FGA_FREQUENCY, FGM, FGA, FG_PCT, EFG_PCT, FG2A_FREQUENCY, FG2M, FG2A, FG2_PCT, FG3A_FREQUENCY, FG3M, FG3A, FG3_PCT |
| `TouchTimeShooting` | TEAM_ID, TEAM_NAME, SORT_ORDER, G, TOUCH_TIME_RANGE, FGA_FREQUENCY, FGM, FGA, FG_PCT, EFG_PCT, FG2A_FREQUENCY, FG2M, FG2A, FG2_PCT, FG3A_FREQUENCY, FG3M, FG3A, FG3_PCT |


## Game logs and game finders

### `cumestatsplayer`

Parameters: `player_id`, `game_ids`, `league_id`, `season`, `season_type_all_star`

| Table | Columns |
|---|---|
| `GameByGameStats` | DATE_EST, VISITOR_TEAM, HOME_TEAM, GP, GS, ACTUAL_MINUTES, ACTUAL_SECONDS, FG, FGA, FG_PCT, FG3, FG3A, FG3_PCT, FT, FTA, FT_PCT, OFF_REB, DEF_REB, TOT_REB, AVG_TOT_REB, AST, PF, DQ, STL, TURNOVERS, BLK, PTS, AVG_PTS |
| `TotalPlayerStats` | DISPLAY_FI_LAST, PERSON_ID, JERSEY_NUM, GP, GS, ACTUAL_MINUTES, ACTUAL_SECONDS, FG, FGA, FG_PCT, FG3, FG3A, FG3_PCT, FT, FTA, FT_PCT, OFF_REB, DEF_REB, TOT_REB, AST, PF, DQ, STL, TURNOVERS, BLK, PTS, MAX_ACTUAL_MINUTES, MAX_ACTUAL_SECONDS, MAX_REB, MAX_AST, MAX_STL, MAX_TURNOVERS, MAX_BLK, MAX_PTS, AVG_ACTUAL_MINUTES, AVG_ACTUAL_SECONDS, AVG_TOT_REB, AVG_AST, AVG_STL, AVG_TURNOVERS, AVG_BLK, AVG_PTS, PER_MIN_TOT_REB, PER_MIN_AST, PER_MIN_STL, PER_MIN_TURNOVERS, PER_MIN_BLK, PER_MIN_PTS |

### `cumestatsplayergames`

Parameters: `player_id`, `league_id`, `season`, `season_type_all_star`, `location_nullable`, `outcome_nullable`, `vs_conference_nullable`, `vs_division_nullable`, `vs_team_id_nullable`

| Table | Columns |
|---|---|
| `CumeStatsPlayerGames` | MATCHUP, GAME_ID |

### `cumestatsteam`

Parameters: `team_id`, `game_ids`, `league_id`, `season`, `season_type_all_star`

| Table | Columns |
|---|---|
| `GameByGameStats` | JERSEY_NUM, PLAYER, PERSON_ID, TEAM_ID, GP, GS, ACTUAL_MINUTES, ACTUAL_SECONDS, FG, FGA, FG_PCT, FG3, FG3A, FG3_PCT, FT, FTA, FT_PCT, OFF_REB, DEF_REB, TOT_REB, AST, PF, DQ, STL, TURNOVERS, BLK, PTS, MAX_ACTUAL_MINUTES, MAX_ACTUAL_SECONDS, MAX_REB, MAX_AST, MAX_STL, MAX_TURNOVERS, MAX_BLKP, MAX_PTS, AVG_ACTUAL_MINUTES, AVG_ACTUAL_SECONDS, AVG_REB, AVG_AST, AVG_STL, AVG_TURNOVERS, AVG_BLKP, AVG_PTS, PER_MIN_REB, PER_MIN_AST, PER_MIN_STL, PER_MIN_TURNOVERS, PER_MIN_BLK, PER_MIN_PTS |
| `TotalTeamStats` | CITY, NICKNAME, TEAM_ID, W, L, W_HOME, L_HOME, W_ROAD, L_ROAD, TEAM_TURNOVERS, TEAM_REBOUNDS, GP, GS, ACTUAL_MINUTES, ACTUAL_SECONDS, FG, FGA, FG_PCT, FG3, FG3A, FG3_PCT, FT, FTA, FT_PCT, OFF_REB, DEF_REB, TOT_REB, AST, PF, STL, TOTAL_TURNOVERS, BLK, PTS, AVG_REB, AVG_PTS, DQ |

### `cumestatsteamgames`

Parameters: `team_id`, `league_id`, `season`, `season_type_all_star`, `location_nullable`, `outcome_nullable`, `season_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`, `vs_team_id_nullable`

| Table | Columns |
|---|---|
| `CumeStatsTeamGames` | MATCHUP, GAME_ID |

### `leaguegamefinder`

Parameters: `player_or_team_abbreviation`, `conference_nullable`, `date_from_nullable`, `date_to_nullable`, `division_simple_nullable`, `draft_number_nullable`, `draft_round_nullable`, `draft_team_id_nullable`, `draft_year_nullable`, `eq_ast_nullable`, `eq_blk_nullable`, `eq_dd_nullable`, `eq_dreb_nullable`, `eq_fg3a_nullable`, `eq_fg3m_nullable`, `eq_fg3_pct_nullable`, `eq_fga_nullable`, `eq_fgm_nullable`, `eq_fg_pct_nullable`, `eq_fta_nullable`, `eq_ftm_nullable`, `eq_ft_pct_nullable`, `eq_minutes_nullable`, `eq_oreb_nullable`, `eq_pf_nullable`, `eq_pts_nullable`, `eq_reb_nullable`, `eq_stl_nullable`, `eq_td_nullable`, `eq_tov_nullable`, `game_id_nullable`, `gt_ast_nullable`, `gt_blk_nullable`, `gt_dd_nullable`, `gt_dreb_nullable`, `gt_fg3a_nullable`, `gt_fg3m_nullable`, `gt_fg3_pct_nullable`, `gt_fga_nullable`, `gt_fgm_nullable`, `gt_fg_pct_nullable`, `gt_fta_nullable`, `gt_ftm_nullable`, `gt_ft_pct_nullable`, `gt_minutes_nullable`, `gt_oreb_nullable`, `gt_pf_nullable`, `gt_pts_nullable`, `gt_reb_nullable`, `gt_stl_nullable`, `gt_td_nullable`, `gt_tov_nullable`, `league_id_nullable`, `location_nullable`, `lt_ast_nullable`, `lt_blk_nullable`, `lt_dd_nullable`, `lt_dreb_nullable`, `lt_fg3a_nullable`, `lt_fg3m_nullable`, `lt_fg3_pct_nullable`, `lt_fga_nullable`, `lt_fgm_nullable`, `lt_fg_pct_nullable`, `lt_fta_nullable`, `lt_ftm_nullable`, `lt_ft_pct_nullable`, `lt_minutes_nullable`, `lt_oreb_nullable`, `lt_pf_nullable`, `lt_pts_nullable`, `lt_reb_nullable`, `lt_stl_nullable`, `lt_td_nullable`, `lt_tov_nullable`, `outcome_nullable`, `po_round_nullable`, `player_id_nullable`, `rookie_year_nullable`, `season_nullable`, `season_segment_nullable`, `season_type_nullable`, `starter_bench_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`, `vs_team_id_nullable`, `years_experience_nullable`

| Table | Columns |
|---|---|
| `LeagueGameFinderResults` | SEASON_ID, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, GAME_ID, GAME_DATE, MATCHUP, WL, MIN, PTS, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PLUS_MINUS |

### `leaguegamelog` **(used)**

Feeds `games.csv, player_game_log.csv`.

Parameters: `counter`, `direction`, `league_id`, `player_or_team_abbreviation`, `season`, `season_type_all_star`, `sorter`, `date_from_nullable`, `date_to_nullable`

| Table | Columns |
|---|---|
| `LeagueGameLog` | SEASON_ID, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, GAME_ID, GAME_DATE, MATCHUP, WL, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS, PLUS_MINUS, VIDEO_AVAILABLE |

### `playergamelog`

Parameters: `player_id`, `season`, `season_type_all_star`, `date_from_nullable`, `date_to_nullable`, `league_id_nullable`

| Table | Columns |
|---|---|
| `PlayerGameLog` | SEASON_ID, Player_ID, Game_ID, GAME_DATE, MATCHUP, WL, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS, PLUS_MINUS, VIDEO_AVAILABLE |

### `playergamelogs`

Parameters: `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `last_n_games_nullable`, `league_id_nullable`, `location_nullable`, `measure_type_player_game_logs_nullable`, `month_nullable`, `opp_team_id_nullable`, `outcome_nullable`, `po_round_nullable`, `per_mode_simple_nullable`, `period_nullable`, `player_id_nullable`, `season_nullable`, `season_segment_nullable`, `season_type_nullable`, `shot_clock_range_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `PlayerGameLogs` | SEASON_YEAR, PLAYER_ID, PLAYER_NAME, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, GAME_ID, GAME_DATE, MATCHUP, WL, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK |

### `playergamestreakfinder`

Parameters: `active_streaks_only_nullable`, `conference_nullable`, `date_from_nullable`, `date_to_nullable`, `division_simple_nullable`, `draft_number_nullable`, `draft_round_nullable`, `draft_team_id_nullable`, `draft_year_nullable`, `eq_ast_nullable`, `eq_blk_nullable`, `eq_dd_nullable`, `eq_dreb_nullable`, `eq_fg3a_nullable`, `eq_fg3m_nullable`, `eq_fg3_pct_nullable`, `eq_fga_nullable`, `eq_fgm_nullable`, `eq_fg_pct_nullable`, `eq_fta_nullable`, `eq_ftm_nullable`, `eq_ft_pct_nullable`, `eq_minutes_nullable`, `eq_oreb_nullable`, `eq_pf_nullable`, `eq_pts_nullable`, `eq_reb_nullable`, `eq_stl_nullable`, `eq_td_nullable`, `eq_tov_nullable`, `game_id_nullable`, `gt_ast_nullable`, `gt_blk_nullable`, `gt_dd_nullable`, `gt_dreb_nullable`, `gt_fg3a_nullable`, `gt_fg3m_nullable`, `gt_fg3_pct_nullable`, `gt_fga_nullable`, `gt_fgm_nullable`, `gt_fg_pct_nullable`, `gt_fta_nullable`, `gt_ftm_nullable`, `gt_ft_pct_nullable`, `gt_minutes_nullable`, `gt_oreb_nullable`, `gt_pf_nullable`, `gt_pts_nullable`, `gt_reb_nullable`, `gt_stl_nullable`, `gt_td_nullable`, `gt_tov_nullable`, `league_id_nullable`, `location_nullable`, `lt_ast_nullable`, `lt_blk_nullable`, `lt_dd_nullable`, `lt_dreb_nullable`, `lt_fg3a_nullable`, `lt_fg3m_nullable`, `lt_fg3_pct_nullable`, `lt_fga_nullable`, `lt_fgm_nullable`, `lt_fg_pct_nullable`, `lt_fta_nullable`, `lt_ftm_nullable`, `lt_ft_pct_nullable`, `lt_minutes_nullable`, `lt_oreb_nullable`, `lt_pf_nullable`, `lt_pts_nullable`, `lt_reb_nullable`, `lt_stl_nullable`, `lt_td_nullable`, `lt_tov_nullable`, `min_games_nullable`, `outcome_nullable`, `po_round_nullable`, `player_id_nullable`, `rookie_year_nullable`, `season_nullable`, `season_segment_nullable`, `season_type_nullable`, `starter_bench_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`, `vs_team_id_nullable`, `years_experience_nullable`

| Table | Columns |
|---|---|
| `PlayerGameStreakFinderResults` | PLAYER_NAME_LAST_FIRST, PLAYER_ID, GAMESTREAK, STARTDATE, ENDDATE, ACTIVESTREAK, NUMSEASONS, LASTSEASON, FIRSTSEASON |

### `teamgamelog`

Parameters: `team_id`, `season`, `season_type_all_star`, `date_from_nullable`, `date_to_nullable`, `league_id_nullable`

| Table | Columns |
|---|---|
| `TeamGameLog` | Team_ID, Game_ID, GAME_DATE, MATCHUP, WL, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |

### `teamgamelogs`

Parameters: `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `last_n_games_nullable`, `league_id_nullable`, `location_nullable`, `measure_type_player_game_logs_nullable`, `month_nullable`, `opp_team_id_nullable`, `outcome_nullable`, `po_round_nullable`, `per_mode_simple_nullable`, `period_nullable`, `player_id_nullable`, `season_nullable`, `season_segment_nullable`, `season_type_nullable`, `shot_clock_range_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `TeamGameLogs` | SEASON_YEAR, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, GAME_ID, GAME_DATE, MATCHUP, WL, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK |

### `teamgamestreakfinder`

Parameters: `active_streaks_only_nullable`, `active_teams_only_nullable`, `btr_opp_ast_nullable`, `btr_opp_blk_nullable`, `btr_opp_dreb_nullable`, `btr_opp_fg3a_nullable`, `btr_opp_fg3m_nullable`, `btr_opp_fg3_pct_nullable`, `btr_opp_fga_nullable`, `btr_opp_fgm_nullable`, `btr_opp_fg_pct_nullable`, `btr_opp_fta_nullable`, `btr_opp_ftm_nullable`, `btr_opp_ft_pct_nullable`, `btr_opp_oreb_nullable`, `btr_opp_pf_nullable`, `btr_opp_pts_nullable`, `btr_opp_pts2nd_chance_nullable`, `btr_opp_pts_fb_nullable`, `btr_opp_pts_off_tov_nullable`, `btr_opp_pts_paint_nullable`, `btr_opp_reb_nullable`, `btr_opp_stl_nullable`, `btr_opp_tov_nullable`, `conference_nullable`, `date_from_nullable`, `date_to_nullable`, `division_simple_nullable`, `eq_ast_nullable`, `eq_blk_nullable`, `eq_dd_nullable`, `eq_dreb_nullable`, `eq_fg3a_nullable`, `eq_fg3m_nullable`, `eq_fg3_pct_nullable`, `eq_fga_nullable`, `eq_fgm_nullable`, `eq_fg_pct_nullable`, `eq_fta_nullable`, `eq_ftm_nullable`, `eq_ft_pct_nullable`, `eq_minutes_nullable`, `eq_opp_pts2nd_chance_nullable`, `eq_opp_pts_fb_nullable`, `eq_opp_pts_off_tov_nullable`, `eq_opp_pts_paint_nullable`, `eq_oreb_nullable`, `eq_pf_nullable`, `eq_pts_nullable`, `eq_pts2nd_chance_nullable`, `eq_pts_fb_nullable`, `eq_pts_off_tov_nullable`, `eq_pts_paint_nullable`, `eq_reb_nullable`, `eq_stl_nullable`, `eq_td_nullable`, `eq_tov_nullable`, `game_id_nullable`, `gt_ast_nullable`, `gt_blk_nullable`, `gt_dd_nullable`, `gt_dreb_nullable`, `gt_fg3a_nullable`, `gt_fg3m_nullable`, `gt_fg3_pct_nullable`, `gt_fga_nullable`, `gt_fgm_nullable`, `gt_fg_pct_nullable`, `gt_fta_nullable`, `gt_ftm_nullable`, `gt_ft_pct_nullable`, `gt_minutes_nullable`, `gt_opp_ast_nullable`, `gt_opp_blk_nullable`, `gt_opp_dreb_nullable`, `gt_opp_fg3a_nullable`, `gt_opp_fg3m_nullable`, `gt_opp_fg3_pct_nullable`, `gt_opp_fga_nullable`, `gt_opp_fgm_nullable`, `gt_opp_fg_pct_nullable`, `gt_opp_fta_nullable`, `gt_opp_ftm_nullable`, `gt_opp_ft_pct_nullable`, `gt_opp_oreb_nullable`, `gt_opp_pf_nullable`, `gt_opp_pts_nullable`, `gt_opp_pts2nd_chance_nullable`, `gt_opp_pts_fb_nullable`, `gt_opp_pts_off_tov_nullable`, `gt_opp_pts_paint_nullable`, `gt_opp_reb_nullable`, `gt_opp_stl_nullable`, `gt_opp_tov_nullable`, `gt_oreb_nullable`, `gt_pf_nullable`, `gt_pts_nullable`, `gt_pts2nd_chance_nullable`, `gt_pts_fb_nullable`, `gt_pts_off_tov_nullable`, `gt_pts_paint_nullable`, `gt_reb_nullable`, `gt_stl_nullable`, `gt_td_nullable`, `gt_tov_nullable`, `lstreak_nullable`, `league_id_nullable`, `location_nullable`, `lt_ast_nullable`, `lt_blk_nullable`, `lt_dd_nullable`, `lt_dreb_nullable`, `lt_fg3a_nullable`, `lt_fg3m_nullable`, `lt_fg3_pct_nullable`, `lt_fga_nullable`, `lt_fgm_nullable`, `lt_fg_pct_nullable`, `lt_fta_nullable`, `lt_ftm_nullable`, `lt_ft_pct_nullable`, `lt_minutes_nullable`, `lt_opp_ast_nullable`, `lt_opp_blk_nullable`, `lt_opp_dreb_nullable`, `lt_opp_fg3a_nullable`, `lt_opp_fg3m_nullable`, `lt_opp_fg3_pct_nullable`, `lt_opp_fga_nullable`, `lt_opp_fgm_nullable`, `lt_opp_fg_pct_nullable`, `lt_opp_fta_nullable`, `lt_opp_ftm_nullable`, `lt_opp_ft_pct_nullable`, `lt_opp_oreb_nullable`, `lt_opp_pf_nullable`, `lt_opp_pts_nullable`, `lt_opp_pts2nd_chance_nullable`, `lt_opp_pts_fb_nullable`, `lt_opp_pts_off_tov_nullable`, `lt_opp_pts_paint_nullable`, `lt_opp_reb_nullable`, `lt_opp_stl_nullable`, `lt_opp_tov_nullable`, `lt_oreb_nullable`, `lt_pf_nullable`, `lt_pts_nullable`, `lt_pts2nd_chance_nullable`, `lt_pts_fb_nullable`, `lt_pts_off_tov_nullable`, `lt_pts_paint_nullable`, `lt_reb_nullable`, `lt_stl_nullable`, `lt_td_nullable`, `lt_tov_nullable`, `min_games_nullable`, `outcome_nullable`, `po_round_nullable`, `season_nullable`, `season_segment_nullable`, `season_type_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`, `vs_team_id_nullable`, `wstreak_nullable`, `wrs_opp_ast_nullable`, `wrs_opp_blk_nullable`, `wrs_opp_dreb_nullable`, `wrs_opp_fg3a_nullable`, `wrs_opp_fg3m_nullable`, `wrs_opp_fg3_pct_nullable`, `wrs_opp_fga_nullable`, `wrs_opp_fgm_nullable`, `wrs_opp_fg_pct_nullable`, `wrs_opp_fta_nullable`, `wrs_opp_ftm_nullable`, `wrs_opp_ft_pct_nullable`, `wrs_opp_oreb_nullable`, `wrs_opp_pf_nullable`, `wrs_opp_pts_nullable`, `wrs_opp_pts2nd_chance_nullable`, `wrs_opp_pts_fb_nullable`, `wrs_opp_pts_off_tov_nullable`, `wrs_opp_pts_paint_nullable`, `wrs_opp_reb_nullable`, `wrs_opp_stl_nullable`, `wrs_opp_tov_nullable`

| Table | Columns |
|---|---|
| `TeamGameStreakFinderParametersResults` | TEAM_NAME, TEAM_ID, GAMESTREAK, STARTDATE, ENDDATE, ACTIVESTREAK, NUMSEASONS, LASTSEASON, FIRSTSEASON, ABBREVIATION |


## Lineups and on/off

### `leaguedashlineups`

Parameters: `group_quantity`, `last_n_games`, `measure_type_detailed_defense`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_all_star`, `conference_nullable`, `date_from_nullable`, `date_to_nullable`, `division_simple_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `Lineups` | GROUP_SET, GROUP_ID, GROUP_NAME, TEAM_ID, TEAM_ABBREVIATION, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK |

### `leaguelineupviz`

Parameters: `minutes_min`, `group_quantity`, `last_n_games`, `measure_type_detailed_defense`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_all_star`, `conference_nullable`, `date_from_nullable`, `date_to_nullable`, `division_simple_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `LeagueLineupViz` | GROUP_ID, GROUP_NAME, TEAM_ID, TEAM_ABBREVIATION, MIN, OFF_RATING, DEF_RATING, NET_RATING, PACE, TS_PCT, FTA_RATE, TM_AST_PCT, PCT_FGA_2PT, PCT_FGA_3PT, PCT_PTS_2PT_MR, PCT_PTS_FB, PCT_PTS_FT, PCT_PTS_PAINT, PCT_AST_FGM, PCT_UAST_FGM, OPP_FG3_PCT, OPP_EFG_PCT, OPP_FTA_RATE, OPP_TOV_PCT |

### `leagueplayerondetails`

Parameters: `team_id`, `last_n_games`, `measure_type_detailed_defense`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_all_star`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `season_segment_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `PlayersOnCourtLeaguePlayerDetails` | GROUP_SET, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, VS_PLAYER_ID, VS_PLAYER_NAME, COURT_STATUS, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK |

### `teamdashlineups`

Parameters: `team_id`, `group_quantity`, `last_n_games`, `measure_type_detailed_defense`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_all_star`, `date_from_nullable`, `date_to_nullable`, `game_id_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `Lineups` | GROUP_SET, GROUP_ID, GROUP_NAME, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK |
| `Overall` | GROUP_SET, GROUP_VALUE, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK |

### `teamplayeronoffdetails`

Parameters: `team_id`, `last_n_games`, `measure_type_detailed_defense`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_all_star`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `season_segment_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `OverallTeamPlayerOnOffDetails` | GROUP_SET, GROUP_VALUE, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK |
| `PlayersOffCourtTeamPlayerOnOffDetails` | GROUP_SET, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, VS_PLAYER_ID, VS_PLAYER_NAME, COURT_STATUS, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK |
| `PlayersOnCourtTeamPlayerOnOffDetails` | GROUP_SET, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, VS_PLAYER_ID, VS_PLAYER_NAME, COURT_STATUS, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK |

### `teamplayeronoffsummary`

Parameters: `team_id`, `last_n_games`, `measure_type_detailed_defense`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_all_star`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `season_segment_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `OverallTeamPlayerOnOffSummary` | GROUP_SET, GROUP_VALUE, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK |
| `PlayersOffCourtTeamPlayerOnOffSummary` | GROUP_SET, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, VS_PLAYER_ID, VS_PLAYER_NAME, COURT_STATUS, GP, MIN, PLUS_MINUS, OFF_RATING, DEF_RATING, NET_RATING |
| `PlayersOnCourtTeamPlayerOnOffSummary` | GROUP_SET, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, VS_PLAYER_ID, VS_PLAYER_NAME, COURT_STATUS, GP, MIN, PLUS_MINUS, OFF_RATING, DEF_RATING, NET_RATING |


## Matchups and player comparisons

### `leagueseasonmatchups`

Parameters: `league_id`, `per_mode_simple`, `season`, `season_type_playoffs`, `def_player_id_nullable`, `def_team_id_nullable`, `off_player_id_nullable`, `off_team_id_nullable`

| Table | Columns |
|---|---|
| `SeasonMatchups` | SEASON_ID, OFF_PLAYER_ID, OFF_PLAYER_NAME, DEF_PLAYER_ID, DEF_PLAYER_NAME, GP, MATCHUP_MIN, PARTIAL_POSS, PLAYER_PTS, TEAM_PTS, MATCHUP_AST, MATCHUP_TOV, MATCHUP_BLK, MATCHUP_FGM, MATCHUP_FGA, MATCHUP_FG_PCT, MATCHUP_FG3M, MATCHUP_FG3A, MATCHUP_FG3_PCT, HELP_BLK, HELP_FGM, HELP_FGA, HELP_FG_PERC, MATCHUP_FTM, MATCHUP_FTA, SFL |

### `matchupsrollup`

Parameters: `league_id`, `per_mode_simple`, `season`, `season_type_playoffs`, `def_player_id_nullable`, `def_team_id_nullable`, `off_player_id_nullable`, `off_team_id_nullable`

| Table | Columns |
|---|---|
| `MatchupsRollup` | SEASON_ID, POSITION, PERCENT_OF_TIME, DEF_PLAYER_ID, DEF_PLAYER_NAME, GP, MATCHUP_MIN, PARTIAL_POSS, PLAYER_PTS, TEAM_PTS, MATCHUP_AST, MATCHUP_TOV, MATCHUP_BLK, MATCHUP_FGM, MATCHUP_FGA, MATCHUP_FG_PCT, MATCHUP_FG3M, MATCHUP_FG3A, MATCHUP_FG3_PCT, MATCHUP_FTM, MATCHUP_FTA, SFL |

### `playercompare`

Parameters: `vs_player_id_list`, `player_id_list`, `last_n_games`, `measure_type_detailed_defense`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_playoffs`, `conference_nullable`, `date_from_nullable`, `date_to_nullable`, `division_simple_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `Individual` | GROUP_SET, DESCRIPTION, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS |
| `OverallCompare` | GROUP_SET, DESCRIPTION, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS |

### `playervsplayer`

Parameters: `vs_player_id`, `player_id`, `last_n_games`, `measure_type_detailed_defense`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_playoffs`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `season_segment_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `OnOffCourt` | GROUP_SET, PLAYER_ID, PLAYER_NAME, VS_PLAYER_ID, VS_PLAYER_NAME, COURT_STATUS, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, CFID, CFPARAMS |
| `Overall` | GROUP_SET, GROUP_VALUE, PLAYER_ID, PLAYER_NAME, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, CFID, CFPARAMS |
| `PlayerInfo` | PERSON_ID, FIRST_NAME, LAST_NAME, DISPLAY_FIRST_LAST, DISPLAY_LAST_COMMA_FIRST, DISPLAY_FI_LAST, BIRTHDATE, SCHOOL, COUNTRY, LAST_AFFILIATION |
| `ShotAreaOffCourt` | GROUP_SET, PLAYER_ID, PLAYER_NAME, VS_PLAYER_ID, VS_PLAYER_NAME, COURT_STATUS, GROUP_VALUE, FGM, FGA, FG_PCT, CFID, CFPARAMS |
| `ShotAreaOnCourt` | GROUP_SET, PLAYER_ID, PLAYER_NAME, VS_PLAYER_ID, VS_PLAYER_NAME, COURT_STATUS, GROUP_VALUE, FGM, FGA, FG_PCT, CFID, CFPARAMS |
| `ShotAreaOverall` | GROUP_SET, GROUP_VALUE, PLAYER_ID, PLAYER_NAME, FGM, FGA, FG_PCT, CFID, CFPARAMS |
| `ShotDistanceOffCourt` | GROUP_SET, PLAYER_ID, PLAYER_NAME, VS_PLAYER_ID, VS_PLAYER_NAME, COURT_STATUS, GROUP_VALUE, FGM, FGA, FG_PCT, CFID, CFPARAMS |
| `ShotDistanceOnCourt` | GROUP_SET, PLAYER_ID, PLAYER_NAME, VS_PLAYER_ID, VS_PLAYER_NAME, COURT_STATUS, GROUP_VALUE, FGM, FGA, FG_PCT, CFID, CFPARAMS |
| `ShotDistanceOverall` | GROUP_SET, GROUP_VALUE, PLAYER_ID, PLAYER_NAME, FGM, FGA, FG_PCT, CFID, CFPARAMS |
| `VsPlayerInfo` | PERSON_ID, FIRST_NAME, LAST_NAME, DISPLAY_FIRST_LAST, DISPLAY_LAST_COMMA_FIRST, DISPLAY_FI_LAST, BIRTHDATE, SCHOOL, COUNTRY, LAST_AFFILIATION |

### `teamandplayersvsplayers`

Parameters: `vs_team_id`, `vs_player_id5`, `vs_player_id4`, `vs_player_id3`, `vs_player_id2`, `vs_player_id1`, `team_id`, `player_id5`, `player_id4`, `player_id3`, `player_id2`, `player_id1`, `last_n_games`, `measure_type_detailed_defense`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_playoffs`, `conference_nullable`, `date_from_nullable`, `date_to_nullable`, `division_simple_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `PlayersVsPlayers` | GROUP_SET, TITLE_DESCRIPTION, DESCRIPTION, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS |
| `TeamPlayersVsPlayersOff` | GROUP_SET, TITLE_DESCRIPTION, PLAYER_ID, PLAYER_NAME, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS |
| `TeamPlayersVsPlayersOn` | GROUP_SET, TITLE_DESCRIPTION, PLAYER_ID, PLAYER_NAME, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS |
| `TeamVsPlayers` | GROUP_SET, TITLE_DESCRIPTION, DESCRIPTION, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS |
| `TeamVsPlayersOff` | GROUP_SET, TITLE_DESCRIPTION, DESCRIPTION, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS |

### `teamvsplayer`

Parameters: `vs_player_id`, `team_id`, `last_n_games`, `measure_type_detailed_defense`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_playoffs`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `player_id_nullable`, `season_segment_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `OnOffCourt` | GROUP_SET, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, VS_PLAYER_ID, VS_PLAYER_NAME, COURT_STATUS, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, CFID, CFPARAMS |
| `Overall` | GROUP_SET, GROUP_VALUE, TEAM_ID, TEAM_ABBREVIATION, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, CFID, CFPARAMS |
| `ShotAreaOffCourt` | GROUP_SET, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, VS_PLAYER_ID, VS_PLAYER_NAME, COURT_STATUS, GROUP_VALUE, FGM, FGA, FG_PCT, CFID, CFPARAMS |
| `ShotAreaOnCourt` | GROUP_SET, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, VS_PLAYER_ID, VS_PLAYER_NAME, COURT_STATUS, GROUP_VALUE, FGM, FGA, FG_PCT, CFID, CFPARAMS |
| `ShotAreaOverall` | GROUP_SET, GROUP_VALUE, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, FGM, FGA, FG_PCT, CFID, CFPARAMS |
| `ShotDistanceOffCourt` | GROUP_SET, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, VS_PLAYER_ID, VS_PLAYER_NAME, COURT_STATUS, GROUP_VALUE, FGM, FGA, FG_PCT, CFID, CFPARAMS |
| `ShotDistanceOnCourt` | GROUP_SET, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, VS_PLAYER_ID, VS_PLAYER_NAME, COURT_STATUS, GROUP_VALUE, FGM, FGA, FG_PCT, CFID, CFPARAMS |
| `ShotDistanceOverall` | GROUP_SET, GROUP_VALUE, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, FGM, FGA, FG_PCT, CFID, CFPARAMS |
| `vsPlayerOverall` | GROUP_SET, GROUP_VALUE, PLAYER_ID, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |


## Player and team tracking (passing, rebounding, defense, hustle)

### `assisttracker`

Parameters: `college_nullable`, `conference_nullable`, `country_nullable`, `date_from_nullable`, `date_to_nullable`, `division_simple_nullable`, `draft_pick_nullable`, `draft_year_nullable`, `game_scope_simple_nullable`, `height_nullable`, `last_n_games_nullable`, `league_id_nullable`, `location_nullable`, `month_nullable`, `opponent_team_id_nullable`, `outcome_nullable`, `po_round_nullable`, `per_mode_simple_nullable`, `player_experience_nullable`, `player_position_abbreviation_nullable`, `season_nullable`, `season_segment_nullable`, `season_type_all_star_nullable`, `starter_bench_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`, `weight_nullable`

| Table | Columns |
|---|---|
| `AssistTracker` | ASSISTS |

### `defensehub`

Parameters: `game_scope_detailed`, `league_id`, `player_or_team`, `player_scope`, `season`, `season_type_playoffs`

| Table | Columns |
|---|---|
| `DefenseHubStat1` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, DREB |
| `DefenseHubStat10` | (none declared) |
| `DefenseHubStat2` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, STL |
| `DefenseHubStat3` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, BLK |
| `DefenseHubStat4` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, TM_DEF_RATING |
| `DefenseHubStat5` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, OVERALL_PM |
| `DefenseHubStat6` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, THREEP_DFGPCT |
| `DefenseHubStat7` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, TWOP_DFGPCT |
| `DefenseHubStat8` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, FIFETEENF_DFGPCT |
| `DefenseHubStat9` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, DEF_RIM_PCT |

### `leaguedashptdefend`

Parameters: `defense_category`, `league_id`, `per_mode_simple`, `season`, `season_type_all_star`, `college_nullable`, `conference_nullable`, `country_nullable`, `date_from_nullable`, `date_to_nullable`, `division_nullable`, `draft_pick_nullable`, `draft_year_nullable`, `game_segment_nullable`, `height_nullable`, `last_n_games_nullable`, `location_nullable`, `month_nullable`, `opponent_team_id_nullable`, `outcome_nullable`, `po_round_nullable`, `period_nullable`, `player_experience_nullable`, `player_id_nullable`, `player_position_nullable`, `season_segment_nullable`, `starter_bench_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`, `weight_nullable`

| Table | Columns |
|---|---|
| `LeagueDashPTDefend` | CLOSE_DEF_PERSON_ID, PLAYER_NAME, PLAYER_LAST_TEAM_ID, PLAYER_LAST_TEAM_ABBREVIATION, PLAYER_POSITION, AGE, GP, G, FREQ, D_FGM, D_FGA, D_FG_PCT, NORMAL_FG_PCT, PCT_PLUSMINUS |

### `leaguedashptstats`

Parameters: `last_n_games`, `month`, `opponent_team_id`, `per_mode_simple`, `player_or_team`, `pt_measure_type`, `season`, `season_type_all_star`, `college_nullable`, `conference_nullable`, `country_nullable`, `date_from_nullable`, `date_to_nullable`, `division_simple_nullable`, `draft_pick_nullable`, `draft_year_nullable`, `game_scope_simple_nullable`, `height_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `player_experience_nullable`, `player_position_abbreviation_nullable`, `season_segment_nullable`, `starter_bench_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`, `weight_nullable`

| Table | Columns |
|---|---|
| `LeagueDashPtStats` | TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, GP, W, L, MIN, DIST_FEET, DIST_MILES, DIST_MILES_OFF, DIST_MILES_DEF, AVG_SPEED, AVG_SPEED_OFF, AVG_SPEED_DEF |

### `leaguedashptteamdefend`

Parameters: `defense_category`, `league_id`, `per_mode_simple`, `season`, `season_type_all_star`, `conference_nullable`, `date_from_nullable`, `date_to_nullable`, `division_nullable`, `game_segment_nullable`, `last_n_games_nullable`, `location_nullable`, `month_nullable`, `opponent_team_id_nullable`, `outcome_nullable`, `po_round_nullable`, `period_nullable`, `season_segment_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `LeagueDashPtTeamDefend` | TEAM_ID, TEAM_NAME, TEAM_ABBREVIATION, GP, G, FREQ, D_FGM, D_FGA, D_FG_PCT, NORMAL_FG_PCT, PCT_PLUSMINUS |

### `leaguehustlestatsplayer`

Parameters: `per_mode_time`, `season`, `season_type_all_star`, `college_nullable`, `conference_nullable`, `country_nullable`, `date_from_nullable`, `date_to_nullable`, `division_simple_nullable`, `draft_pick_nullable`, `draft_year_nullable`, `height_nullable`, `league_id_nullable`, `location_nullable`, `month_nullable`, `opponent_team_id_nullable`, `outcome_nullable`, `po_round_nullable`, `player_experience_nullable`, `player_position_nullable`, `season_segment_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`, `weight_nullable`

| Table | Columns |
|---|---|
| `HustleStatsPlayer` | PLAYER_ID, PLAYER_NAME, TEAM_ID, TEAM_ABBREVIATION, AGE, G, MIN, CONTESTED_SHOTS, CONTESTED_SHOTS_2PT, CONTESTED_SHOTS_3PT, DEFLECTIONS, CHARGES_DRAWN, SCREEN_ASSISTS, SCREEN_AST_PTS, OFF_LOOSE_BALLS_RECOVERED, DEF_LOOSE_BALLS_RECOVERED, LOOSE_BALLS_RECOVERED, PCT_LOOSE_BALLS_RECOVERED_OFF, PCT_LOOSE_BALLS_RECOVERED_DEF, OFF_BOXOUTS, DEF_BOXOUTS, BOX_OUT_PLAYER_TEAM_REBS, BOX_OUT_PLAYER_REBS, BOX_OUTS, PCT_BOX_OUTS_OFF, PCT_BOX_OUTS_DEF, PCT_BOX_OUTS_TEAM_REB, PCT_BOX_OUTS_REB |

### `leaguehustlestatsteam`

Parameters: `per_mode_time`, `season`, `season_type_all_star`, `college_nullable`, `conference_nullable`, `country_nullable`, `date_from_nullable`, `date_to_nullable`, `division_simple_nullable`, `draft_pick_nullable`, `draft_year_nullable`, `height_nullable`, `league_id_nullable`, `location_nullable`, `month_nullable`, `opponent_team_id_nullable`, `outcome_nullable`, `po_round_nullable`, `player_experience_nullable`, `player_position_nullable`, `season_segment_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`, `weight_nullable`

| Table | Columns |
|---|---|
| `HustleStatsTeam` | TEAM_ID, TEAM_NAME, MIN, CONTESTED_SHOTS, CONTESTED_SHOTS_2PT, CONTESTED_SHOTS_3PT, DEFLECTIONS, CHARGES_DRAWN, SCREEN_ASSISTS, SCREEN_AST_PTS, OFF_LOOSE_BALLS_RECOVERED, DEF_LOOSE_BALLS_RECOVERED, LOOSE_BALLS_RECOVERED, PCT_LOOSE_BALLS_RECOVERED_OFF, PCT_LOOSE_BALLS_RECOVERED_DEF, OFF_BOXOUTS, DEF_BOXOUTS, BOX_OUTS, PCT_BOX_OUTS_OFF, PCT_BOX_OUTS_DEF |

### `playerdashptpass`

Parameters: `team_id`, `player_id`, `last_n_games`, `league_id`, `month`, `opponent_team_id`, `per_mode_simple`, `season`, `season_type_all_star`, `date_from_nullable`, `date_to_nullable`, `location_nullable`, `outcome_nullable`, `season_segment_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `PassesMade` | PLAYER_ID, PLAYER_NAME_LAST_FIRST, TEAM_NAME, TEAM_ID, TEAM_ABBREVIATION, PASS_TYPE, G, PASS_TO, PASS_TEAMMATE_PLAYER_ID, FREQUENCY, PASS, AST, FGM, FGA, FG_PCT, FG2M, FG2A, FG2_PCT, FG3M, FG3A, FG3_PCT |
| `PassesReceived` | PLAYER_ID, PLAYER_NAME_LAST_FIRST, TEAM_NAME, TEAM_ID, TEAM_ABBREVIATION, PASS_TYPE, G, PASS_FROM, PASS_TEAMMATE_PLAYER_ID, FREQUENCY, PASS, AST, FGM, FGA, FG_PCT, FG2M, FG2A, FG2_PCT, FG3M, FG3A, FG3_PCT |

### `playerdashptreb`

Parameters: `team_id`, `player_id`, `last_n_games`, `league_id`, `month`, `opponent_team_id`, `per_mode_simple`, `period`, `season`, `season_type_all_star`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `location_nullable`, `outcome_nullable`, `season_segment_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `NumContestedRebounding` | PLAYER_ID, PLAYER_NAME_LAST_FIRST, SORT_ORDER, G, REB_NUM_CONTESTING_RANGE, REB_FREQUENCY, OREB, DREB, REB, C_OREB, C_DREB, C_REB, C_REB_PCT, UC_OREB, UC_DREB, UC_REB, UC_REB_PCT |
| `OverallRebounding` | PLAYER_ID, PLAYER_NAME_LAST_FIRST, G, OVERALL, REB_FREQUENCY, OREB, DREB, REB, C_OREB, C_DREB, C_REB, C_REB_PCT, UC_OREB, UC_DREB, UC_REB, UC_REB_PCT |
| `RebDistanceRebounding` | PLAYER_ID, PLAYER_NAME_LAST_FIRST, SORT_ORDER, G, REB_DIST_RANGE, REB_FREQUENCY, OREB, DREB, REB, C_OREB, C_DREB, C_REB, C_REB_PCT, UC_OREB, UC_DREB, UC_REB, UC_REB_PCT |
| `ShotDistanceRebounding` | PLAYER_ID, PLAYER_NAME_LAST_FIRST, SORT_ORDER, G, SHOT_DIST_RANGE, REB_FREQUENCY, OREB, DREB, REB, C_OREB, C_DREB, C_REB, C_REB_PCT, UC_OREB, UC_DREB, UC_REB, UC_REB_PCT |
| `ShotTypeRebounding` | PLAYER_ID, PLAYER_NAME_LAST_FIRST, SORT_ORDER, G, SHOT_TYPE_RANGE, REB_FREQUENCY, OREB, DREB, REB, C_OREB, C_DREB, C_REB, C_REB_PCT, UC_OREB, UC_DREB, UC_REB, UC_REB_PCT |

### `playerdashptshotdefend`

Parameters: `team_id`, `player_id`, `last_n_games`, `league_id`, `month`, `opponent_team_id`, `per_mode_simple`, `period`, `season`, `season_type_all_star`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `location_nullable`, `outcome_nullable`, `season_segment_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `DefendingShots` | CLOSE_DEF_PERSON_ID, GP, G, DEFENSE_CATEGORY, FREQ, D_FGM, D_FGA, D_FG_PCT, NORMAL_FG_PCT, PCT_PLUSMINUS |

### `teamdashptpass`

Parameters: `team_id`, `last_n_games`, `league_id`, `month`, `opponent_team_id`, `per_mode_simple`, `season`, `season_type_all_star`, `date_from_nullable`, `date_to_nullable`, `location_nullable`, `outcome_nullable`, `season_segment_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `PassesMade` | TEAM_ID, TEAM_NAME, PASS_TYPE, G, PASS_FROM, PASS_TEAMMATE_PLAYER_ID, FREQUENCY, PASS, AST, FGM, FGA, FG_PCT, FG2M, FG2A, FG2_PCT, FG3M, FG3A, FG3_PCT |
| `PassesReceived` | TEAM_ID, TEAM_NAME, PASS_TYPE, G, PASS_TO, PASS_TEAMMATE_PLAYER_ID, FREQUENCY, PASS, AST, FGM, FGA, FG_PCT, FG2M, FG2A, FG2_PCT, FG3M, FG3A, FG3_PCT |

### `teamdashptreb`

Parameters: `team_id`, `last_n_games`, `league_id`, `month`, `opponent_team_id`, `per_mode_simple`, `period`, `season`, `season_type_all_star`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `location_nullable`, `outcome_nullable`, `season_segment_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `NumContestedRebounding` | TEAM_ID, TEAM_NAME, SORT_ORDER, G, REB_NUM_CONTESTING_RANGE, REB_FREQUENCY, OREB, DREB, REB, C_OREB, C_DREB, C_REB, C_REB_PCT, UC_OREB, UC_DREB, UC_REB, UC_REB_PCT |
| `OverallRebounding` | TEAM_ID, TEAM_NAME, G, OVERALL, REB_FREQUENCY, OREB, DREB, REB, C_OREB, C_DREB, C_REB, C_REB_PCT, UC_OREB, UC_DREB, UC_REB, UC_REB_PCT |
| `RebDistanceRebounding` | TEAM_ID, TEAM_NAME, SORT_ORDER, G, REB_DIST_RANGE, REB_FREQUENCY, OREB, DREB, REB, C_OREB, C_DREB, C_REB, C_REB_PCT, UC_OREB, UC_DREB, UC_REB, UC_REB_PCT |
| `ShotDistanceRebounding` | TEAM_ID, TEAM_NAME, SORT_ORDER, G, SHOT_DIST_RANGE, REB_FREQUENCY, OREB, DREB, REB, C_OREB, C_DREB, C_REB, C_REB_PCT, UC_OREB, UC_DREB, UC_REB, UC_REB_PCT |
| `ShotTypeRebounding` | TEAM_ID, TEAM_NAME, SORT_ORDER, G, SHOT_TYPE_RANGE, REB_FREQUENCY, OREB, DREB, REB, C_OREB, C_DREB, C_REB, C_REB_PCT, UC_OREB, UC_DREB, UC_REB, UC_REB_PCT |


## League-wide player and team stats

### `leaguedashplayerbiostats`

Parameters: `league_id`, `per_mode_simple`, `season`, `season_type_all_star`, `college_nullable`, `conference_nullable`, `country_nullable`, `date_from_nullable`, `date_to_nullable`, `division_simple_nullable`, `draft_pick_nullable`, `draft_year_nullable`, `game_scope_simple_nullable`, `game_segment_nullable`, `height_nullable`, `last_n_games_nullable`, `location_nullable`, `month_nullable`, `opponent_team_id_nullable`, `outcome_nullable`, `po_round_nullable`, `period_nullable`, `player_experience_nullable`, `player_position_abbreviation_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `starter_bench_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`, `weight_nullable`

| Table | Columns |
|---|---|
| `LeagueDashPlayerBioStats` | PLAYER_ID, PLAYER_NAME, TEAM_ID, TEAM_ABBREVIATION, AGE, PLAYER_HEIGHT, PLAYER_HEIGHT_INCHES, PLAYER_WEIGHT, COLLEGE, COUNTRY, DRAFT_YEAR, DRAFT_ROUND, DRAFT_NUMBER, GP, PTS, REB, AST, NET_RATING, OREB_PCT, DREB_PCT, USG_PCT, TS_PCT, AST_PCT |

### `leaguedashplayerclutch`

Parameters: `ahead_behind`, `clutch_time`, `last_n_games`, `measure_type_detailed_defense`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `point_diff`, `rank`, `season`, `season_type_all_star`, `college_nullable`, `conference_nullable`, `country_nullable`, `date_from_nullable`, `date_to_nullable`, `division_simple_nullable`, `draft_pick_nullable`, `draft_year_nullable`, `game_scope_simple_nullable`, `game_segment_nullable`, `height_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `player_experience_nullable`, `player_position_abbreviation_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `starter_bench_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`, `weight_nullable`

| Table | Columns |
|---|---|
| `LeagueDashPlayerClutch` | GROUP_SET, PLAYER_ID, PLAYER_NAME, TEAM_ID, TEAM_ABBREVIATION, AGE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |

### `leaguedashplayerstats`

Parameters: `last_n_games`, `measure_type_detailed_defense`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_all_star`, `college_nullable`, `conference_nullable`, `country_nullable`, `date_from_nullable`, `date_to_nullable`, `division_simple_nullable`, `draft_pick_nullable`, `draft_year_nullable`, `game_scope_simple_nullable`, `game_segment_nullable`, `height_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `player_experience_nullable`, `player_position_abbreviation_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `starter_bench_nullable`, `team_id_nullable`, `two_way_nullable`, `vs_conference_nullable`, `vs_division_nullable`, `weight_nullable`

| Table | Columns |
|---|---|
| `LeagueDashPlayerStats` | PLAYER_ID, PLAYER_NAME, TEAM_ID, TEAM_ABBREVIATION, AGE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |

### `leaguedashteamclutch`

Parameters: `ahead_behind`, `clutch_time`, `last_n_games`, `measure_type_detailed_defense`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `point_diff`, `rank`, `season`, `season_type_all_star`, `conference_nullable`, `date_from_nullable`, `date_to_nullable`, `division_simple_nullable`, `game_scope_simple_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `player_experience_nullable`, `player_position_abbreviation_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `starter_bench_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `LeagueDashTeamClutch` | TEAM_ID, TEAM_NAME, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, CFID, CFPARAMS |

### `leaguedashteamstats`

Parameters: `last_n_games`, `measure_type_detailed_defense`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_all_star`, `conference_nullable`, `date_from_nullable`, `date_to_nullable`, `division_simple_nullable`, `game_scope_simple_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `player_experience_nullable`, `player_position_abbreviation_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `starter_bench_nullable`, `team_id_nullable`, `two_way_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `LeagueDashTeamStats` | TEAM_ID, TEAM_NAME, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, CFID, CFPARAMS |

### `playerestimatedmetrics`

Parameters: `league_id`, `season`, `season_type`

| Table | Columns |
|---|---|
| `PlayerEstimatedMetrics` | PLAYER_ID, PLAYER_NAME, GP, W, L, W_PCT, MIN, E_OFF_RATING, E_DEF_RATING, E_NET_RATING, E_AST_RATIO, E_OREB_PCT, E_DREB_PCT, E_REB_PCT, E_TOV_PCT, E_USG_PCT, E_PACE, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, E_OFF_RATING_RANK, E_DEF_RATING_RANK, E_NET_RATING_RANK, E_AST_RATIO_RANK, E_OREB_PCT_RANK, E_DREB_PCT_RANK, E_REB_PCT_RANK, E_TOV_PCT_RANK, E_USG_PCT_RANK, E_PACE_RANK |

### `synergyplaytypes`

Parameters: `league_id`, `per_mode_simple`, `player_or_team_abbreviation`, `season_type_all_star`, `season`, `play_type_nullable`, `type_grouping_nullable`

| Table | Columns |
|---|---|
| `SynergyPlayType` | SEASON_ID, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, PLAY_TYPE, TYPE_GROUPING, PERCENTILE, GP, POSS_PCT, PPP, FG_PCT, FT_POSS_PCT, TOV_POSS_PCT, SF_POSS_PCT, PLUSONE_POSS_PCT, SCORE_POSS_PCT, EFG_PCT, POSS, PTS, FGM, FGA, FGMX |

### `teamestimatedmetrics`

Parameters: `league_id`, `season`, `season_type`

| Table | Columns |
|---|---|
| `TeamEstimatedMetrics` | TEAM_NAME, TEAM_ID, GP, W, L, W_PCT, MIN, E_OFF_RATING, E_DEF_RATING, E_NET_RATING, E_PACE, E_AST_RATIO, E_OREB_PCT, E_DREB_PCT, E_REB_PCT, E_TM_TOV_PCT, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, E_OFF_RATING_RANK, E_DEF_RATING_RANK, E_NET_RATING_RANK, E_AST_RATIO_RANK, E_OREB_PCT_RANK, E_DREB_PCT_RANK, E_REB_PCT_RANK, E_TM_TOV_PCT_RANK, E_PACE_RANK |


## Player splits, profiles and careers

### `commonallplayers`

Parameters: `is_only_current_season`, `league_id`, `season`

| Table | Columns |
|---|---|
| `CommonAllPlayers` | PERSON_ID, DISPLAY_LAST_COMMA_FIRST, DISPLAY_FIRST_LAST, ROSTERSTATUS, FROM_YEAR, TO_YEAR, PLAYERCODE, PLAYER_SLUG, TEAM_ID, TEAM_CITY, TEAM_NAME, TEAM_ABBREVIATION, TEAM_CODE, TEAM_SLUG, GAMES_PLAYED_FLAG, OTHERLEAGUE_EXPERIENCE_CH |

### `commonplayerinfo`

Parameters: `player_id`, `league_id_nullable`

| Table | Columns |
|---|---|
| `AvailableSeasons` | SEASON_ID |
| `CommonPlayerInfo` | PERSON_ID, FIRST_NAME, LAST_NAME, DISPLAY_FIRST_LAST, DISPLAY_LAST_COMMA_FIRST, DISPLAY_FI_LAST, PLAYER_SLUG, BIRTHDATE, SCHOOL, COUNTRY, LAST_AFFILIATION, HEIGHT, WEIGHT, SEASON_EXP, JERSEY, POSITION, ROSTERSTATUS, TEAM_ID, TEAM_NAME, TEAM_ABBREVIATION, TEAM_CODE, TEAM_CITY, PLAYERCODE, FROM_YEAR, TO_YEAR, DLEAGUE_FLAG, NBA_FLAG, GAMES_PLAYED_FLAG, DRAFT_YEAR, DRAFT_ROUND, DRAFT_NUMBER |
| `PlayerHeadlineStats` | PLAYER_ID, PLAYER_NAME, TimeFrame, PTS, AST, REB, PIE |

### `playerawards`

Parameters: `player_id`

| Table | Columns |
|---|---|
| `PlayerAwards` | PERSON_ID, FIRST_NAME, LAST_NAME, TEAM, DESCRIPTION, ALL_NBA_TEAM_NUMBER, SEASON, MONTH, WEEK, CONFERENCE, TYPE, SUBTYPE1, SUBTYPE2, SUBTYPE3 |

### `playercareerbycollege`

Parameters: `college`, `league_id`, `per_mode_simple`, `season_type_all_star`, `season_nullable`

| Table | Columns |
|---|---|
| `PlayerCareerByCollege` | PLAYER_ID, PLAYER_NAME, COLLEGE, GP, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |

### `playercareerbycollegerollup`

Parameters: `league_id`, `per_mode_simple`, `season_type_all_star`, `season_nullable`

| Table | Columns |
|---|---|
| `East` | REGION, SEED, COLLEGE, PLAYERS, GP, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `Midwest` | REGION, SEED, COLLEGE, PLAYERS, GP, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `South` | REGION, SEED, COLLEGE, PLAYERS, GP, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `West` | REGION, SEED, COLLEGE, PLAYERS, GP, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |

### `playercareerstats`

Parameters: `player_id`, `per_mode36`, `league_id_nullable`

| Table | Columns |
|---|---|
| `CareerTotalsAllStarSeason` | PLAYER_ID, LEAGUE_ID, Team_ID, GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `CareerTotalsCollegeSeason` | PLAYER_ID, LEAGUE_ID, ORGANIZATION_ID, GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `CareerTotalsPostSeason` | PLAYER_ID, LEAGUE_ID, Team_ID, GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `CareerTotalsRegularSeason` | PLAYER_ID, LEAGUE_ID, Team_ID, GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `SeasonRankingsPostSeason` | PLAYER_ID, SEASON_ID, LEAGUE_ID, TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, RANK_MIN, RANK_FGM, RANK_FGA, RANK_FG_PCT, RANK_FG3M, RANK_FG3A, RANK_FG3_PCT, RANK_FTM, RANK_FTA, RANK_FT_PCT, RANK_OREB, RANK_DREB, RANK_REB, RANK_AST, RANK_STL, RANK_BLK, RANK_TOV, RANK_PTS, RANK_EFF |
| `SeasonRankingsRegularSeason` | PLAYER_ID, SEASON_ID, LEAGUE_ID, TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, RANK_MIN, RANK_FGM, RANK_FGA, RANK_FG_PCT, RANK_FG3M, RANK_FG3A, RANK_FG3_PCT, RANK_FTM, RANK_FTA, RANK_FT_PCT, RANK_OREB, RANK_DREB, RANK_REB, RANK_AST, RANK_STL, RANK_BLK, RANK_TOV, RANK_PTS, RANK_EFF |
| `SeasonTotalsAllStarSeason` | PLAYER_ID, SEASON_ID, LEAGUE_ID, TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `SeasonTotalsCollegeSeason` | PLAYER_ID, SEASON_ID, LEAGUE_ID, ORGANIZATION_ID, SCHOOL_NAME, PLAYER_AGE, GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `SeasonTotalsPostSeason` | PLAYER_ID, SEASON_ID, LEAGUE_ID, TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `SeasonTotalsRegularSeason` | PLAYER_ID, SEASON_ID, LEAGUE_ID, TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |

### `playerdashboardbyclutch`

Parameters: `player_id`, `last_n_games`, `measure_type_detailed`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_playoffs`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `Last10Sec3Point2PlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `Last10Sec3PointPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `Last1Min5PointPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `Last1MinPlusMinus5PointPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `Last30Sec3Point2PlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `Last30Sec3PointPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `Last3Min5PointPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `Last3MinPlusMinus5PointPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `Last5Min5PointPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `Last5MinPlusMinus5PointPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `OverallPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |

### `playerdashboardbygamesplits`

Parameters: `player_id`, `last_n_games`, `measure_type_detailed`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_playoffs`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `ByActualMarginPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `ByHalfPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `ByPeriodPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `ByScoreMarginPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `OverallPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |

### `playerdashboardbygeneralsplits`

Parameters: `player_id`, `last_n_games`, `measure_type_detailed`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_playoffs`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `DaysRestPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `LocationPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `MonthPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `OverallPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `PrePostAllStarPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `StartingPosition` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `WinsLossesPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |

### `playerdashboardbylastngames`

Parameters: `player_id`, `last_n_games`, `measure_type_detailed`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_playoffs`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `GameNumberPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `Last10PlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `Last15PlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `Last20PlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `Last5PlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `OverallPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |

### `playerdashboardbyteamperformance`

Parameters: `player_id`, `last_n_games`, `measure_type_detailed`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_playoffs`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `OverallPlayerDashboard` | GROUP_SET, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `PointsScoredPlayerDashboard` | GROUP_SET, GROUP_VALUE_ORDER, GROUP_VALUE, GROUP_VALUE_2, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `PontsAgainstPlayerDashboard` | GROUP_SET, GROUP_VALUE_ORDER, GROUP_VALUE, GROUP_VALUE_2, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `ScoreDifferentialPlayerDashboard` | GROUP_SET, GROUP_VALUE_ORDER, GROUP_VALUE, GROUP_VALUE_2, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |

### `playerdashboardbyyearoveryear`

Parameters: `player_id`, `last_n_games`, `measure_type_detailed`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_playoffs`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `ByYearPlayerDashboard` | GROUP_SET, GROUP_VALUE, TEAM_ID, TEAM_ABBREVIATION, MAX_GAME_DATE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |
| `OverallPlayerDashboard` | GROUP_SET, GROUP_VALUE, TEAM_ID, TEAM_ABBREVIATION, MAX_GAME_DATE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK, CFID, CFPARAMS |

### `playerfantasyprofilebargraph`

Parameters: `player_id`, `season`, `league_id_nullable`, `season_type_all_star_nullable`

| Table | Columns |
|---|---|
| `LastFiveGamesAvg` | PLAYER_ID, PLAYER_NAME, TEAM_ID, TEAM_ABBREVIATION, FAN_DUEL_PTS, NBA_FANTASY_PTS, PTS, REB, AST, FG3M, FT_PCT, STL, BLK, TOV, FG_PCT |
| `SeasonAvg` | PLAYER_ID, PLAYER_NAME, TEAM_ID, TEAM_ABBREVIATION, FAN_DUEL_PTS, NBA_FANTASY_PTS, PTS, REB, AST, FG3M, FT_PCT, STL, BLK, TOV, FG_PCT |

### `playerindex`

Parameters: `active_nullable`, `allstar_nullable`, `college_nullable`, `country_nullable`, `draft_pick_nullable`, `draft_year_nullable`, `height_nullable`, `player_position_abbreviation_nullable`, `historical_nullable`, `league_id`, `season`, `team_id_nullable`, `weight_nullable`

| Table | Columns |
|---|---|
| `PlayerIndex` | PERSON_ID, PLAYER_LAST_NAME, PLAYER_FIRST_NAME, PLAYER_SLUG, TEAM_ID, TEAM_SLUG, IS_DEFUNCT, TEAM_CITY, TEAM_NAME, TEAM_ABBREVIATION, JERSEY_NUMBER, POSITION, HEIGHT, WEIGHT, COLLEGE, COUNTRY, DRAFT_YEAR, DRAFT_ROUND, DRAFT_NUMBER, ROSTER_STATUS, PTS, REB, AST, STATS_TIMEFRAME, FROM_YEAR, TO_YEAR |

### `playernextngames`

Parameters: `player_id`, `number_of_games`, `season_all`, `season_type_all_star`, `league_id_nullable`

| Table | Columns |
|---|---|
| `NextNGames` | GAME_ID, GAME_DATE, HOME_TEAM_ID, VISITOR_TEAM_ID, HOME_TEAM_NAME, VISITOR_TEAM_NAME, HOME_TEAM_ABBREVIATION, VISITOR_TEAM_ABBREVIATION, HOME_TEAM_NICKNAME, VISITOR_TEAM_NICKNAME, GAME_TIME, HOME_WL, VISITOR_WL |

### `playerprofilev2`

Parameters: `player_id`, `per_mode36`, `league_id_nullable`

| Table | Columns |
|---|---|
| `CareerHighs` | PLAYER_ID, GAME_ID, GAME_DATE, VS_TEAM_ID, VS_TEAM_CITY, VS_TEAM_NAME, VS_TEAM_ABBREVIATION, STAT, STAT_VALUE, STAT_ORDER, DATE_EST |
| `CareerTotalsAllStarSeason` | PLAYER_ID, LEAGUE_ID, TEAM_ID, GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `CareerTotalsCollegeSeason` | PLAYER_ID, LEAGUE_ID, ORGANIZATION_ID, GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `CareerTotalsPostSeason` | PLAYER_ID, LEAGUE_ID, TEAM_ID, GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `CareerTotalsPreseason` | PLAYER_ID, LEAGUE_ID, TEAM_ID, GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `CareerTotalsRegularSeason` | PLAYER_ID, LEAGUE_ID, TEAM_ID, GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `NextGame` | GAME_ID, GAME_DATE, GAME_TIME, LOCATION, PLAYER_TEAM_ID, PLAYER_TEAM_CITY, PLAYER_TEAM_NICKNAME, PLAYER_TEAM_ABBREVIATION, VS_TEAM_ID, VS_TEAM_CITY, VS_TEAM_NICKNAME, VS_TEAM_ABBREVIATION |
| `SeasonHighs` | PLAYER_ID, GAME_DATE, VS_TEAM_ID, VS_TEAM_CITY, VS_TEAM_NAME, VS_TEAM_ABBREVIATION, STAT, STATS_VALUE, STAT_ORDER, DATE_EST |
| `SeasonRankingsPostSeason` | PLAYER_ID, SEASON_ID, LEAGUE_ID, TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, RANK_MIN, RANK_FGM, RANK_FGA, RANK_FG_PCT, RANK_FG3M, RANK_FG3A, RANK_FG3_PCT, RANK_FTM, RANK_FTA, RANK_FT_PCT, RANK_OREB, RANK_DREB, RANK_REB, RANK_AST, RANK_STL, RANK_BLK, RANK_TOV, RANK_PTS, RANK_EFF |
| `SeasonRankingsRegularSeason` | PLAYER_ID, SEASON_ID, LEAGUE_ID, TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, RANK_MIN, RANK_FGM, RANK_FGA, RANK_FG_PCT, RANK_FG3M, RANK_FG3A, RANK_FG3_PCT, RANK_FTM, RANK_FTA, RANK_FT_PCT, RANK_OREB, RANK_DREB, RANK_REB, RANK_AST, RANK_STL, RANK_BLK, RANK_TOV, RANK_PTS, RANK_EFF |
| `SeasonTotalsAllStarSeason` | PLAYER_ID, SEASON_ID, LEAGUE_ID, TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `SeasonTotalsCollegeSeason` | PLAYER_ID, SEASON_ID, LEAGUE_ID, ORGANIZATION_ID, SCHOOL_NAME, PLAYER_AGE, GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `SeasonTotalsPostSeason` | PLAYER_ID, SEASON_ID, LEAGUE_ID, TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `SeasonTotalsPreseason` | PLAYER_ID, SEASON_ID, LEAGUE_ID, TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |
| `SeasonTotalsRegularSeason` | PLAYER_ID, SEASON_ID, LEAGUE_ID, TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS |


## Team splits, rosters and history

### `commonteamroster`

Parameters: `team_id`, `season`, `league_id_nullable`

| Table | Columns |
|---|---|
| `Coaches` | TEAM_ID, SEASON, COACH_ID, FIRST_NAME, LAST_NAME, COACH_NAME, IS_ASSISTANT, COACH_TYPE, SORT_SEQUENCE |
| `CommonTeamRoster` | TeamID, SEASON, LeagueID, PLAYER, PLAYER_SLUG, NUM, POSITION, HEIGHT, WEIGHT, BIRTH_DATE, AGE, EXP, SCHOOL, PLAYER_ID |

### `commonteamyears`

Parameters: `league_id`

| Table | Columns |
|---|---|
| `TeamYears` | LEAGUE_ID, TEAM_ID, MIN_YEAR, MAX_YEAR, ABBREVIATION |

### `franchisehistory`

Parameters: `league_id`

| Table | Columns |
|---|---|
| `DefunctTeams` | LEAGUE_ID, TEAM_ID, TEAM_CITY, TEAM_NAME, START_YEAR, END_YEAR, YEARS, GAMES, WINS, LOSSES, WIN_PCT, PO_APPEARANCES, DIV_TITLES, CONF_TITLES, LEAGUE_TITLES |
| `FranchiseHistory` | LEAGUE_ID, TEAM_ID, TEAM_CITY, TEAM_NAME, START_YEAR, END_YEAR, YEARS, GAMES, WINS, LOSSES, WIN_PCT, PO_APPEARANCES, DIV_TITLES, CONF_TITLES, LEAGUE_TITLES |

### `franchiseleaders`

Parameters: `team_id`, `league_id_nullable`

| Table | Columns |
|---|---|
| `FranchiseLeaders` | TEAM_ID, PTS, PTS_PERSON_ID, PTS_PLAYER, AST, AST_PERSON_ID, AST_PLAYER, REB, REB_PERSON_ID, REB_PLAYER, BLK, BLK_PERSON_ID, BLK_PLAYER, STL, STL_PERSON_ID, STL_PLAYER |

### `franchiseplayers`

Parameters: `team_id`, `league_id`, `per_mode_detailed`, `season_type_all_star`

| Table | Columns |
|---|---|
| `FranchisePlayers` | LEAGUE_ID, TEAM_ID, TEAM, PERSON_ID, PLAYER, SEASON_TYPE, ACTIVE_WITH_TEAM, GP, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, PF, STL, TOV, BLK, PTS |

### `teamdashboardbygeneralsplits`

Parameters: `team_id`, `last_n_games`, `measure_type_detailed_defense`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_all_star`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `DaysRestTeamDashboard` | GROUP_SET, GROUP_VALUE, TEAM_DAYS_REST_RANGE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, CFID, CFPARAMS |
| `LocationTeamDashboard` | GROUP_SET, GROUP_VALUE, TEAM_GAME_LOCATION, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, CFID, CFPARAMS |
| `MonthTeamDashboard` | GROUP_SET, GROUP_VALUE, SEASON_MONTH_NAME, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, CFID, CFPARAMS |
| `OverallTeamDashboard` | GROUP_SET, GROUP_VALUE, SEASON_YEAR, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, CFID, CFPARAMS |
| `PrePostAllStarTeamDashboard` | GROUP_SET, GROUP_VALUE, SEASON_SEGMENT, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, CFID, CFPARAMS |
| `WinsLossesTeamDashboard` | GROUP_SET, GROUP_VALUE, GAME_RESULT, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, CFID, CFPARAMS |

### `teamdetails`

Parameters: `team_id`

| Table | Columns |
|---|---|
| `TeamAwardsChampionships` | YEARAWARDED, OPPOSITETEAM |
| `TeamAwardsConf` | YEARAWARDED, OPPOSITETEAM |
| `TeamAwardsDiv` | YEARAWARDED, OPPOSITETEAM |
| `TeamBackground` | TEAM_ID, ABBREVIATION, NICKNAME, YEARFOUNDED, CITY, ARENA, ARENACAPACITY, OWNER, GENERALMANAGER, HEADCOACH, DLEAGUEAFFILIATION |
| `TeamHistory` | TEAM_ID, CITY, NICKNAME, YEARFOUNDED, YEARACTIVETILL |
| `TeamHof` | PLAYERID, PLAYER, POSITION, JERSEY, SEASONSWITHTEAM, YEAR |
| `TeamRetired` | PLAYERID, PLAYER, POSITION, JERSEY, SEASONSWITHTEAM, YEAR |
| `TeamSocialSites` | ACCOUNTTYPE, WEBSITE_LINK |

### `teamhistoricalleaders`

Parameters: `team_id`, `league_id`, `season_id`

| Table | Columns |
|---|---|
| `CareerLeadersByTeam` | TEAM_ID, PTS, PTS_PERSON_ID, PTS_PLAYER, AST, AST_PERSON_ID, AST_PLAYER, REB, REB_PERSON_ID, REB_PLAYER, BLK, BLK_PERSON_ID, BLK_PLAYER, STL, STL_PERSON_ID, STL_PLAYER, SEASON_YEAR |

### `teaminfocommon`

Parameters: `team_id`, `league_id`, `season_nullable`, `season_type_nullable`

| Table | Columns |
|---|---|
| `AvailableSeasons` | SEASON_ID |
| `TeamInfoCommon` | TEAM_ID, SEASON_YEAR, TEAM_CITY, TEAM_NAME, TEAM_ABBREVIATION, TEAM_CONFERENCE, TEAM_DIVISION, TEAM_CODE, W, L, PCT, CONF_RANK, DIV_RANK, MIN_YEAR, MAX_YEAR |
| `TeamSeasonRanks` | LEAGUE_ID, SEASON_ID, TEAM_ID, PTS_RANK, PTS_PG, REB_RANK, REB_PG, AST_RANK, AST_PG, OPP_PTS_RANK, OPP_PTS_PG |

### `teamplayerdashboard`

Parameters: `team_id`, `last_n_games`, `measure_type_detailed_defense`, `month`, `opponent_team_id`, `pace_adjust`, `per_mode_detailed`, `period`, `plus_minus`, `rank`, `season`, `season_type_all_star`, `date_from_nullable`, `date_to_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `po_round_nullable`, `season_segment_nullable`, `shot_clock_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `PlayersSeasonTotals` | GROUP_SET, PLAYER_ID, PLAYER_NAME, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK, NBA_FANTASY_PTS_RANK, DD2_RANK, TD3_RANK |
| `TeamOverall` | GROUP_SET, TEAM_ID, TEAM_NAME, GROUP_VALUE, GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, GP_RANK, W_RANK, L_RANK, W_PCT_RANK, MIN_RANK, FGM_RANK, FGA_RANK, FG_PCT_RANK, FG3M_RANK, FG3A_RANK, FG3_PCT_RANK, FTM_RANK, FTA_RANK, FT_PCT_RANK, OREB_RANK, DREB_RANK, REB_RANK, AST_RANK, TOV_RANK, STL_RANK, BLK_RANK, BLKA_RANK, PF_RANK, PFD_RANK, PTS_RANK, PLUS_MINUS_RANK |

### `teamyearbyyearstats`

Parameters: `team_id`, `league_id`, `per_mode_simple`, `season_type_all_star`

| Table | Columns |
|---|---|
| `TeamStats` | TEAM_ID, TEAM_CITY, TEAM_NAME, YEAR, GP, WINS, LOSSES, WIN_PCT, CONF_RANK, DIV_RANK, PO_WINS, PO_LOSSES, CONF_COUNT, DIV_COUNT, NBA_FINALS_APPEARANCE, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, PF, STL, TOV, BLK, PTS, PTS_RANK |


## Leaders

### `alltimeleadersgrids`

Parameters: `league_id`, `per_mode_simple`, `season_type`, `topx`

| Table | Columns |
|---|---|
| `ASTLeaders` | PLAYER_ID, PLAYER_NAME, AST, AST_RANK |
| `BLKLeaders` | PLAYER_ID, PLAYER_NAME, BLK, BLK_RANK |
| `DREBLeaders` | PLAYER_ID, PLAYER_NAME, DREB, DREB_RANK |
| `FG3ALeaders` | PLAYER_ID, PLAYER_NAME, FG3A, FG3A_RANK |
| `FG3MLeaders` | PLAYER_ID, PLAYER_NAME, FG3M, FG3M_RANK |
| `FG3_PCTLeaders` | PLAYER_ID, PLAYER_NAME, FG3_PCT, FG3_PCT_RANK |
| `FGALeaders` | PLAYER_ID, PLAYER_NAME, FGA, FGA_RANK |
| `FGMLeaders` | PLAYER_ID, PLAYER_NAME, FGM, FGM_RANK |
| `FG_PCTLeaders` | PLAYER_ID, PLAYER_NAME, FG_PCT, FG_PCT_RANK |
| `FTALeaders` | PLAYER_ID, PLAYER_NAME, FTA, FTA_RANK |
| `FTMLeaders` | PLAYER_ID, PLAYER_NAME, FTM, FTM_RANK |
| `FT_PCTLeaders` | PLAYER_ID, PLAYER_NAME, FT_PCT, FT_PCT_RANK |
| `GPLeaders` | PLAYER_ID, PLAYER_NAME, GP, GP_RANK |
| `OREBLeaders` | PLAYER_ID, PLAYER_NAME, OREB, OREB_RANK |
| `PFLeaders` | PLAYER_ID, PLAYER_NAME, PF, PF_RANK |
| `PTSLeaders` | PLAYER_ID, PLAYER_NAME, PTS, PTS_RANK |
| `REBLeaders` | PLAYER_ID, PLAYER_NAME, REB, REB_RANK |
| `STLLeaders` | PLAYER_ID, PLAYER_NAME, STL, STL_RANK |
| `TOVLeaders` | PLAYER_ID, PLAYER_NAME, TOV, TOV_RANK |

### `assistleaders`

Parameters: `league_id`, `per_mode_simple`, `player_or_team`, `season`, `season_type_playoffs`

| Table | Columns |
|---|---|
| `AssistLeaders` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, AST |

### `dunkscoreleaders` *(new)*

Parameters: `league_id_nullable`, `season`, `season_type_all_star`, `player_id_nullable`, `team_id_nullable`, `game_id_nullable`

| Table | Columns |
|---|---|
| `dunks` | gameId, gameDate, matchup, period, gameClockTime, eventNum, playerId, playerName, firstName, lastName, teamId, teamName, teamCity, teamAbbreviation, dunkScore, jumpSubscore, powerSubscore, styleSubscore, defensiveContestSubscore, maxBallHeight, ballSpeedThroughRim, playerVertical, hangTime, takeoffDistance, reverseDunk, dunk360, throughTheLegs, alleyOop, tipIn, selfOop, playerRotation, playerLateralSpeed, ballDistanceTraveled, ballReachBack, totalBallAcceleration, dunkingHand, jumpingFoot, passLength, catchingHand, catchDistance, lateralCatchDistance, passerId, passerName, passerFirstName, passerLastName, passReleasePoint, shooterId, shooterName, shooterFirstName, shooterLastName, shotReleasePoint, shotLength, defensiveContestLevel, possibleAttemptedCharge, videoAvailable |

### `gravityleaders` *(new)*

Parameters: `league_id`, `season`, `season_type_all_star`

| Table | Columns |
|---|---|
| `leaders` | PLAYERID, FIRSTNAME, LASTNAME, TEAMID, TEAMABBREVIATION, TEAMNAME, TEAMCITY, FRAMES, GRAVITYSCORE, AVGGRAVITYSCORE, ONBALLPERIMETERFRAMES, ONBALLPERIMETERGRAVITYSCORE, AVGONBALLPERIMETERGRAVITYSCORE, OFFBALLPERIMETERFRAMES, OFFBALLPERIMETERGRAVITYSCORE, AVGOFFBALLPERIMETERGRAVITYSCORE, ONBALLINTERIORFRAMES, ONBALLINTERIORGRAVITYSCORE, AVGONBALLINTERIORGRAVITYSCORE, OFFBALLINTERIORFRAMES, OFFBALLINTERIORGRAVITYSCORE, AVGOFFBALLINTERIORGRAVITYSCORE, GAMESPLAYED, MINUTES, PTS, REB, AST |

### `homepageleaders`

Parameters: `game_scope_detailed`, `league_id`, `player_or_team`, `player_scope`, `season`, `season_type_playoffs`, `stat_category`

| Table | Columns |
|---|---|
| `HomePageLeaders` | RANK, TEAM_ID, TEAM_NAME, TEAM_ABBREVIATION, PTS, FG_PCT, FG3_PCT, FT_PCT, EFG_PCT, TS_PCT, PTS_PER48 |
| `LeagueAverage` | PTS, FG_PCT, FG3_PCT, FT_PCT, EFG_PCT, TS_PCT, PTS_PER48 |
| `LeagueMax` | PTS, FG_PCT, FG3_PCT, FT_PCT, EFG_PCT, TS_PCT, PTS_PER48 |

### `leaderstiles`

Parameters: `game_scope_detailed`, `league_id`, `player_or_team`, `player_scope`, `season`, `season_type_playoffs`, `stat`

| Table | Columns |
|---|---|
| `AllTimeSeasonHigh` | TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, SEASON_YEAR, PTS |
| `LastSeasonHigh` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, PTS |
| `LeadersTiles` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, PTS |
| `LowSeasonHigh` | TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, SEASON_YEAR, PTS |

### `leagueleaders`

Parameters: `league_id`, `per_mode48`, `scope`, `season`, `season_type_all_star`, `stat_category_abbreviation`, `active_flag_nullable`

| Table | Columns |
|---|---|
| `LeagueLeaders` | PLAYER_ID, RANK, PLAYER, TEAM, GP, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS, EFF, AST_TOV, STL_TOV |


## Standings, schedules and scoreboards

### `commonplayoffseries`

Parameters: `league_id`, `season`, `series_id_nullable`

| Table | Columns |
|---|---|
| `PlayoffSeries` | GAME_ID, HOME_TEAM_ID, VISITOR_TEAM_ID, SERIES_ID, GAME_NUM |

### `iststandings`

Parameters: `league_id`, `season`, `section`

| Table | Columns |
|---|---|
| `Standings` | leagueId, seasonYear, teamId, teamCity, teamName, teamAbbreviation, teamSlug, conference, istGroup, clinchIndicator, clinchedIstKnockout, clinchedIstGroup, clinchedIstWildcard, istWildcardRank, istGroupRank, istKnockoutRank, wins, losses, pct, istGroupGb, istWildcardGb, diff, pts, oppPts, gameId1, opponentTeamAbbreviation1, location1, gameStatus1, gameStatusText1, outcome1, gameId2, opponentTeamAbbreviation2, location2, gameStatus2, gameStatusText2, outcome2, gameId3, opponentTeamAbbreviation3, location3, gameStatus3, gameStatusText3, outcome3, gameId4, opponentTeamAbbreviation4, location4, gameStatus4, gameStatusText4, outcome4 |

### `leaguestandings`

Parameters: `league_id`, `season`, `season_type`, `season_nullable`

| Table | Columns |
|---|---|
| `Standings` | LeagueID, SeasonID, TeamID, TeamCity, TeamName, Conference, ConferenceRecord, PlayoffRank, ClinchIndicator, Division, DivisionRecord, DivisionRank, WINS, LOSSES, WinPCT, LeagueRank, Record, HOME, ROAD, L10, Last10Home, Last10Road, OT, ThreePTSOrLess, TenPTSOrMore, LongHomeStreak, strLongHomeStreak, LongRoadStreak, strLongRoadStreak, LongWinStreak, LongLossStreak, CurrentHomeStreak, strCurrentHomeStreak, CurrentRoadStreak, strCurrentRoadStreak, CurrentStreak, strCurrentStreak, ConferenceGamesBack, DivisionGamesBack, ClinchedConferenceTitle, ClinchedDivisionTitle, ClinchedPlayoffBirth, EliminatedConference, EliminatedDivision, AheadAtHalf, BehindAtHalf, TiedAtHalf, AheadAtThird, BehindAtThird, TiedAtThird, Score100PTS, OppScore100PTS, OppOver500, LeadInFGPCT, LeadInReb, FewerTurnovers, PointsPG, OppPointsPG, DiffPointsPG, vsEast, vsAtlantic, vsCentral, vsSoutheast, vsWest, vsNorthwest, vsPacific, vsSouthwest, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec, PreAS, PostAS |

### `leaguestandingsv3`

Parameters: `league_id`, `season`, `season_type`, `season_nullable`

| Table | Columns |
|---|---|
| `Standings` | LeagueID, SeasonID, TeamID, TeamCity, TeamName, TeamSlug, Conference, ConferenceRecord, PlayoffRank, ClinchIndicator, Division, DivisionRecord, DivisionRank, WINS, LOSSES, WinPCT, LeagueRank, Record, HOME, ROAD, L10, Last10Home, Last10Road, OT, ThreePTSOrLess, TenPTSOrMore, LongHomeStreak, strLongHomeStreak, LongRoadStreak, strLongRoadStreak, LongWinStreak, LongLossStreak, CurrentHomeStreak, strCurrentHomeStreak, CurrentRoadStreak, strCurrentRoadStreak, CurrentStreak, strCurrentStreak, ConferenceGamesBack, DivisionGamesBack, ClinchedConferenceTitle, ClinchedDivisionTitle, ClinchedPlayoffBirth, EliminatedConference, EliminatedDivision, AheadAtHalf, BehindAtHalf, TiedAtHalf, AheadAtThird, BehindAtThird, TiedAtThird, Score100PTS, OppScore100PTS, OppOver500, LeadInFGPCT, LeadInReb, FewerTurnovers, PointsPG, OppPointsPG, DiffPointsPG, vsEast, vsAtlantic, vsCentral, vsSoutheast, vsWest, vsNorthwest, vsPacific, vsSouthwest, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec, ReturnToPlay_East_PI_Flag, ReturnToPlay_West_PI_Flag, ReturnToPlay_Already_Eliminated, Seeding_Game_1_Outcome, Seeding_Game_2_Outcome, Seeding_Game_3_Outcome, Seeding_Game_4_Outcome, Seeding_Game_5_Outcome, Seeding_Game_6_Outcome, Seeding_Game_7_Outcome, Seeding_Game_8_Outcome, Seeding_Game_1_ID, Seeding_Game_2_ID, Seeding_Game_3_ID, Seeding_Game_4_ID, Seeding_Game_5_ID, Seeding_Game_6_ID, Seeding_Game_7_ID, Seeding_Game_8_ID, Seeding_Game_1_Opponent, Seeding_Game_2_Opponent, Seeding_Game_3_Opponent, Seeding_Game_4_Opponent, Seeding_Game_5_Opponent, Seeding_Game_6_Opponent, Seeding_Game_7_Opponent, Seeding_Game_8_Opponent, Seeding_Game_1_Label, Seeding_Game_2_Label, Seeding_Game_3_Label, Seeding_Game_4_Label, Seeding_Game_5_Label, Seeding_Game_6_Label, Seeding_Game_7_Label, Seeding_Game_8_Label |

### `playoffpicture`

Parameters: `league_id`, `season_id`

| Table | Columns |
|---|---|
| `EastConfPlayoffPicture` | CONFERENCE, HIGH_SEED_RANK, HIGH_SEED_TEAM, HIGH_SEED_TEAM_ID, LOW_SEED_RANK, LOW_SEED_TEAM, LOW_SEED_TEAM_ID, HIGH_SEED_SERIES_W, HIGH_SEED_SERIES_L, HIGH_SEED_SERIES_REMAINING_G, HIGH_SEED_SERIES_REMAINING_HOME_G, HIGH_SEED_SERIES_REMAINING_AWAY_G |
| `EastConfRemainingGames` | TEAM, TEAM_ID, REMAINING_G, REMAINING_HOME_G, REMAINING_AWAY_G |
| `EastConfStandings` | CONFERENCE, RANK, TEAM, TEAM_SLUG, TEAM_ID, WINS, LOSSES, PCT, DIV, CONF, HOME, AWAY, GB, GR_OVER_500, GR_OVER_500_HOME, GR_OVER_500_AWAY, GR_UNDER_500, GR_UNDER_500_HOME, GR_UNDER_500_AWAY, RANKING_CRITERIA, CLINCHED_PLAYOFFS, CLINCHED_CONFERENCE, CLINCHED_DIVISION, Clinched_Play_In, ELIMINATED_PLAYOFFS, SOSA_REMAINING, ReturnToPlay_East_PI_Flag, ReturnToPlay_Already_Eliminated, Seeding_Game_1_Outcome, Seeding_Game_2_Outcome, Seeding_Game_3_Outcome, Seeding_Game_4_Outcome, Seeding_Game_5_Outcome, Seeding_Game_6_Outcome, Seeding_Game_7_Outcome, Seeding_Game_8_Outcome, Seeding_Game_1_ID, Seeding_Game_2_ID, Seeding_Game_3_ID, Seeding_Game_4_ID, Seeding_Game_5_ID, Seeding_Game_6_ID, Seeding_Game_7_ID, Seeding_Game_8_ID, Seeding_Game_1_Opponent, Seeding_Game_2_Opponent, Seeding_Game_3_Opponent, Seeding_Game_4_Opponent, Seeding_Game_5_Opponent, Seeding_Game_6_Opponent, Seeding_Game_7_Opponent, Seeding_Game_8_Opponent, Seeding_Game_1_Label, Seeding_Game_2_Label, Seeding_Game_3_Label, Seeding_Game_4_Label, Seeding_Game_5_Label, Seeding_Game_6_Label, Seeding_Game_7_Label, Seeding_Game_8_Label |
| `WestConfPlayoffPicture` | CONFERENCE, HIGH_SEED_RANK, HIGH_SEED_TEAM, HIGH_SEED_TEAM_ID, LOW_SEED_RANK, LOW_SEED_TEAM, LOW_SEED_TEAM_ID, HIGH_SEED_SERIES_W, HIGH_SEED_SERIES_L, HIGH_SEED_SERIES_REMAINING_G, HIGH_SEED_SERIES_REMAINING_HOME_G, HIGH_SEED_SERIES_REMAINING_AWAY_G |
| `WestConfRemainingGames` | TEAM, TEAM_ID, REMAINING_G, REMAINING_HOME_G, REMAINING_AWAY_G |
| `WestConfStandings` | CONFERENCE, RANK, TEAM, TEAM_SLUG, TEAM_ID, WINS, LOSSES, PCT, DIV, CONF, HOME, AWAY, GB, GR_OVER_500, GR_OVER_500_HOME, GR_OVER_500_AWAY, GR_UNDER_500, GR_UNDER_500_HOME, GR_UNDER_500_AWAY, RANKING_CRITERIA, CLINCHED_PLAYOFFS, CLINCHED_CONFERENCE, CLINCHED_DIVISION, Clinched_Play_In, ELIMINATED_PLAYOFFS, SOSA_REMAINING, ReturnToPlay_West_PI_Flag, ReturnToPlay_Already_Eliminated, Seeding_Game_1_Outcome, Seeding_Game_2_Outcome, Seeding_Game_3_Outcome, Seeding_Game_4_Outcome, Seeding_Game_5_Outcome, Seeding_Game_6_Outcome, Seeding_Game_7_Outcome, Seeding_Game_8_Outcome, Seeding_Game_1_ID, Seeding_Game_2_ID, Seeding_Game_3_ID, Seeding_Game_4_ID, Seeding_Game_5_ID, Seeding_Game_6_ID, Seeding_Game_7_ID, Seeding_Game_8_ID, Seeding_Game_1_Opponent, Seeding_Game_2_Opponent, Seeding_Game_3_Opponent, Seeding_Game_4_Opponent, Seeding_Game_5_Opponent, Seeding_Game_6_Opponent, Seeding_Game_7_Opponent, Seeding_Game_8_Opponent, Seeding_Game_1_Label, Seeding_Game_2_Label, Seeding_Game_3_Label, Seeding_Game_4_Label, Seeding_Game_5_Label, Seeding_Game_6_Label, Seeding_Game_7_Label, Seeding_Game_8_Label |

### `scheduleleaguev2` *(new)*

Parameters: `league_id`, `season`

| Table | Columns |
|---|---|
| `SeasonGames` | leagueId, seasonYear, gameDate, gameId, gameCode, gameStatus, gameStatusText, gameSequence, gameDateEst, gameTimeEst, gameDateTimeEst, gameDateUTC, gameTimeUTC, gameDateTimeUTC, awayTeamTime, homeTeamTime, day, monthNum, weekNumber, weekName, ifNecessary, seriesGameNumber, gameLabel, gameSubLabel, seriesText, arenaName, arenaState, arenaCity, postponedStatus, branchLink, gameSubtype, isNeutral, homeTeam_teamId, homeTeam_teamName, homeTeam_teamCity, homeTeam_teamTricode, homeTeam_teamSlug, homeTeam_wins, homeTeam_losses, homeTeam_score, homeTeam_seed, awayTeam_teamId, awayTeam_teamName, awayTeam_teamCity, awayTeam_teamTricode, awayTeam_teamSlug, awayTeam_wins, awayTeam_losses, awayTeam_score, awayTeam_seed, pointsLeaders_personId, pointsLeaders_firstName, pointsLeaders_lastName, pointsLeaders_teamId, pointsLeaders_teamCity, pointsLeaders_teamName, pointsLeaders_teamTricode, pointsLeaders_points, nationalBroadcasters_broadcasterScope, nationalBroadcasters_broadcasterMedia, nationalBroadcasters_broadcasterId, nationalBroadcasters_broadcasterDisplay, nationalBroadcasters_broadcasterAbbreviation, nationalBroadcasters_tapeDelayComments, nationalBroadcasters_broadcasterVideoLink, nationalBroadcasters_broadcasterDescription, nationalBroadcasters_broadcasterTeamId, nationalRadioBroadcasters_broadcasterScope, nationalRadioBroadcasters_broadcasterMedia, nationalRadioBroadcasters_broadcasterId, nationalRadioBroadcasters_broadcasterDisplay, nationalRadioBroadcasters_broadcasterAbbreviation, nationalRadioBroadcasters_tapeDelayComments, nationalRadioBroadcasters_broadcasterVideoLink, nationalRadioBroadcasters_broadcasterDescription, nationalRadioBroadcasters_broadcasterTeamId, nationalOttBroadcasters_broadcasterScope, nationalOttBroadcasters_broadcasterMedia, nationalOttBroadcasters_broadcasterId, nationalOttBroadcasters_broadcasterDisplay, nationalOttBroadcasters_broadcasterAbbreviation, nationalOttBroadcasters_tapeDelayComments, nationalOttBroadcasters_broadcasterVideoLink, nationalOttBroadcasters_broadcasterDescription, nationalOttBroadcasters_broadcasterTeamId, homeTvBroadcasters_broadcasterScope, homeTvBroadcasters_broadcasterMedia, homeTvBroadcasters_broadcasterId, homeTvBroadcasters_broadcasterDisplay, homeTvBroadcasters_broadcasterAbbreviation, homeTvBroadcasters_tapeDelayComments, homeTvBroadcasters_broadcasterVideoLink, homeTvBroadcasters_broadcasterDescription, homeTvBroadcasters_broadcasterTeamId, homeRadioBroadcasters_broadcasterScope, homeRadioBroadcasters_broadcasterMedia, homeRadioBroadcasters_broadcasterId, homeRadioBroadcasters_broadcasterDisplay, homeRadioBroadcasters_broadcasterAbbreviation, homeRadioBroadcasters_tapeDelayComments, homeRadioBroadcasters_broadcasterVideoLink, homeRadioBroadcasters_broadcasterDescription, homeRadioBroadcasters_broadcasterTeamId, homeOttBroadcasters_broadcasterScope, homeOttBroadcasters_broadcasterMedia, homeOttBroadcasters_broadcasterId, homeOttBroadcasters_broadcasterDisplay, homeOttBroadcasters_broadcasterAbbreviation, homeOttBroadcasters_tapeDelayComments, homeOttBroadcasters_broadcasterVideoLink, homeOttBroadcasters_broadcasterDescription, homeOttBroadcasters_broadcasterTeamId, awayTvBroadcasters_broadcasterScope, awayTvBroadcasters_broadcasterMedia, awayTvBroadcasters_broadcasterId, awayTvBroadcasters_broadcasterDisplay, awayTvBroadcasters_broadcasterAbbreviation, awayTvBroadcasters_tapeDelayComments, awayTvBroadcasters_broadcasterVideoLink, awayTvBroadcasters_broadcasterDescription, awayTvBroadcasters_broadcasterTeamId, awayRadioBroadcasters_broadcasterScope, awayRadioBroadcasters_broadcasterMedia, awayRadioBroadcasters_broadcasterId, awayRadioBroadcasters_broadcasterDisplay, awayRadioBroadcasters_broadcasterAbbreviation, awayRadioBroadcasters_tapeDelayComments, awayRadioBroadcasters_broadcasterVideoLink, awayRadioBroadcasters_broadcasterDescription, awayRadioBroadcasters_broadcasterTeamId, awayOttBroadcasters_broadcasterScope, awayOttBroadcasters_broadcasterMedia, awayOttBroadcasters_broadcasterId, awayOttBroadcasters_broadcasterDisplay, awayOttBroadcasters_broadcasterAbbreviation, awayOttBroadcasters_tapeDelayComments, awayOttBroadcasters_broadcasterVideoLink, awayOttBroadcasters_broadcasterDescription, awayOttBroadcasters_broadcasterTeamId |
| `SeasonWeeks` | leagueId, seasonYear, weekNumber, weekName, startDate, endDate |

### `scheduleleaguev2int` *(new)*

Parameters: `league_id`, `season`

| Table | Columns |
|---|---|
| `SeasonGames` | leagueId, seasonYear, gameDate, gameId, gameCode, gameStatus, gameStatusText, gameSequence, gameDateEst, gameTimeEst, gameDateTimeEst, gameDateUTC, gameTimeUTC, gameDateTimeUTC, awayTeamTime, homeTeamTime, day, monthNum, weekNumber, weekName, ifNecessary, seriesGameNumber, gameLabel, gameSubLabel, seriesText, arenaName, arenaState, arenaCity, postponedStatus, branchLink, gameSubtype, isNeutral, homeTeam_teamId, homeTeam_teamName, homeTeam_teamCity, homeTeam_teamTricode, homeTeam_teamSlug, homeTeam_wins, homeTeam_losses, homeTeam_score, homeTeam_seed, awayTeam_teamId, awayTeam_teamName, awayTeam_teamCity, awayTeam_teamTricode, awayTeam_teamSlug, awayTeam_wins, awayTeam_losses, awayTeam_score, awayTeam_seed, pointsLeaders_personId, pointsLeaders_firstName, pointsLeaders_lastName, pointsLeaders_teamId, pointsLeaders_teamCity, pointsLeaders_teamName, pointsLeaders_teamTricode, pointsLeaders_points, nationalBroadcasters_broadcasterScope, nationalBroadcasters_broadcasterMedia, nationalBroadcasters_broadcasterId, nationalBroadcasters_broadcasterDisplay, nationalBroadcasters_broadcasterAbbreviation, nationalBroadcasters_tapeDelayComments, nationalBroadcasters_broadcasterVideoLink, nationalBroadcasters_broadcasterDescription, nationalBroadcasters_broadcasterTeamId, nationalRadioBroadcasters_broadcasterScope, nationalRadioBroadcasters_broadcasterMedia, nationalRadioBroadcasters_broadcasterId, nationalRadioBroadcasters_broadcasterDisplay, nationalRadioBroadcasters_broadcasterAbbreviation, nationalRadioBroadcasters_tapeDelayComments, nationalRadioBroadcasters_broadcasterVideoLink, nationalRadioBroadcasters_broadcasterDescription, nationalRadioBroadcasters_broadcasterTeamId, nationalOttBroadcasters_broadcasterScope, nationalOttBroadcasters_broadcasterMedia, nationalOttBroadcasters_broadcasterId, nationalOttBroadcasters_broadcasterDisplay, nationalOttBroadcasters_broadcasterAbbreviation, nationalOttBroadcasters_tapeDelayComments, nationalOttBroadcasters_broadcasterVideoLink, nationalOttBroadcasters_broadcasterDescription, nationalOttBroadcasters_broadcasterTeamId, homeTvBroadcasters_broadcasterScope, homeTvBroadcasters_broadcasterMedia, homeTvBroadcasters_broadcasterId, homeTvBroadcasters_broadcasterDisplay, homeTvBroadcasters_broadcasterAbbreviation, homeTvBroadcasters_tapeDelayComments, homeTvBroadcasters_broadcasterVideoLink, homeTvBroadcasters_broadcasterDescription, homeTvBroadcasters_broadcasterTeamId, homeRadioBroadcasters_broadcasterScope, homeRadioBroadcasters_broadcasterMedia, homeRadioBroadcasters_broadcasterId, homeRadioBroadcasters_broadcasterDisplay, homeRadioBroadcasters_broadcasterAbbreviation, homeRadioBroadcasters_tapeDelayComments, homeRadioBroadcasters_broadcasterVideoLink, homeRadioBroadcasters_broadcasterDescription, homeRadioBroadcasters_broadcasterTeamId, homeOttBroadcasters_broadcasterScope, homeOttBroadcasters_broadcasterMedia, homeOttBroadcasters_broadcasterId, homeOttBroadcasters_broadcasterDisplay, homeOttBroadcasters_broadcasterAbbreviation, homeOttBroadcasters_tapeDelayComments, homeOttBroadcasters_broadcasterVideoLink, homeOttBroadcasters_broadcasterDescription, homeOttBroadcasters_broadcasterTeamId, awayTvBroadcasters_broadcasterScope, awayTvBroadcasters_broadcasterMedia, awayTvBroadcasters_broadcasterId, awayTvBroadcasters_broadcasterDisplay, awayTvBroadcasters_broadcasterAbbreviation, awayTvBroadcasters_tapeDelayComments, awayTvBroadcasters_broadcasterVideoLink, awayTvBroadcasters_broadcasterDescription, awayTvBroadcasters_broadcasterTeamId, awayRadioBroadcasters_broadcasterScope, awayRadioBroadcasters_broadcasterMedia, awayRadioBroadcasters_broadcasterId, awayRadioBroadcasters_broadcasterDisplay, awayRadioBroadcasters_broadcasterAbbreviation, awayRadioBroadcasters_tapeDelayComments, awayRadioBroadcasters_broadcasterVideoLink, awayRadioBroadcasters_broadcasterDescription, awayRadioBroadcasters_broadcasterTeamId, awayOttBroadcasters_broadcasterScope, awayOttBroadcasters_broadcasterMedia, awayOttBroadcasters_broadcasterId, awayOttBroadcasters_broadcasterDisplay, awayOttBroadcasters_broadcasterAbbreviation, awayOttBroadcasters_tapeDelayComments, awayOttBroadcasters_broadcasterVideoLink, awayOttBroadcasters_broadcasterDescription, awayOttBroadcasters_broadcasterTeamId |
| `SeasonWeeks` | leagueId, seasonYear, weekNumber, weekName, startDate, endDate |
| `BroadcasterList` | leagueId, seasonYear, broadcasterAbbreviation, broadcasterDisplay, broadcasterId, regionId |

### `scoreboardv2`

Parameters: `day_offset`, `game_date`, `league_id`

| Table | Columns |
|---|---|
| `Available` | GAME_ID, PT_AVAILABLE |
| `EastConfStandingsByDay` | TEAM_ID, LEAGUE_ID, SEASON_ID, STANDINGSDATE, CONFERENCE, TEAM, G, W, L, W_PCT, HOME_RECORD, ROAD_RECORD, RETURNTOPLAY |
| `GameHeader` | GAME_DATE_EST, GAME_SEQUENCE, GAME_ID, GAME_STATUS_ID, GAME_STATUS_TEXT, GAMECODE, HOME_TEAM_ID, VISITOR_TEAM_ID, SEASON, LIVE_PERIOD, LIVE_PC_TIME, NATL_TV_BROADCASTER_ABBREVIATION, HOME_TV_BROADCASTER_ABBREVIATION, AWAY_TV_BROADCASTER_ABBREVIATION, LIVE_PERIOD_TIME_BCAST, ARENA_NAME, WH_STATUS |
| `LastMeeting` | GAME_ID, LAST_GAME_ID, LAST_GAME_DATE_EST, LAST_GAME_HOME_TEAM_ID, LAST_GAME_HOME_TEAM_CITY, LAST_GAME_HOME_TEAM_NAME, LAST_GAME_HOME_TEAM_ABBREVIATION, LAST_GAME_HOME_TEAM_POINTS, LAST_GAME_VISITOR_TEAM_ID, LAST_GAME_VISITOR_TEAM_CITY, LAST_GAME_VISITOR_TEAM_NAME, LAST_GAME_VISITOR_TEAM_CITY1, LAST_GAME_VISITOR_TEAM_POINTS |
| `LineScore` | GAME_DATE_EST, GAME_SEQUENCE, GAME_ID, TEAM_ID, TEAM_ABBREVIATION, TEAM_CITY_NAME, TEAM_NAME, TEAM_WINS_LOSSES, PTS_QTR1, PTS_QTR2, PTS_QTR3, PTS_QTR4, PTS_OT1, PTS_OT2, PTS_OT3, PTS_OT4, PTS_OT5, PTS_OT6, PTS_OT7, PTS_OT8, PTS_OT9, PTS_OT10, PTS, FG_PCT, FT_PCT, FG3_PCT, AST, REB, TOV |
| `SeriesStandings` | GAME_ID, HOME_TEAM_ID, VISITOR_TEAM_ID, GAME_DATE_EST, HOME_TEAM_WINS, HOME_TEAM_LOSSES, SERIES_LEADER |
| `TeamLeaders` | GAME_ID, TEAM_ID, TEAM_CITY, TEAM_NICKNAME, TEAM_ABBREVIATION, PTS_PLAYER_ID, PTS_PLAYER_NAME, PTS, REB_PLAYER_ID, REB_PLAYER_NAME, REB, AST_PLAYER_ID, AST_PLAYER_NAME, AST |
| `TicketLinks` | GAME_ID, LEAG_TIX |
| `WestConfStandingsByDay` | TEAM_ID, LEAGUE_ID, SEASON_ID, STANDINGSDATE, CONFERENCE, TEAM, G, W, L, W_PCT, HOME_RECORD, ROAD_RECORD |
| `WinProbability` | (none declared) |

### `scoreboardv3` *(new)*

Parameters: `game_date`, `league_id`

| Table | Columns |
|---|---|
| `ScoreboardInfo` | gameDate, leagueId, leagueName |
| `GameHeader` | gameId, gameCode, gameStatus, gameStatusText, period, gameClock, gameTimeUTC, gameEt, regulationPeriods, seriesGameNumber, gameLabel, gameSubLabel, seriesText, ifNecessary, seriesConference, poRoundDesc, gameSubtype, isNeutral |
| `LineScore` | gameId, teamId, teamCity, teamName, teamTricode, teamSlug, wins, losses, score, seed, inBonus, timeoutsRemaining |
| `GameLeaders` | gameId, teamId, leaderType, personId, name, playerSlug, jerseyNum, position, teamTricode, points, rebounds, assists |
| `TeamLeaders` | gameId, teamId, leaderType, personId, name, playerSlug, jerseyNum, position, teamTricode, points, rebounds, assists, seasonLeadersFlag |
| `Broadcasters` | gameId, broadcasterType, broadcasterId, broadcastDisplay, broadcasterTeamId, broadcasterDescription |


## Draft and combine

### `draftboard`

Parameters: `league_id`, `season_year`, `college_nullable`, `overall_pick_nullable`, `round_num_nullable`, `round_pick_nullable`, `team_id_nullable`, `topx_nullable`

| Table | Columns |
|---|---|
| `DraftBoard` | PERSON_ID, PLAYER_NAME, SEASON, ROUND_NUMBER, ROUND_PICK, OVERALL_PICK, TEAM_ID, TEAM_CITY, TEAM_NAME, TEAM_ABBREVIATION, ORGANIZATION, ORGANIZATION_TYPE, HEIGHT, WEIGHT, POSITION, JERSEY_NUMBER, BIRTHDATE, AGE |

### `draftcombinedrillresults`

Parameters: `league_id`, `season_year`

| Table | Columns |
|---|---|
| `Results` | TEMP_PLAYER_ID, PLAYER_ID, FIRST_NAME, LAST_NAME, PLAYER_NAME, POSITION, STANDING_VERTICAL_LEAP, MAX_VERTICAL_LEAP, LANE_AGILITY_TIME, MODIFIED_LANE_AGILITY_TIME, THREE_QUARTER_SPRINT, BENCH_PRESS |

### `draftcombinenonstationaryshooting`

Parameters: `league_id`, `season_year`

| Table | Columns |
|---|---|
| `Results` | TEMP_PLAYER_ID, PLAYER_ID, FIRST_NAME, LAST_NAME, PLAYER_NAME, POSITION, OFF_DRIB_FIFTEEN_BREAK_LEFT_MADE, OFF_DRIB_FIFTEEN_BREAK_LEFT_ATTEMPT, OFF_DRIB_FIFTEEN_BREAK_LEFT_PCT, OFF_DRIB_FIFTEEN_TOP_KEY_MADE, OFF_DRIB_FIFTEEN_TOP_KEY_ATTEMPT, OFF_DRIB_FIFTEEN_TOP_KEY_PCT, OFF_DRIB_FIFTEEN_BREAK_RIGHT_MADE, OFF_DRIB_FIFTEEN_BREAK_RIGHT_ATTEMPT, OFF_DRIB_FIFTEEN_BREAK_RIGHT_PCT, OFF_DRIB_COLLEGE_BREAK_LEFT_MADE, OFF_DRIB_COLLEGE_BREAK_LEFT_ATTEMPT, OFF_DRIB_COLLEGE_BREAK_LEFT_PCT, OFF_DRIB_COLLEGE_TOP_KEY_MADE, OFF_DRIB_COLLEGE_TOP_KEY_ATTEMPT, OFF_DRIB_COLLEGE_TOP_KEY_PCT, OFF_DRIB_COLLEGE_BREAK_RIGHT_MADE, OFF_DRIB_COLLEGE_BREAK_RIGHT_ATTEMPT, OFF_DRIB_COLLEGE_BREAK_RIGHT_PCT, ON_MOVE_FIFTEEN_MADE, ON_MOVE_FIFTEEN_ATTEMPT, ON_MOVE_FIFTEEN_PCT, ON_MOVE_COLLEGE_MADE, ON_MOVE_COLLEGE_ATTEMPT, ON_MOVE_COLLEGE_PCT |

### `draftcombineplayeranthro`

Parameters: `league_id`, `season_year`

| Table | Columns |
|---|---|
| `Results` | TEMP_PLAYER_ID, PLAYER_ID, FIRST_NAME, LAST_NAME, PLAYER_NAME, POSITION, HEIGHT_WO_SHOES, HEIGHT_WO_SHOES_FT_IN, HEIGHT_W_SHOES, HEIGHT_W_SHOES_FT_IN, WEIGHT, WINGSPAN, WINGSPAN_FT_IN, STANDING_REACH, STANDING_REACH_FT_IN, BODY_FAT_PCT, HAND_LENGTH, HAND_WIDTH |

### `draftcombinespotshooting`

Parameters: `league_id`, `season_year`

| Table | Columns |
|---|---|
| `Results` | TEMP_PLAYER_ID, PLAYER_ID, FIRST_NAME, LAST_NAME, PLAYER_NAME, POSITION, FIFTEEN_CORNER_LEFT_MADE, FIFTEEN_CORNER_LEFT_ATTEMPT, FIFTEEN_CORNER_LEFT_PCT, FIFTEEN_BREAK_LEFT_MADE, FIFTEEN_BREAK_LEFT_ATTEMPT, FIFTEEN_BREAK_LEFT_PCT, FIFTEEN_TOP_KEY_MADE, FIFTEEN_TOP_KEY_ATTEMPT, FIFTEEN_TOP_KEY_PCT, FIFTEEN_BREAK_RIGHT_MADE, FIFTEEN_BREAK_RIGHT_ATTEMPT, FIFTEEN_BREAK_RIGHT_PCT, FIFTEEN_CORNER_RIGHT_MADE, FIFTEEN_CORNER_RIGHT_ATTEMPT, FIFTEEN_CORNER_RIGHT_PCT, COLLEGE_CORNER_LEFT_MADE, COLLEGE_CORNER_LEFT_ATTEMPT, COLLEGE_CORNER_LEFT_PCT, COLLEGE_BREAK_LEFT_MADE, COLLEGE_BREAK_LEFT_ATTEMPT, COLLEGE_BREAK_LEFT_PCT, COLLEGE_TOP_KEY_MADE, COLLEGE_TOP_KEY_ATTEMPT, COLLEGE_TOP_KEY_PCT, COLLEGE_BREAK_RIGHT_MADE, COLLEGE_BREAK_RIGHT_ATTEMPT, COLLEGE_BREAK_RIGHT_PCT, COLLEGE_CORNER_RIGHT_MADE, COLLEGE_CORNER_RIGHT_ATTEMPT, COLLEGE_CORNER_RIGHT_PCT, NBA_CORNER_LEFT_MADE, NBA_CORNER_LEFT_ATTEMPT, NBA_CORNER_LEFT_PCT, NBA_BREAK_LEFT_MADE, NBA_BREAK_LEFT_ATTEMPT, NBA_BREAK_LEFT_PCT, NBA_TOP_KEY_MADE, NBA_TOP_KEY_ATTEMPT, NBA_TOP_KEY_PCT, NBA_BREAK_RIGHT_MADE, NBA_BREAK_RIGHT_ATTEMPT, NBA_BREAK_RIGHT_PCT, NBA_CORNER_RIGHT_MADE, NBA_CORNER_RIGHT_ATTEMPT, NBA_CORNER_RIGHT_PCT |

### `draftcombinestats`

Parameters: `league_id`, `season_all_time`

| Table | Columns |
|---|---|
| `DraftCombineStats` | SEASON, PLAYER_ID, FIRST_NAME, LAST_NAME, PLAYER_NAME, POSITION, HEIGHT_WO_SHOES, HEIGHT_WO_SHOES_FT_IN, HEIGHT_W_SHOES, HEIGHT_W_SHOES_FT_IN, WEIGHT, WINGSPAN, WINGSPAN_FT_IN, STANDING_REACH, STANDING_REACH_FT_IN, BODY_FAT_PCT, HAND_LENGTH, HAND_WIDTH, STANDING_VERTICAL_LEAP, MAX_VERTICAL_LEAP, LANE_AGILITY_TIME, MODIFIED_LANE_AGILITY_TIME, THREE_QUARTER_SPRINT, BENCH_PRESS, SPOT_FIFTEEN_CORNER_LEFT, SPOT_FIFTEEN_BREAK_LEFT, SPOT_FIFTEEN_TOP_KEY, SPOT_FIFTEEN_BREAK_RIGHT, SPOT_FIFTEEN_CORNER_RIGHT, SPOT_COLLEGE_CORNER_LEFT, SPOT_COLLEGE_BREAK_LEFT, SPOT_COLLEGE_TOP_KEY, SPOT_COLLEGE_BREAK_RIGHT, SPOT_COLLEGE_CORNER_RIGHT, SPOT_NBA_CORNER_LEFT, SPOT_NBA_BREAK_LEFT, SPOT_NBA_TOP_KEY, SPOT_NBA_BREAK_RIGHT, SPOT_NBA_CORNER_RIGHT, OFF_DRIB_FIFTEEN_BREAK_LEFT, OFF_DRIB_FIFTEEN_TOP_KEY, OFF_DRIB_FIFTEEN_BREAK_RIGHT, OFF_DRIB_COLLEGE_BREAK_LEFT, OFF_DRIB_COLLEGE_TOP_KEY, OFF_DRIB_COLLEGE_BREAK_RIGHT, ON_MOVE_FIFTEEN, ON_MOVE_COLLEGE |

### `drafthistory`

Parameters: `league_id`, `college_nullable`, `overall_pick_nullable`, `round_num_nullable`, `round_pick_nullable`, `season_year_nullable`, `team_id_nullable`, `topx_nullable`

| Table | Columns |
|---|---|
| `DraftHistory` | PERSON_ID, PLAYER_NAME, SEASON, ROUND_NUMBER, ROUND_PICK, OVERALL_PICK, DRAFT_TYPE, TEAM_ID, TEAM_CITY, TEAM_NAME, TEAM_ABBREVIATION, ORGANIZATION, ORGANIZATION_TYPE |


## Video

### `videodetails`

Parameters: `team_id`, `player_id`, `context_measure_detailed`, `last_n_games`, `month`, `opponent_team_id`, `period`, `season`, `season_type_all_star`, `ahead_behind_nullable`, `clutch_time_nullable`, `context_filter_nullable`, `date_from_nullable`, `date_to_nullable`, `end_period_nullable`, `end_range_nullable`, `game_id_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `point_diff_nullable`, `position_nullable`, `range_type_nullable`, `rookie_year_nullable`, `season_segment_nullable`, `start_period_nullable`, `start_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`

No tables declared; returns video asset URLs as nested JSON.

### `videodetailsasset`

Parameters: `team_id`, `player_id`, `context_measure_detailed`, `last_n_games`, `month`, `opponent_team_id`, `period`, `season`, `season_type_all_star`, `ahead_behind_nullable`, `clutch_time_nullable`, `context_filter_nullable`, `date_from_nullable`, `date_to_nullable`, `end_period_nullable`, `end_range_nullable`, `game_id_nullable`, `game_segment_nullable`, `league_id_nullable`, `location_nullable`, `outcome_nullable`, `point_diff_nullable`, `position_nullable`, `range_type_nullable`, `rookie_year_nullable`, `season_segment_nullable`, `start_period_nullable`, `start_range_nullable`, `vs_conference_nullable`, `vs_division_nullable`

No tables declared; returns video asset URLs as nested JSON.

### `videoevents`

Parameters: `game_id`, `game_event_id`

No tables declared; returns video asset URLs as nested JSON.

### `videoeventsasset`

Parameters: `game_id`, `game_event_id`

No tables declared; returns video asset URLs as nested JSON.

### `videostatus`

Parameters: `game_date`, `league_id`

| Table | Columns |
|---|---|
| `VideoStatus` | GAME_ID, GAME_DATE, VISITOR_TEAM_ID, VISITOR_TEAM_CITY, VISITOR_TEAM_NAME, VISITOR_TEAM_ABBREVIATION, HOME_TEAM_ID, HOME_TEAM_CITY, HOME_TEAM_NAME, HOME_TEAM_ABBREVIATION, GAME_STATUS, GAME_STATUS_TEXT, IS_AVAILABLE, PT_XYZ_AVAILABLE |


## Other

### `fantasywidget`

Parameters: `active_players`, `last_n_games`, `league_id`, `season`, `season_type_all_star`, `todays_opponent`, `todays_players`, `date_from_nullable`, `date_to_nullable`, `location_nullable`, `month_nullable`, `opponent_team_id_nullable`, `po_round_nullable`, `player_id_nullable`, `position_nullable`, `season_segment_nullable`, `team_id_nullable`, `vs_conference_nullable`, `vs_division_nullable`

| Table | Columns |
|---|---|
| `FantasyWidgetResult` | PLAYER_ID, PLAYER_NAME, PLAYER_POSITION, TEAM_ID, TEAM_ABBREVIATION, GP, MIN, FAN_DUEL_PTS, NBA_FANTASY_PTS, PTS, REB, AST, BLK, STL, TOV, FG3M, FGA, FG_PCT, FTA, FT_PCT |

### `homepagev2`

Parameters: `game_scope_detailed`, `league_id`, `player_or_team`, `player_scope`, `season`, `season_type_playoffs`, `stat_type`

| Table | Columns |
|---|---|
| `HomePageStat1` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, PTS |
| `HomePageStat2` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, REB |
| `HomePageStat3` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, AST |
| `HomePageStat4` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, STL |
| `HomePageStat5` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, FG_PCT |
| `HomePageStat6` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, FT_PCT |
| `HomePageStat7` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, FG3_PCT |
| `HomePageStat8` | RANK, TEAM_ID, TEAM_ABBREVIATION, TEAM_NAME, BLK |

### `infographicfanduelplayer`

Parameters: `game_id`

| Table | Columns |
|---|---|
| `FanDuelPlayer` | PLAYER_ID, PLAYER_NAME, TEAM_ID, TEAM_NAME, TEAM_ABBREVIATION, JERSEY_NUM, PLAYER_POSITION, LOCATION, FAN_DUEL_PTS, NBA_FANTASY_PTS, USG_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS |

