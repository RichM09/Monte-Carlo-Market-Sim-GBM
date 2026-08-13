"""
Geometric Brownian Motion price path simulation.

dS_t = mu * S_t * dt + sigma * S_t * dW_t
"""

import numpy as np


def simulate_gbm(S0: float, mu: float, sigma: float, T: float,
                  steps: int, n_paths: int, seed: int | None = None) -> np.ndarray:
    """
    Simulate GBM price paths.

    Parameters
    ----------
    S0 : starting price
    mu : annualized drift (expected return)
    sigma : annualized volatility
    T : time horizon in years
    steps : number of time steps
    n_paths : number of simulated paths
    seed : optional RNG seed for reproducibility

    Returns
    -------
    np.ndarray of shape (steps + 1, n_paths) — simulated price paths
    """
    rng = np.random.default_rng(seed)
    dt = T / steps

    Z = rng.standard_normal((steps, n_paths))
    increments = (mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z

    log_paths = np.cumsum(increments, axis=0)
    log_paths = np.vstack([np.zeros(n_paths), log_paths])

    paths = S0 * np.exp(log_paths)
    return paths


if __name__ == "__main__":
    # quick smoke test
    paths = simulate_gbm(S0=100, mu=0.08, sigma=0.2, T=1, steps=252, n_paths=1000, seed=42)
    print(f"Simulated {paths.shape[1]} paths over {paths.shape[0]} steps")
    print(f"Terminal price mean: {paths[-1].mean():.2f}, std: {paths[-1].std():.2f}")
