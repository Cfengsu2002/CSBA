from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_players_normal_case():
    response = client.get("/teams/1/players")

    assert response.status_code == 200

    players = response.json()
    assert len(players) == 2
    assert players[0]["name"] == "Bob"
    assert players[1]["name"] == "Alice"


def test_get_players_empty_team():
    response = client.get("/teams/3/players")

    assert response.status_code == 200
    assert response.json() == []


def test_team_not_found():
    response = client.get("/teams/999/players")

    assert response.status_code == 404
    assert response.json()["detail"] == "Team not found"