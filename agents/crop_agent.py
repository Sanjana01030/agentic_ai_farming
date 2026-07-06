import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "ml", "crop_model.pkl")

model = joblib.load(MODEL_PATH)


def predict_yield(*features):

    prediction = model.predict([list(features)])

    return prediction[0]