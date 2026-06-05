import pandas as pd
import pandas_ta as ta
import numpy as np

def calculate_signals(df):
    if len(df) < 50:
        return df

    # Trend indicators
    df['ema_20']  = ta.ema(df['close'], length=20)
    df['ema_50']  = ta.ema(df['close'], length=50)
    df['adx']     = ta.adx(df['high'], df['low'], df['close'])['ADX_14']

    # Momentum indicators
    df['rsi']  = ta.rsi(df['close'], length=14)
    df['rsi_slope'] = df['rsi'].diff(3)

    # Volatility indicators
    bb          = ta.bbands(df['close'], length=20)
    # pandas-ta can sometimes return different column names depending on version
    df['bb_upper']  = bb.iloc[:, 2] # BBU is usually the 3rd column
    df['bb_lower']  = bb.iloc[:, 0] # BBL is usually the 1st column
    df['atr']       = ta.atr(df['high'], df['low'], df['close'], length=14)

    return df

def engineer_features(df):
    # This prepares the data for the AI Brain
    features = pd.DataFrame(index=df.index)

    features['rsi'] = df['rsi']
    features['rsi_slope'] = df['rsi_slope']
    features['adx'] = df['adx']
    features['dist_from_ema_50'] = (df['close'] - df['ema_50']) / df['ema_50']
    features['bb_width'] = (df['bb_upper'] - df['bb_lower']) / df['bb_lower']
    features['volatility'] = df['atr'] / df['close']

    # Lag features
    features['prev_rsi'] = df['rsi'].shift(1)
    features['prev_close_change'] = df['close'].pct_change(1)

    return features.dropna()
