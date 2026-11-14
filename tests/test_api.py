from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_feature_request_with_mocked_llm(monkeypatch):
    monkeypatch.setattr("app.main.llm.generate", lambda system, user: "mock analysis")
    r = client.post(
        "/feature-requests",
        json={"title": "Dark mode", "description": "Add a dark theme."},
    )
    assert r.status_code == 200
    assert r.json()["analysis"] == "mock analysis"