from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_get_crypto_tokens():
    res = client.get("/api/crypto/tokens")
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, list)
    assert len(data) >= 10
    assert any(t["symbol"] == "BTC" or t["symbol"] == "ARB" for t in data)

def test_get_crypto_token_detail():
    res = client.get("/api/crypto/token/arbitrum")
    assert res.status_code == 200
    data = res.json()
    assert data["symbol"] == "ARB"
    assert "allocations" in data

def test_get_crypto_buybacks():
    res = client.get("/api/crypto/buybacks")
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, list)
    assert len(data) >= 5

def test_get_crypto_market_makers():
    res = client.get("/api/crypto/market-makers")
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, list)
    assert len(data) >= 5
