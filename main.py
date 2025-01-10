import time
from strategy import simple_strategy

def run_bot():
    symbol = 'BTCUSDT'
    buy_price = 30000    # Example: buy BTC if it goes below $30,000
    quantity = 0.001     # Example: buy 0.001 BTC
    
    while True:
        simple_strategy(symbol, buy_price, quantity)
        time.sleep(60)

if __name__ == "__main__":
    run_bot()
