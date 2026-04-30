from pydantic import BaseModel
from datetime import datetime

class Team(BaseModel):
    id: int
    name: str

class Player(BaseModel):
    id: int
    name: str
    teamId: int
    joinedAt: datetime