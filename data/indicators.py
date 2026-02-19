import pandas as pd

def compute_sma(prices, period=20):
    if len(prices) < period:
        return sum(prices)/len(prices)
    return pd.Series(prices).rolling(period).mean().iloc[-1]

def compute_rsi(prices, period=14):
    if len(prices) < period + 1:
        return 50  # neutral if not enough data
    df = pd.Series(prices)
    delta = df.diff().dropna()
    gain = delta.where(delta>0, 0)
    loss = -delta.where(delta<0, 0)
    avg_gain = gain.rolling(period).mean().iloc[-1]
    avg_loss = loss.rolling(period).mean().iloc[-1]
    if avg_loss == 0:
        return 100
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi
