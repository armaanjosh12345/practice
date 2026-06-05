import numpy as np
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import joblib
import os

class EnsembleBrain:
    def __init__(self, model_dir="models"):
        self.model_dir = model_dir
        self.rf = None
        self.xgb = None
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)

    def train_mock_models(self, X, y):
        # This is a fallback to allow the bot to run if no real models exist
        self.rf = RandomForestClassifier(n_estimators=100)
        self.rf.fit(X, y)
        self.xgb = XGBClassifier()
        self.xgb.fit(X, y)
        self.save_models()

    def save_models(self):
        joblib.dump(self.rf, os.path.join(self.model_dir, "rf_model.pkl"))
        joblib.dump(self.xgb, os.path.join(self.model_dir, "xgb_model.pkl"))

    def load_models(self):
        try:
            self.rf = joblib.load(os.path.join(self.model_dir, "rf_model.pkl"))
            self.xgb = joblib.load(os.path.join(self.model_dir, "xgb_model.pkl"))
            return True
        except:
            return False

    def predict(self, features):
        if self.rf is None or self.xgb is None:
            if not self.load_models():
                return "NEUTRAL", 0.0

        # Ensemble voting
        rf_proba = self.rf.predict_proba(features)[0]
        xgb_proba = self.xgb.predict_proba(features)[0]

        avg_proba = (rf_proba + xgb_proba) / 2
        confidence = np.max(avg_proba)
        prediction = np.argmax(avg_proba) # 0 = Bearish, 1 = Bullish

        label = "BULLISH" if prediction == 1 else "BEARISH"
        return label, confidence
