try:
    import MetaTrader5 as mt5
except ImportError:
    mt5 = None
import pandas as pd
import time
import os

class TradingBridge:
    def __init__(self, account=None, password=None, server=None):
        self.account = account or (int(os.getenv("FBS_ACCOUNT")) if os.getenv("FBS_ACCOUNT") else None)
        self.password = password or os.getenv("FBS_PASSWORD")
        self.server = server or os.getenv("FBS_SERVER")
        self.connected = False

    def connect(self):
        if mt5 is None:
            return "MetaTrader5 library not installed. Please run on Windows."

        if not mt5.initialize():
            return f"MT5 initialize() failed, error code: {mt5.last_error()}"

        if self.account and self.password and self.server:
            authorized = mt5.login(self.account, password=self.password, server=self.server)
            if not authorized:
                return f"Failed to connect to account #{self.account}, error code: {mt5.last_error()}"

        self.connected = True
        return "Connected to MT5"

    def get_market_data(self, symbol, timeframe=None, bars=100):
        if not self.connected:
            return "Not connected to MT5"

        if timeframe is None:
            timeframe = mt5.TIMEFRAME_H1

        rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)
        if rates is None:
            return f"Failed to get rates for {symbol}, error code: {mt5.last_error()}"

        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        return df

    def place_order(self, symbol, order_type, volume, price=None, sl=None, tp=None):
        if not self.connected:
            return "Not connected to MT5"

        # Simplification: in real usage, we'd check symbol_info_tick for current price
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": float(volume),
            "type": order_type,
            "magic": 234000,
            "comment": "JARVIS Autonomous Trade",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }

        if price: request["price"] = price
        if sl: request["sl"] = sl
        if tp: request["tp"] = tp

        result = mt5.order_send(request)
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            return f"Order failed, retcode: {result.retcode}"

        return f"Order placed successfully: {result.order}"

    def shutdown(self):
        if mt5:
            mt5.shutdown()
        self.connected = False
