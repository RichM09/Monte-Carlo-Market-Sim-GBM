# Monte Carlo Market Simulator

Simulating stock prices with Geometric Brownian Motion, and testing whether the model actually resembles real market behavior.

## Research Question

Geometric Brownian Motion (GBM) is the standard textbook model for stock price movement. Does it actually resemble how a real stock behaves — or does it miss key features of real markets like fat tails and volatility clustering?

## Data

- Ticker: `[TICKER]` (e.g. AAPL)
- Date range: `[START]` to `[END]`
- Source: Yahoo Finance via `yfinance`
- Daily adjusted close prices, converted to log returns

## Methodology

1. **Simulate**: Generate `N` price paths using GBM:

   dS_t = μ S_t dt + σ S_t dW_t

   discretized as:

   S[t+1] = S[t] · exp((μ − 0.5σ²)Δt + σ√Δt · Z),  Z ~ N(0,1)

2. **Calibrate**: Estimate μ (drift) and σ (volatility) from real historical log returns, annualized.

3. **Compare real vs. simulated** on:
   - Distribution of returns (histogram, skewness, kurtosis)
   - Tail behavior (how often do large moves happen vs. GBM's prediction?)
   - Rolling volatility (does volatility cluster in real data but not in GBM?)
   - Autocorrelation of squared returns (a signature of volatility clustering)

4. **No look-ahead bias**: μ and σ are estimated only from data before the simulation's start date, never from the full sample.

## Results

*(fill in after running — embed your key chart here, e.g. `![terminal price distribution](results/terminal_dist.png)`)*

- Simulated terminal price distribution vs. actual outcome
- Real vs. simulated skewness/kurtosis
- Real vs. simulated rolling volatility plot

## Findings

*(1-2 paragraphs, written after you've actually run it — e.g. does GBM under-predict tail risk? Does it miss volatility clustering? Be specific with numbers.)*

## Limitations

- GBM assumes constant volatility and normally distributed returns — both are known to be unrealistic
- Single-stock analysis; results may not generalize across assets or time periods
- Parameter estimation window affects results (state what window you used)

## Future Work

- Compare GBM against a stochastic-volatility model (e.g. Heston) or GARCH
- Extend to multiple assets and test correlation assumptions
- Feeds into the next project: portfolio optimization using these return/covariance estimates

## Setup

```bash
git clone https://github.com/yourusername/monte-carlo-market-sim.git
cd monte-carlo-market-sim
pip install -r requirements.txt
jupyter notebook notebooks/demo.ipynb
```

## Project Structure

```
monte-carlo-market-sim/
├── README.md
├── requirements.txt
├── data/              # cached historical price data
├── src/
│   ├── simulate.py    # GBM path simulation
│   ├── calibrate.py   # estimate mu/sigma from real data
│   └── analyze.py     # compare real vs simulated distributions
├── notebooks/
│   └── demo.ipynb     # walkthrough notebook using src/
└── tests/
    └── test_simulate.py
```
