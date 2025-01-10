from binance.client import Client

client = Client(api_key, api_secret)

def place_order(symbol, quantity, price, order_type="LIMIT", side="BUY"):
    try:
        order = client.create_limit_buy(
            symbol=symbol,
            quantity=quantity,
            price=price
        )