import time
from data_collector import DataCollector
from trading_bridge import TradingBridge
from signals import calculate_signals, engineer_features
from regime import RegimeDetector, get_strategy_recommendation
from brain_models import EnsembleBrain
from memory import MemoryManager

class AutonomousBot:
    def __init__(self):
        self.data_collector = DataCollector()
        self.trading_bridge = TradingBridge()
        self.brain = EnsembleBrain()
        self.memory = MemoryManager()
        self.is_running = False

    def run_cycle(self):
        print("--- Trading Cycle Started ---")

        # 1. Connect to MT5
        self.trading_bridge.connect()

        # 2. Collect Data
        df = self.trading_bridge.get_market_data("XAUUSD")
        if isinstance(df, str):
            print(df)
            return

        # 3. Calculate Signals
        df = calculate_signals(df)

        # 4. Detect Regime
        regime = RegimeDetector.detect(df)
        print(f"Current Regime: {regime}")

        # 5. AI Brain Prediction
        features = engineer_features(df)
        ai_signal, confidence = self.brain.predict(features.tail(1))
        print(f"AI Prediction: {ai_signal} ({confidence:.2%})")

        # 6. Strategy Recommendation
        recommendation = get_strategy_recommendation(regime, ai_signal)
        print(f"Recommendation: {recommendation}")

        # 7. Execute Trade (if confidence > 72%)
        if recommendation != "WAIT" and recommendation != "AVOID" and confidence > 0.72:
            print(f"Executing {recommendation} on XAUUSD...")

            # Map recommendation string to MT5 order type
            import MetaTrader5 as mt5
            order_type = mt5.ORDER_TYPE_BUY if recommendation == "BUY" else mt5.ORDER_TYPE_SELL

            # Execute actual trade
            exec_result = self.trading_bridge.place_order(
                symbol="XAUUSD",
                order_type=order_type,
                volume=0.01,
                price=df.iloc[-1]['close']
            )
            print(f"Execution Result: {exec_result}")

            self.memory.log_trade("XAUUSD", recommendation, df.iloc[-1]['close'], regime, confidence)

        print("--- Trading Cycle Finished ---")

    def start(self, interval=300):
        self.is_running = True
        while self.is_running:
            try:
                self.run_cycle()
            except Exception as e:
                print(f"Bot Error: {str(e)}")
            time.sleep(interval)

    def stop(self):
        self.is_running = False
        self.trading_bridge.shutdown()

if __name__ == "__main__":
    bot = AutonomousBot()
    bot.start()
