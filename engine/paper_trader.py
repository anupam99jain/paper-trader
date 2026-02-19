import time
class PaperTrader:
    def __init__(self, initial_balance=10000):
        self.balance = initial_balance
        self.position = 0
        self.entry_price = 0
        self.trade_log = []

    def execute(self, decision, price):
        decision = decision.strip().upper()
        if decision == "BUY" and self.balance > 0 and self.position == 0:
            self.position = self.balance / price
            self.entry_price = price
            self.balance = 0
            self.trade_log.append(("BUY", price))
            print(f"[BUY] Bought at {price}")
            with open("logs/trades.txt", "a") as f:
                f.write(f"BUY,{price},{self.balance},{self.position}\n")
        elif decision == "SELL" and self.position > 0:
            self.balance = self.position * price
            profit = self.balance - (self.position * self.entry_price)
            self.position = 0
            self.trade_log.append(("SELL", price))
            print(f"[SELL] Sold at {price} | PnL: {profit:.2f}")
            with open("logs/trades.txt", "a") as f:
                f.write(f"SELL,{price},{self.balance},{self.position}\n")
        else:
            print("[HOLD / INVALID] No action")

    def portfolio_value(self, current_price):
        return self.balance + self.position * current_price
