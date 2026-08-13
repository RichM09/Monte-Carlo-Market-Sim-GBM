import numpy as np
from src.simulate import simulate_gbm


def test_output_shape():
    paths = simulate_gbm(S0=100, mu=0.05, sigma=0.2, T=1, steps=252, n_paths=500, seed=1)
    assert paths.shape == (253, 500)


def test_starting_price():
    paths = simulate_gbm(S0=100, mu=0.05, sigma=0.2, T=1, steps=252, n_paths=500, seed=1)
    assert np.allclose(paths[0], 100)


def test_reproducible_with_seed():
    p1 = simulate_gbm(S0=100, mu=0.05, sigma=0.2, T=1, steps=100, n_paths=100, seed=7)
    p2 = simulate_gbm(S0=100, mu=0.05, sigma=0.2, T=1, steps=100, n_paths=100, seed=7)
    assert np.allclose(p1, p2)


def test_zero_volatility_is_deterministic():
    paths = simulate_gbm(S0=100, mu=0.05, sigma=0.0, T=1, steps=100, n_paths=10, seed=1)
    # with sigma=0, all paths should be identical
    assert np.allclose(paths, paths[:, [0]])
