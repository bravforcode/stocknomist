"""
FastAPI Routes for Live Crypto, Tokenomics, Protocol Buybacks, and Market Makers.
"""

from typing import Any, Dict, List, Optional
from fastapi import APIRouter, HTTPException, Query
from backend.app.data.crypto_client import CryptoDataClient

router = APIRouter(prefix="/crypto", tags=["Crypto Tokenomics & Market Real Data"])
_crypto_client = CryptoDataClient()


def get_crypto_client() -> CryptoDataClient:
    return _crypto_client


@router.get("/tokens", response_model=List[Dict[str, Any]])
def list_tokens(limit: int = Query(default=50, ge=1, le=250)):
    """Returns top real cryptocurrency tokens with live prices, supplies, and verified unlocks."""
    client = get_crypto_client()
    return client.get_top_tokens(limit=limit)


@router.get("/token/{id_or_symbol}", response_model=Dict[str, Any])
def get_token_detail(id_or_symbol: str):
    """Returns deep-dive token details including allocations, vesting rules, and unlock milestones."""
    client = get_crypto_client()
    token = client.get_real_token(id_or_symbol)
    if not token:
        raise HTTPException(status_code=404, detail=f"Token '{id_or_symbol}' not found in real crypto index")
    return token


@router.get("/emissions", response_model=List[Dict[str, Any]])
def list_emissions():
    """Returns verified token emission rates, circulating supplies, and projected dilution windows."""
    client = get_crypto_client()
    return client.get_real_tokens()


@router.get("/unlocks", response_model=List[Dict[str, Any]])
def list_unlocks():
    """Returns upcoming token unlock events."""
    client = get_crypto_client()
    return client.get_real_unlocks()


@router.get("/buybacks", response_model=List[Dict[str, Any]])
def list_buybacks():
    """Returns verified protocol fees, revenues, and automated buyback/burn metrics."""
    client = get_crypto_client()
    return client.get_real_buybacks()


@router.get("/market-makers", response_model=List[Dict[str, Any]])
def list_market_makers():
    """Returns verified institutional liquidity providers, desks, and tier-1 exchanges."""
    client = get_crypto_client()
    return client.get_real_market_makers()
