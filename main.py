import time
from data.market import get_price
from ai.llm import ask_llm
from engine.paper_trader import PaperTrader
from data.indicators import compute_sma, compute_rsi

trader = PaperTrader(initial_balance=10000)
price_history = []

while True:
    try:
        price = get_price()
        price_history.append(price)

        sma_20 = compute_sma(price_history, 20)
        sma_50 = compute_sma(price_history, 50)
        rsi = compute_rsi(price_history, 14)
        
        trend = "UP" if sma_20 > sma_50 else "DOWN"

        prompt = f"""
You are a trading decision engine.
Market price: {price}
RSI: {rsi:.2f}
SMA_20: {sma_20:.2f}
SMA_50: {sma_50:.2f}
Trend: {trend}
Rules:
Return ONLY one word:
BUY
SELL
HOLD
"""

        decision = ask_llm(prompt)

        print("\n-----------------------------")
        print(f"Price: {price}")
        print(f"RSI: {rsi:.2f}, SMA_20: {sma_20:.2f}, SMA_50: {sma_50:.2f}, Trend: {trend}")
        print("AI Decision:", decision)

        trader.execute(decision, price)

        portfolio = trader.portfolio_value(price)
        print("Portfolio Value:", portfolio)

        time.sleep(10)

    except KeyboardInterrupt:
        print("\nBot stopped.")
        break
