import pandas as pd
import numpy as np
import optuna
from pathlib import Path
from indicators.SMA import sma
from indicators.EMA import ema
from graph import create_graph

class PyTrader:
    def __init__(self, dataset_path, long_sma=133, short_sma=116):
        self.df = pd.read_csv(dataset_path)
        self.df.columns = [col.title() for col in self.df.columns]
        self.df['Date'] = pd.to_datetime(self.df['Date'])

        self.stock_list = []
        self.percent_to_sell = 1

        self.long_sma = long_sma
        self.short_sma = short_sma



    def calculate_indicators(self):
        self.df = sma(df=self.df, long=self.long_sma, short=self.short_sma)
        self.df = ema(df=self.df, span=10) #    To be used later


    def remove_nans(self):
        self.df = self.df.dropna(subset=[f'SMA_{self.short_sma}', f'SMA_{self.long_sma}'], ignore_index=True)

    def generate_signals(self):
        self.df['POS'] = np.where(self.df[f'SMA_{self.short_sma}'] > self.df[f'SMA_{self.long_sma}'], 1, 0)
        self.df['SIGNAL'] = self.df['POS'].diff()
        self.df['SIGNAL'] = self.df['SIGNAL'].fillna(0).astype(int)

        self.df['market_return'] = self.df['Close'].pct_change()
        self.df['strat_returns'] = self.df['POS'].shift(1) * self.df['market_return']
        self.df['cumulative_return'] = (1 + self.df['strat_returns'].fillna(0)).cumprod()
        self.df['cumulative_market'] = (1 + self.df['market_return'].fillna(0)).cumprod()

        print(f'Strategy performance: {self.df['cumulative_return'].iloc[-1]}')
        print(f'Market performance: {self.df['cumulative_market'].iloc[-1]}')

        if not self.df['strat_returns'].std():
            return 0

        mean_return = self.df['strat_returns'].mean()
        std_return = self.df['strat_returns'].std()
        total_years = (self.df['Date'].iloc[-1] - self.df['Date'].iloc[0]).days / 365

        if total_years <= 0:
            return 0
        
        trading_days_per_year = len(self.df) / total_years
        daily_risk_free_rate = 0.04 / trading_days_per_year
        sharpe_ratio = ((mean_return - daily_risk_free_rate) / std_return) * np.sqrt(trading_days_per_year)
        print(f'Sharpe Ratio: {sharpe_ratio}')

        return sharpe_ratio

    

def objective(trial):

        long_sma = trial.suggest_int('long_sma', 50, 200)
        short_sma = trial.suggest_int('short_sma', 5, long_sma - 1)

        dir = Path('datasets')
        sharpes = []

        for dataset in dir.iterdir():
            pytrader = PyTrader(str(dataset), long_sma=long_sma, short_sma=short_sma)
            pytrader.calculate_indicators()
            pytrader.remove_nans()

            if pytrader.df.empty:
                continue

            sharpe_ratio = pytrader.generate_signals()

            if sharpe_ratio is not None:
                sharpes.append(sharpe_ratio)

        if not sharpes:
            return float('-inf')

        return np.mean(sharpes)



if __name__ == '__main__':
     
    # study = optuna.create_study(direction='maximize')
    # study.optimize(objective, n_trials=75)
    # print(f"Best Robust Combined Score: {study.best_value:.4f}")
    # for key, value in study.best_params.items():
    #     print(f"  {key}: {value}")

    pytrader = PyTrader(dataset_path='datasets\\WRK.csv')
    pytrader.calculate_indicators()
    pytrader.remove_nans()
    pytrader.generate_signals()
    #pytrader.df.to_csv('datasets\\testing.csv')
    create_graph(df=pytrader.df)

    
    # print(pytrader.df.head(50))
    # print(pytrader.df.tail(20))