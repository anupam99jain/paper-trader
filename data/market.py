import requests

def get_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    r = requests.get(url)
    data = r.json()
    return float(data["price"])
