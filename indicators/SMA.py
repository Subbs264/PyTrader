import pandas as pd

def sma(df: pd.DataFrame, long, short):
    df[f'SMA_{short}'] = df['Close'].rolling(window=short).mean()
    df[f'SMA_{long}'] = df['Close'].rolling(window=long).mean()
    return df