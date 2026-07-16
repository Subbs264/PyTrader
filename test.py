import pandas as pd
from pathlib import Path

def seperate_data():
    df = pd.read_csv('all_stocks_5yr.csv')
    output_dir = Path('datasets')
    output_dir.mkdir(exist_ok=True)

    for name, group in df.groupby('Name'):
        group.to_csv(output_dir / f'{name}.csv', index=False)

if __name__ == '__main__':
    seperate_data()

    