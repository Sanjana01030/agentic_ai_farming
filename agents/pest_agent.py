import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml", "pest_model.pkl")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Pest model not found at {MODEL_PATH}")

model = joblib.load(MODEL_PATH)


def predict_pest_risk(temp, humidity):
    prediction = model.predict([[temp, humidity]])
    return prediction[0]