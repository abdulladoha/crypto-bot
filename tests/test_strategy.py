import pytest
from bot import BinanceTrader
import config

@pytest.fixture
def trader():
    return BinanceTrader(config.API_KEY, config.API_SECRET)

def test_trading_algorithm(trader):
    result = trader.trading_algorithm("BTCUSDT", 0.1)
    assert result is None  # Assuming the function does not return anything