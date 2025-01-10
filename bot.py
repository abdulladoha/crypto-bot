from binance.client import Client
import logging
import config

client = Client(api_key, api_secret)

def place_order(symbol, quantity, price, order_type="LIMIT", side="BUY"):
    try:
        order = client.create_limit_buy(
            symbol=symbol,
            quantity=quantity,
            price=price
        )
        logging.info(f"Order placed: {order}")
        return order
    except Exception as e:
        logging.error(f"Error placing order: {e}")
        return None