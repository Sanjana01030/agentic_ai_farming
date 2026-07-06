"""
Generate ML models for the AI Farming Assistant.
Run this script to create crop_model.pkl and pest_model.pkl
"""

import os
import sys
import joblib
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split

def create_crop_model():
    """Create a simple crop yield prediction model"""
    print("🌾 Creating crop yield model...")
    
    # Generate synthetic training data
    np.random.seed(42)
    n_samples = 1000
    
    data = {
        'area': np.random.uniform(100, 5000, n_samples),
        'fertilizer': np.random.uniform(100, 2000, n_samples),
        'pesticide': np.random.uniform(50, 500, n_samples),
        'temp': np.random.uniform(15, 40, n_samples),
        'rainfall': np.random.uniform(50, 300, n_samples),
        'humidity': np.random.uniform(40, 90, n_samples),
        'N': np.random.uniform(20, 100, n_samples),
        'P': np.random.uniform(10, 80, n_samples),
        'K': np.random.uniform(10, 80, n_samples),
        'pH': np.random.uniform(4.5, 8.5, n_samples),
    }
    
    # Create target: yield = f(area, fertilizer, rainfall, etc.)
    yield_values = (
        data['area'] * 2.5 * 
        (1 + data['fertilizer']/1000) * 
        (1 + data['rainfall']/500) *
        (0.8 + 0.4 * (data['pH'] - 4.5) / 4.0) +
        np.random.normal(0, 200, n_samples)  # Add noise
    )
    
    X = pd.DataFrame(data)
    y = yield_values
    
    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    # Save model
    os.makedirs('ml', exist_ok=True)
    joblib.dump(model, 'ml/crop_model.pkl')
    print("✅ Crop model saved to ml/crop_model.pkl")


def create_pest_model():
    """Create a simple pest risk prediction model"""
    print("🐛 Creating pest risk model...")
    
    # Generate synthetic training data
    np.random.seed(42)
    n_samples = 1000
    
    temps = np.random.uniform(15, 40, n_samples)
    humidity = np.random.uniform(40, 90, n_samples)
    
    # Rule-based labels with some noise
    risk_labels = []
    for t, h in zip(temps, humidity):
        if t > 30 and h > 70:
            risk_labels.append('High' if np.random.random() > 0.1 else 'Medium')
        elif t > 25 and h > 60:
            risk_labels.append('Medium' if np.random.random() > 0.15 else 'Low')
        else:
            risk_labels.append('Low' if np.random.random() > 0.1 else 'Medium')
    
    X = np.column_stack([temps, humidity])
    y = risk_labels
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    # Save model
    os.makedirs('ml', exist_ok=True)
    joblib.dump(model, 'ml/pest_model.pkl')
    print("✅ Pest model saved to ml/pest_model.pkl")


def main():
    """Generate all models"""
    print("=" * 50)
    print("🤖 AI Farming Assistant - Model Generator")
    print("=" * 50)
    print()
    
    try:
        create_crop_model()
        print()
        create_pest_model()
        print()
        print("=" * 50)
        print("✅ All models generated successfully!")
        print("=" * 50)
        print()
        print("You can now run the application with:")
        print("  streamlit run chatbot_app.py")
        print()
        
    except Exception as e:
        print(f"❌ Error generating models: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
