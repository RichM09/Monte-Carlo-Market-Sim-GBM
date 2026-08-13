"""
Estimate GBM parameters (mu, sigma) from real historical price data.
"""

import numpy as np
import pandas as pd


def log_returns(prices: pd.Series) -> pd.Series:
    """Compute daily log returns from a price series."""
    return np.log(prices / prices.shift(1)).dropna()


def estimate_params(prices: pd.Series, trading_days: int = 252) -> tuple[float, float]:
    """
    Estimate annualized drift (mu) and volatility (sigma) from historical prices.

    IMPORTANT: only pass in data up to your simulation start date —
    never estimate parameters using data from the period you're testing against.
    """
    rets = log_returns(prices)
    mu = rets.mean() * trading_days
    sigma = rets.std() * np.sqrt(trading_days)
    return mu, sigma


if __name__ == "__main__":
    # Example (requires yfinance):
    # import yfinance as yf
    # data = yf.download("AAPL", start="2018-01-01", end="2022-12-31")["Adj Close"]
    # mu, sigma = estimate_params(data)
    # print(f"mu={mu:.4f}, sigma={sigma:.4f}")
    pass
