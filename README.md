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
- Implement another trading strategy after backtesting it (probably something EMA related since I have that already calculated)
- Implement another way to measure sucesss (MDD, win loss ratio or something similiar)

## DISCLOSURE
I am using AI to help me with this project - I am not using it to think for me though - I am going to query it like a library,
its going to help me use Pandas and numpy since I have not used much at all in the past.
Furthermore using AI is a lot faster than manually searching through documentation allowing me to progress faster and recieve personalised feedback.
For example it helped me better format my readme (which was a large paragraph beforehand - which was a lot more inconvenient and unclear to read)
