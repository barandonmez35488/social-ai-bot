from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert "AI Social Media Bot" in r.json()["message"]


def test_fetch_trends():
    r = client.get("/fetch-trends")
    assert r.status_code == 200
    assert isinstance(r.json().get("trends"), list)
