# Test Code Snippet:

import pickle
import numpy as np

# Load model
with open("crypto_liquidity_model.pkl", "rb") as f:
    model = pickle.load(f)

# Example input values
input_data = {
    "price": 40859.46,
    "1h": 0.022,
    "24h": 0.03,
    "7d": 0.055,
    "24h_volume": 3.5e10,
    "mkt_cap": 7.7e11
}

features = [
    input_data['price'],
    input_data['1h'],
    input_data['24h'],
    input_data['7d'],
    input_data['24h_volume'],
    input_data['mkt_cap'],
    abs(input_data['24h'])  # Volatility
]

# Make a prediction
prediction = model.predict([features])[0]
print(f"Predicted Liquidity Ratio: {prediction:.6f}")
