from fastapi import FastAPI
import nfl_data_py as nfl
import pandas as pd

app = FastAPI(title="NFL Data API", version="1.0")

@app.get("/")
def root():
    return {"message": "NFL Data API is running!"}

@app.get("/player-stats/{season}")
def get_player_stats(season: int):
    stats = nfl.import_player_stats([season])
    return stats.to_dict(orient="records")

@app.get("/play-by-play/{season}")
def get_play_by_play(season: int):
    pbp = nfl.import_pbp_data([season])
    return pbp.to_dict(orient="records")

@app.get("/teams")
def get_teams():
    teams = nfl.import_team_desc()
    return teams.to_dict(orient="records")

@app.get("/schedule/{season}")
def get_schedule(season: int):
    sched = nfl.import_schedules([season])
    return sched.to_dict(orient="records")
