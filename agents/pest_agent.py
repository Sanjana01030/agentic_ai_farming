import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml", "pest_model.pkl")

# Try to load model, use fallback if not available
try:
    model = joblib.load(MODEL_PATH)
    MODEL_AVAILABLE = True
except FileNotFoundError:
    model = None
    MODEL_AVAILABLE = False
    print(f"⚠️ Warning: Pest model not found at {MODEL_PATH}. Using fallback predictions.")


def predict_pest_risk(temp, humidity):
    """
    Predict pest risk based on temperature and humidity.
    Returns: "High", "Medium", or "Low"
    """
    if MODEL_AVAILABLE and model is not None:
        prediction = model.predict([[temp, humidity]])
        return prediction[0]
    else:
        # Fallback: Rule-based pest risk assessment
        # High temp + high humidity = high risk
        if temp > 30 and humidity > 70:
            return "High"
        elif temp > 25 and humidity > 60:
            return "Medium"
        else:
            return "Low"