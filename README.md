# PyTrader

A stock trading signal bot using moving average crossover strategies. Part of my EPQ college project.

## Strategy

**Moving Average Crossover** — buys when the 20-day SMA crosses above the 50-day SMA, sells when it crosses below.

### Indicators

- SMA (20, 50)
- EMA (10)

## Libraries

- **pandas** / **numpy** - data analysis
- **plotly** - candlestick charts with buy/sell markers

## Usage

```bash
pip install pandas numpy plotly
python main.py
```

This loads Tesla (TSLA) historical data from `datasets/TSLA.csv`, calculates indicators, generates signals, displays an interactive chart, and saves the enriched data to `datasets/testing.csv`.

## Status

Working signal generator. Next steps:
- Turn it into a full backtesting engine (P&L tracking, equity curve, Sharpe ratio, max drawdown)
- Parameter optimization script
- Multi-ticker support
- Risk management (stop-loss, position sizing)


## DISCLOSURE
I am using AI to help me with this project - I am not using it to think for me though - I am going to query it like a library,
its going to help me use Pandas and numpy since I have not used much at all in the past.
Furthermore using AI is a lot faster than manually searching through documentation allowing me to progress faster and recieve personalised feedback.
