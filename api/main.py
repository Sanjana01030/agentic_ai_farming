from fastapi import FastAPI
from agents.weather_agent import predict_weather
from agents.crop_agent import predict_yield

app = FastAPI()

@app.get("/weather/{city}")
def get_weather(city: str):
    return predict_weather(city)

@app.post("/predict-yield")
def yield_prediction(data: dict):
    result = predict_yield(data)
    return {"predicted_yield": result}