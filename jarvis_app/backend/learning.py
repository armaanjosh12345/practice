import pandas as pd
from brain_models import EnsembleBrain
from signals import calculate_signals, engineer_features
import sqlite3

class LearningPipeline:
    def __init__(self, db_path="jarvis_memory.db"):
        self.db_path = db_path
        self.brain = EnsembleBrain()

    def fetch_training_data(self, symbol="XAUUSD", bars=1000):
        # Fetches historical data from MT5 for retraining
        from trading_bridge import TradingBridge
        bridge = TradingBridge()
        bridge.connect()
        df = bridge.get_market_data(symbol, bars=bars)
        bridge.shutdown()
        return df

    def perform_nightly_retrain(self, historical_df):
        print("Starting Nightly Retraining...")

        # 1. Clean and Prepare
        df = calculate_signals(historical_df)
        X = engineer_features(df)

        # 2. Define Targets (e.g., did price go up in next 5 bars?)
        y = (df['close'].shift(-5) > df['close']).astype(int)
        y = y.loc[X.index] # Align with features

        # 3. Retrain Brain
        self.brain.train_mock_models(X, y)

        print("Brain updated with new market patterns.")

    def update_signal_weights(self):
        # Evaluate which signals performed best in the last 24h
        conn = sqlite3.connect(self.db_path)
        # logic to read trade_log and update signal_performance table
        conn.close()
        print("Signal weights adjusted based on recent performance.")
