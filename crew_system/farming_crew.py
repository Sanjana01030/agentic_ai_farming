from crewai import Agent, Task, Crew

weather_agent = Agent(
    role="Weather Analyst",
    goal="Provide weather data for farming",
    backstory="Expert in agricultural weather patterns",
    verbose=True,
    llm=None
)

crop_agent = Agent(
    role="Crop Yield Predictor",
    goal="Predict crop yield based on soil and weather",
    backstory="Machine learning crop prediction expert",
    verbose=True,
    llm=None
)

pest_agent = Agent(
    role="Pest Risk Analyst",
    goal="Detect pest risk",
    backstory="Agricultural pest expert",
    verbose=True,
    llm=None
)