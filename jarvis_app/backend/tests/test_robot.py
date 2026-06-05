import pytest
import pandas as pd
import numpy as np
import sys
import os
from unittest.mock import MagicMock

# Mock MT5
sys.modules['MetaTrader5'] = MagicMock()

from signals import calculate_signals, engineer_features
from regime import RegimeDetector
from brain_models import EnsembleBrain

def test_signals_calculation():
    # Create mock OHLCV data
    data = {
        'open': np.random.rand(100),
        'high': np.random.rand(100),
        'low': np.random.rand(100),
        'close': np.random.rand(100),
        'tick_volume': np.random.rand(100)
    }
    df = pd.DataFrame(data)

    df_signals = calculate_signals(df)
    assert 'rsi' in df_signals.columns
    assert 'adx' in df_signals.columns
    assert 'ema_50' in df_signals.columns

def test_regime_detection():
    data = {
        'close': [100, 101, 102, 103, 104],
        'ema_50': [90, 90, 90, 90, 90],
        'adx': [30, 30, 30, 30, 30],
        'atr': [1, 1, 1, 1, 1]
    }
    df = pd.DataFrame(data)
    regime = RegimeDetector.detect(df)
    assert regime == "BULL_TREND"

def test_brain_prediction():
    brain = EnsembleBrain(model_dir="test_models")
    # Mock data for training
    X = pd.DataFrame(np.random.rand(100, 5), columns=['a', 'b', 'c', 'd', 'e'])
    y = np.random.randint(0, 2, 100)

    brain.train_mock_models(X, y)

    label, confidence = brain.predict(X.tail(1))
    assert label in ["BULLISH", "BEARISH"]
    assert 0.0 <= confidence <= 1.0

    # Cleanup
    import shutil
    if os.path.exists("test_models"):
        shutil.rmtree("test_models")
