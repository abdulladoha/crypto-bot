from binance.client import Client
import logging
import config

# Configure logging
logging.basicConfig(filename='crypto_bot.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:&(message)s')

# Retrieive API key and secret from env variables
api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')

# Initialise Binance client with key and secret
client = Client(api_key, api_secret)

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