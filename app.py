import streamlit as st

from agents.weather_agent import predict_weather
from agents.crop_agent import predict_yield
from agents.pest_agent import predict_pest_risk

st.title("🌱 AI Farming Assistant")

city = st.text_input("Enter City")

area = st.number_input("Cultivation Area")
fertilizer = st.number_input("Fertilizer Usage")
pesticide = st.number_input("Pesticide Usage")

N = st.number_input("Nitrogen Level")
P = st.number_input("Phosphorus Level")
K = st.number_input("Potassium Level")
pH = st.number_input("Soil pH")

if st.button("Predict Yield"):

    weather = predict_weather(city)

    temp = weather["avg_temp"]
    rainfall = weather["total_rainfall_mm"]
    humidity = weather["avg_humidity_percent"]

    yield_prediction = predict_yield(
        area,
        fertilizer,
        pesticide,
        temp,
        rainfall,
        humidity,
        N,
        P,
        K,
        pH
    )

    pest_risk = predict_pest_risk(temp, humidity)

    st.success(f"Predicted Yield: {yield_prediction}")
    st.warning(f"Pest Risk: {pest_risk}")