from fastapi import HTTPException
from app.repositories.team_repository import TeamRepository


class TeamService:
    def __init__(self):
        self.repository = TeamRepository()

    def get_players_by_team(self, team_id: int):
        team = self.repository.get_team_by_id(team_id)
        if not team:
            raise HTTPException(status_code=404, detail="Team not found")
        players = self.repository.get_players_by_team_id(team_id)
        return sorted(players, key=lambda player: player.joinedAt, reverse=True)