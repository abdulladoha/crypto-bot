from binance.client import Client
import logging
import config
import time

client = Client(config.API_KEY, config.API_SECRET)

class BinanceTrader:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)

    def place_order(self, symbol, quantity, price, order_type="LIMIT", side="BUY"):
        try:
            if side == "BUY":
                order = self.client.create_limit_buy_order(
                    symbol=symbol,
                    quantity=quantity,
                    price=price
                )
            else:
                order = self.client.create_limit_sell_order(
                    symbol=symbol,
                    quantity=quantity,
                    price=price
                )
            logging.info(f"Order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing order: {e}")
            return None

    def calculate_moving_average(self, symbol, interval='1h', window=20):
        try:
            klines = self.client.get_historical_klines(symbol, interval, f"{window} hours ago UTC")
            closes = [float(kline[4]) for kline in klines]
            sma = sum(closes) / len(closes)
            return sma
        except Exception as e:
            logging.error(f"Error calculating moving average: {e}")
            return None

    def check_rsi(self, symbol, interval='1h', period=14):
        try:
            klines = self.client.get_historical_klines(symbol, interval, f"{period+1} hours ago UTC")
            closes = [float(kline[4]) for kline in klines]
            gains = []
            losses = []

            for i in range(1, len(closes)):
                diff = closes[i] - closes[i-1]
                if diff > 0:
                    gains.append(diff)
                    losses.append(0)
                else:
                    gains.append(0)
                    losses.append(abs(diff))

            avg_gain = sum(gains) / period
            avg_loss = sum(losses) / period

            if avg_loss == 0:
                return 100

            rs = avg_gain / avg_loss
            rsi = 100 - (100 / (1 + rs))
            return rsi
        except Exception as e:
            logging.error(f"Error calculating RSI: {e}")
            return None

    def trading_algorithm(self, symbol="BTCUSDT", quantity=0.1):
        try:
            ticker = self.client.get_symbol_ticker(symbol=symbol)
            current_price = float(ticker['price'])

            sma = self.calculate_moving_average(symbol)
            rsi = self.check_rsi(symbol)

            if sma and rsi:
                if current_price < sma and rsi < 30:
                    order = self.place_order(
                        symbol=symbol,
                        quantity=quantity,
                        price=current_price,
                        side="BUY"
                    )
                    if order:
                        logging.info(f"Buy order placed at {current_price}")

                elif current_price > sma and rsi > 70:
                    order = self.place_order(
                        symbol=symbol,
                        quantity=quantity,
                        price=current_price,
                        side="SELL"
                    )
                    if order:
                        logging.info(f"Sell order placed at {current_price}")

        except Exception as e:
            logging.error(f"Error in trading algorithm: {e}")

def main():
    trader = BinanceTrader(config.API_KEY, config.API_SECRET)
    while True:
        trader.trading_algorithm()
        time.sleep(3600)

if __name__ == "__main__":
    main()