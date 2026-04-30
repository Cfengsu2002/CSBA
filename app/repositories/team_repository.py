from datetime import datetime
from app.models import Team, Player


class TeamRepository:
    def __init__(self):
        self.teams = [
            Team(id=1, name="Lakers"),
            Team(id=2, name="Warriors"),
            Team(id=3, name="Empty Team"),
        ]

        # joinedAt 降序：同队中较新的在前（与 test_team_players 一致）
        self.players = [
            Player(id=1, name="Alice", teamId=1, joinedAt=datetime(2024, 1, 10, 10, 0)),
            Player(id=2, name="Bob", teamId=1, joinedAt=datetime(2024, 3, 5, 12, 0)),
            Player(id=3, name="Alex", teamId=2, joinedAt=datetime(2024, 2, 1, 9, 0)),
        ]

    def get_team_by_id(self, team_id: int):
        return next((team for team in self.teams if team.id == team_id), None)

    def get_players_by_team_id(self, team_id: int):
        return [player for player in self.players if player.teamId == team_id]