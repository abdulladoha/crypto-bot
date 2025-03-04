import pytest
from bot import BinanceTrader
import config

@pytest.fixture
def trader():
    return BinanceTrader(config.API_KEY, config.API_SECRET)

def test_calculate_moving_average(trader):
    sma = trader.calculate_moving_average("BTCUSDT")
    assert sma is not None

def test_check_rsi(trader):
    rsi = trader.check_rsi("BTCUSDT")
    assert rsi is not None