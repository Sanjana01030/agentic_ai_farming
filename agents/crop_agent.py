import joblib
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml", "crop_model.pkl")

# Try to load model, use fallback if not available
try:
    model = joblib.load(MODEL_PATH)
    MODEL_AVAILABLE = True
except FileNotFoundError:
    model = None
    MODEL_AVAILABLE = False
    print(f"⚠️ Warning: Crop model not found at {MODEL_PATH}. Using fallback predictions.")


def predict_yield(*features):
    """
    Predict crop yield based on features:
    area, fertilizer, pesticide, temp, rainfall, humidity, N, P, K, pH
    """
    if MODEL_AVAILABLE and model is not None:
        prediction = model.predict([list(features)])
        return prediction[0]
    else:
        # Fallback: Simple heuristic-based prediction
        # features: area, fertilizer, pesticide, temp, rainfall, humidity, N, P, K, pH
        area = features[0] if len(features) > 0 else 1000
        fertilizer = features[1] if len(features) > 1 else 500
        rainfall = features[4] if len(features) > 4 else 100
        
        # Simple formula: base yield affected by inputs
        base_yield = 2.5  # tons per unit area
        fertilizer_factor = 1 + (fertilizer / 1000)
        rainfall_factor = 1 + (rainfall / 500)
        
        estimated_yield = area * base_yield * fertilizer_factor * rainfall_factor
        
        return round(estimated_yield, 2)