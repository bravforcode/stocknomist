# Stocknomist — Quantitative Swing Trading Screener

Inspired by Tokenomist.ai, **Stocknomist** is an institutional-grade, 100% self-hosted quantitative equity screener targeting **3% to 10% monthly swing returns** across 1,015 US equities (S&P 500, Nasdaq 100, Russell 1000).

## Core Architecture
- **Frontend**: Vite 6, React 19, Tailwind CSS, TradingView Lightweight Charts (60fps Canvas), Recharts 5-Factor Radar, TanStack Table v8 Virtualized.
- **Backend**: FastAPI, DuckDB analytical columnar store, SQLite WAL fundamental store.
- **Data Pipelines**: Zero-spend public ingestion (Direct Yahoo Finance v8 chart API + chunked yfinance + SEC EDGAR company facts).
- **Security & Sandboxing**: Non-root UID 10001, cgroups v2 resource limits (1 GiB RAM cap, 0.5 CPU cap), Caddy reverse proxy with automated TLS.

## 4 Quantitative Swing Strategies
1. **Momentum Breakout**: 20/50/200 SMA Bullish alignment + volume spike > 1.5x + Bollinger Band squeeze expansion.
2. **Earnings Drift (PEAD)**: Post-Earnings Announcement Drift with revenue acceleration.
3. **Oversold Bounce (Mean Reversion)**: Wilder's RSI(14) < 35 with bullish MACD crossover on strong fundamental equities.
4. **Quality & Free-Cash-Flow Yield**: ROE > 15%, Debt/Equity < 1.0, FCF Yield > 5%.

## Risk Management & Position Sizing
- Wilder's ATR(14) 1.5x dynamic trailing stop-loss.
- Enforced Risk:Reward ratio $R:R \ge 2.0$.
- Dynamic Position Sizing Calculator with customizable portfolio size and risk budget.
