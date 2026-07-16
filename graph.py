import plotly.graph_objects as go

def create_graph(df):
        fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

        buy_signals = df[df['SIGNAL'] == 1]
        sell_signals = df[df['SIGNAL'] == -1]

        fig.add_trace(go.Scatter(
            x=buy_signals['Date'],
            y=buy_signals['Low'],
            mode='markers',
            marker=dict(symbol='triangle-up', size=12, color='green'),
            name='Buy'
        ))

        fig.add_trace(go.Scatter(
            x=sell_signals['Date'],
            y=sell_signals['High'],
            mode='markers',
            marker=dict(symbol='triangle-down', size=12, color='red'),
            name='Sell'
        ))

        fig.show()