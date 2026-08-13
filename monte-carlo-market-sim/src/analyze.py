"""
Compare real vs. simulated return distributions:
skewness, kurtosis, rolling volatility, autocorrelation of squared returns
(a signature of volatility clustering that GBM does not produce).
"""

import numpy as np
import pandas as pd
from scipy import stats


def distribution_stats(returns: pd.Series | np.ndarray) -> dict:
    """Return basic distribution stats: mean, std, skew, kurtosis."""
    returns = np.asarray(returns).flatten()
    return {
        "mean": returns.mean(),
        "std": returns.std(),
        "skew": stats.skew(returns),
        "kurtosis": stats.kurtosis(returns),  # excess kurtosis; 0 = normal, >0 = fat tails
    }


def rolling_volatility(returns: pd.Series, window: int = 20) -> pd.Series:
    """Rolling standard deviation of returns — used to check for volatility clustering."""
    return returns.rolling(window).std()


def autocorr_squared_returns(returns: pd.Series, lags: int = 20) -> np.ndarray:
    """
    Autocorrelation of squared returns. Real markets show significant positive
    autocorrelation here (volatility clustering); GBM, by construction, does not.
    """
    sq = returns ** 2
    return np.array([sq.autocorr(lag=lag) for lag in range(1, lags + 1)])
