import pytest
from backend.app.data.crypto_client import CryptoDataClient

def test_crypto_client_tokens_normalization():
    client = CryptoDataClient()
    tokens = client.get_top_tokens(limit=10)
    assert len(tokens) > 0
    first = tokens[0]
    assert "symbol" in first
    assert "price" in first
    assert "marketCap" in first
    assert first["marketCap"] > 0
    assert "upcomingUnlock" in first

def test_crypto_client_buybacks():
    client = CryptoDataClient()
    buybacks = client.get_real_buybacks()
    assert len(buybacks) >= 5
    assert any(b["protocolId"] == "hyperliquid" or b["name"] == "Hyperliquid" for b in buybacks)

def test_crypto_client_market_makers():
    client = CryptoDataClient()
    mms = client.get_real_market_makers()
    assert len(mms) >= 5
    assert any("Wintermute" in m["name"] for m in mms)
