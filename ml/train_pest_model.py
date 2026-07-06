import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
import os

os.makedirs("ml", exist_ok=True)


X = np.random.rand(100, 2)  # temp + humidity
y = np.random.choice(["Low", "Medium", "High"], 100)

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "ml/pest_model.pkl")

print("pest_model.pkl created successfully")