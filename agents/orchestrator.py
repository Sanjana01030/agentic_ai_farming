from agents.weather_agent import predict_weather
from agents.crop_agent import predict_yield
from agents.pest_agent import predict_pest_risk
from agents.llm_agent import ask_llm


def route_question(question):

    q = question.lower()

    if "weather" in q or "rain" in q:
        return predict_weather("Chennai")

    elif "yield" in q or "production" in q:
        return predict_yield([25, 60, 7])

    elif "pest" in q or "disease" in q:
        return predict_pest_risk([30, 80, 10])

    else:
        return ask_llm(question)
        