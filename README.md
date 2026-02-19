Simulated trading platform designed to test and evaluate trading strategies using LLM-guided decisions.


This project is a lightweight paper trading engine that combines traditional technical indicators with large language model (LLM) decision support, allowing rapid experimentation with strategy logic without risking real capital. It continuously fetches market data, computes indicators (like SMA & RSI), prompts an LLM for trading decisions, and simulates virtual trades.


-> Features
1. Simulated order execution with virtual capital
2. Built-in technical indicators (SMA, RSI)
3. LLM-powered trade decisions (BUY/SELL/HOLD)
4. Portfolio value tracking in real time
5. Easy to extend with more indicators and strategy logic


-> How It Works
1. The script fetches current market price data periodically.
2. It computes technical indicators like 20-period SMA, 50-period SMA, and 14-period RSI.
3. The current market state is formatted into a prompt and sent to an LLM.
4. Based on the model’s (Qwen 2.5: 7b) output (BUY, SELL, or HOLD), the engine executes a simulated trade.
5. The portfolio value is printed after each decision.


The project currently expects:
Python >= 3.9
Modules in engine/, data/, and ai/ to be implemented
An API key or local LLM access for the ask_llm() interface


-> Example output
-----------------------------
Price: 102.34
RSI: 43.21, SMA_20: 100.15, SMA_50: 98.42, Trend: UP
AI Decision: BUY
Portfolio Value: 10075.20


This project is not just a simulator — it’s a learning platform:
you can experiment with rule-based indicators
you can blend quant strategies with LLM reasoning
you can iterate quickly without risking money
