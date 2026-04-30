from fastapi import APIRouter
from typing import List
from app.models import Player
from app.services.team_service import TeamService

router = APIRouter()
team_service = TeamService()

@router.get("/teams/{team_id}/players", response_model=List[Player])
def get_team_players(team_id: int):
    return team_service.get_players_by_team(team_id)