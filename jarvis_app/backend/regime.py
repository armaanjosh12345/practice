class RegimeDetector:
    @staticmethod
    def detect(df):
        if len(df) < 5:
            return "UNKNOWN"

        latest = df.iloc[-1]

        # 1. Detect Crisis (High Volatility)
        atr_avg = df['atr'].rolling(20).mean().iloc[-1]
        if latest['atr'] > atr_avg * 2.0:
            return "CRISIS"

        # 2. Detect Trends
        if latest['adx'] > 25:
            if latest['close'] > latest['ema_50']:
                return "BULL_TREND"
            else:
                return "BEAR_TREND"

        # 3. Default to Ranging
        return "RANGING"

def get_strategy_recommendation(regime, ai_signal):
    # This logic maps the AI's prediction to the current market regime
    if regime == "CRISIS":
        return "AVOID" # Too risky

    if regime == "BULL_TREND":
        return "BUY" if ai_signal == "BULLISH" else "WAIT"

    if regime == "BEAR_TREND":
        return "SELL" if ai_signal == "BEARISH" else "WAIT"

    if regime == "RANGING":
        # Mean reversion logic
        if ai_signal == "BULLISH": return "BUY"
        if ai_signal == "BEARISH": return "SELL"

    return "WAIT"
