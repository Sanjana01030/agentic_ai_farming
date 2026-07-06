import requests

API_KEY = "a3798e4c82181bb101041e6aa29b0fec"


def predict_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    # check if API failed
    if "main" not in data:
        raise Exception(f"Weather API error: {data}")

    return {
        "avg_temp": data["main"]["temp"],
        "avg_humidity_percent": data["main"]["humidity"],
        "total_rainfall_mm": data.get("rain", {}).get("1h", 0)
    }