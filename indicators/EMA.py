import pandas as pd

def ema(df: pd.DataFrame, span):
    df[f'EMA_{span}'] = df['Close'].ewm(span=span, adjust=False).mean()
    return df