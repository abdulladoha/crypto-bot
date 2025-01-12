from binance.client import Client
import logging
import config

client = Client(api_key, api_secret)

# Configure logging
logging.basicConfig(filename='crypto_bot.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:&(message)s')


def place_order(symbol, quantity, price, order_type="LIMIT", side="BUY"):
    try:
        # Place a limit buy order
        order = client.create_limit_buy(
            symbol=symbol,
            quantity=quantity,
            price=price
        )
        # Log the order details
        logging.info(f"Order placed: {order}")
        return order
        # Log any errors that occur
    except Exception as e:
        logging.error(f"Error placing order: {e}")
        return None