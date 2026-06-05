# QUANTUM SANDBOX: MASTER BUILD GUIDE

## 1. Project Philosophy
This is not a "bot"; it is a living system. It prioritizes **Intelligence Speed** (minutes ahead of humans) over **Execution Speed** (microseconds). It uses the **7-Layer Architecture** to ensure it can survive any market regime.

---

## 2. The 7-Layer Architecture

### Layer 1: Data Infrastructure
- **MT5 (MetaTrader5)**: Primary source for OHLCV (Price) and Tick data.
- **NewsAPI**: Real-time news headlines for sentiment analysis.
- **FRED API**: Macro data (Interest rates, CPI, GDP) to understand the "Big Picture."
- **Reddit/Social**: Sentiment data to detect retail crowd behavior.

### Layer 2: Signal Generation
- **Technical**: RSI Slope, MACD Acceleration, Bollinger Compression.
- **Narrative**: FinBERT scoring of news and earnings calls.
- **Institutional**: Dark Pool prints and Options flow (where available).

### Layer 3: The Brain (ML Core)
- **Regime Detection**: Classified as Bull, Bear, Ranging, or Crisis.
- **Ensemble Voting**: Random Forest, XGBoost, and LSTM must vote. Only trade when confidence > 72%.
- **Daily Retraining**: The bot must retrain every night on new data to avoid "Alpha Decay."

### Layer 4: Risk Management
- **Kelly Criterion**: Dynamic position sizing based on signal confidence.
- **Correlation Control**: Don't open 3 trades that all depend on the Dollar falling.
- **Circuit Breaker**: Auto-shutdown if daily drawdown exceeds 3%.

### Layer 5: Execution Engine
- **MT5 Bridge**: Direct Python-to-MT5 terminal connection.
- **Smart Routing**: Use IOC (Immediate or Cancel) orders to prevent slippage.

### Layer 6: Monitoring & Memory
- **SQLite Database**: 5 key tables (Trades, Signal Performance, Regime History, Model Stats, Market Events).
- **Learning Loop**: The bot reads its history before every trade to avoid repeating past mistakes.

### Layer 7: Meta-Learning
- **Analogy Reasoning**: Finding historical "Black Swans" that mirror current patterns.
- **Adversarial Simulation**: Predicting what other bots will do and avoiding "Exit Liquidity."

---

## 3. Implementation Blueprint (Where things go)

### Backend (Python)
- `main.py`: The FastAPI server & system coordinator.
- `brain.py`: The AI logic, ML model loading, and ensemble voting.
- `data_collector.py`: API handlers for FRED, News, and MT5 data.
- `trading_bridge.py`: The MetaTrader5 execution logic.
- `memory.py`: The SQLite database managers and "Learning" functions.
- `system_info.py`: Hardware monitoring (CPU/RAM/Battery).

### Frontend (React/Electron)
- `App.tsx`: The root navigator.
- `CommandCenter.tsx`: The primary dashboard with charts and live signals.
- `MemoryView.tsx`: Visualization of the bot's learning history.
- `SystemStatus.tsx`: Real-time hardware and "Jarvis" status.

---

## 4. Setup Instructions for Precision 5550
1. **Environment**: Use Python 3.12 with CUDA 11.8 for GPU acceleration on the Quadro T2000.
2. **MT5**: Must be running the FBS-branded terminal on Windows.
3. **VPS**: For 24/7 integration, deploy to a Windows VPS near the FBS servers to minimize latency.
4. **Ollama**: Run `ollama run llama3` locally for the conversational "Jarvis" brain.

---

## 5. Critical Truths
- **No Overfitting**: Always use Walk-Forward testing.
- **No Emotions**: The Risk Gate is the final authority, not the AI signal.
- **Continuous Growth**: If the bot doesn't update its database daily, it will die.
