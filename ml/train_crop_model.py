import numpy as np
import joblib
from sklearn.linear_model import LinearRegression

# dummy training data
X = np.random.rand(100, 10)
y = np.random.rand(100)

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "ml/crop_model.pkl")

print("Model saved successfully")
