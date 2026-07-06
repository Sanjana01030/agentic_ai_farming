from agents.weather_agent import predict_weather
from agents.crop_agent import predict_yield
from agents.pest_agent import predict_pest_risk

print("🌱 AI Farming Assistant")

# User inputs
city = input("Enter city: ")

area = float(input("Enter cultivation area: "))
fertilizer = float(input("Enter fertilizer usage: "))
pesticide = float(input("Enter pesticide usage: "))

N = float(input("Enter Nitrogen level: "))
P = float(input("Enter Phosphorus level: "))
K = float(input("Enter Potassium level: "))
pH = float(input("Enter soil pH: "))

print("\nFetching weather data...")

# Weather agent
weather = predict_weather(city)

temp = weather["avg_temp"]
rainfall = weather["total_rainfall_mm"]
humidity = weather["avg_humidity_percent"]

print("Weather conditions:", weather)

print("\nPredicting crop yield...")

# Crop agent
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

print("Predicted Crop Yield:", yield_prediction)

# Pest agent
pest_risk = predict_pest_risk(temp, humidity)

print("Pest Risk:", pest_risk)

# Simple recommendation
print("\n🌾 Farming Recommendation")

if yield_prediction < 1:
    print("Improve irrigation and soil nutrients.")
elif yield_prediction < 3:
    print("Use balanced fertilizer and monitor pests.")
else:
    print("Conditions look good for cultivation.")