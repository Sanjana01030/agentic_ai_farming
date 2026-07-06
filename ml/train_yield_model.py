import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

print("Loading datasets...")

# Load datasets
crop = pd.read_csv("data/yield/crop_yield.csv")
soil = pd.read_csv("data/yield/state_soil_data.csv")
weather = pd.read_csv("data/yield/state_weather_data_1997_2020.csv")

print("Datasets loaded successfully")

# Clean column names (remove hidden spaces)
crop.columns = crop.columns.str.strip()
soil.columns = soil.columns.str.strip()
weather.columns = weather.columns.str.strip()

# Merge datasets
data = crop.merge(soil, on="state")
data = data.merge(weather, on=["state", "year"])

print("Merged dataset shape:", data.shape)

# Show merged columns (helps debugging)
print("Columns in merged dataset:")
print(data.columns)

# Features used for prediction
features = [
    "area",
    "fertilizer",
    "pesticide",
    "avg_temp_c",
    "total_rainfall_mm",
    "avg_humidity_percent",
    "N",
    "P",
    "K",
    "pH"
]

# Keep only features that exist in dataset
features = [f for f in features if f in data.columns]

print("Using features:", features)

# Remove rows with missing values
data = data.dropna()

# Input features
X = data[features]

# Target variable
y = data["yield"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training model...")

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


score = model.score(X_test, y_test)

print("Model accuracy:", score)


os.makedirs("models", exist_ok=True)


joblib.dump(model, "models/yield_prediction_model.pkl")

print("Model saved successfully!")