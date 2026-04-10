import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200

def test_predict_missing_text(client):
    response = client.post("/predict", json={})
    assert response.status_code == 400

def test_predict_success(client):
    response = client.post("/predict", json={"text": "I love this!"})
    assert response.status_code == 200