import pandas as pd
import numpy as np
import plotly.graph_objects as go

class PyTrader:
    def __init__(self, dataset_path):
        self.df = pd.read_csv(dataset_path)

    def calculate_indicators(self):
        self.df['SMA_20'] = self.df['Close'].rolling(window=20).mean()
        self.df['SMA_50'] = self.df['Close'].rolling(window=50).mean()
        self.df['EMA_10'] = self.df['Close'].ewm(span=10, adjust=False).mean()

    def remove_nans(self):
        self.df = self.df.dropna(subset=['SMA_20', 'SMA_50'])

    def generate_signals(self):
        self.df['POS'] = np.where(self.df['SMA_20'] > self.df['SMA_50'], 1, 0)
        self.df['SIGNAL'] = self.df['POS'].diff()
        self.df['SIGNAL'] = self.df['SIGNAL'].fillna(0).astype(int)

    def create_graph(self):
        fig = go.Figure(data=[go.Candlestick(x=self.df['Date'],
                open=self.df['Open'],
                high=self.df['High'],
                low=self.df['Low'],
                close=self.df['Close'])])

        buy_signals = self.df[self.df['SIGNAL'] == 1]
        sell_signals = self.df[self.df['SIGNAL'] == -1]

        fig.add_trace(go.Scatter(
            x=buy_signals['Date'],
            y=buy_signals['Low'] - 5,
            mode='markers',
            marker=dict(symbol='triangle-up', size=12, color='green'),
            name='Buy'
        ))

        fig.add_trace(go.Scatter(
            x=sell_signals['Date'],
            y=sell_signals['High'] + 5,
            mode='markers',
            marker=dict(symbol='triangle-down', size=12, color='red'),
            name='Sell'
        ))

        fig.show()
        
            


if __name__ == '__main__':
    pytrader = PyTrader(dataset_path='datasets\\TSLA.csv')
    pytrader.calculate_indicators()
    pytrader.remove_nans()
    pytrader.generate_signals()
    pytrader.df.to_csv('datasets\\testing.csv')
    pytrader.create_graph()

    
    print(pytrader.df.head(50))
    print(pytrader.df.tail(20))
    