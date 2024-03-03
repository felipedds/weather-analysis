from sklearn.linear_model import Ridge
from joblib import dump
import os
import pandas as pd
import matplotlib.pyplot as plt 


data = pd.read_csv("../data/processed/historical_hourly_weather_processed.csv")
print(data.head())

# Defining the model's target
data["target"] = data.shift(-1)["temp"]

print(data.tail())

# Making a copy of the data frame just cut off the last row
data = data.iloc[:-1, :].copy()
print(data.tail())

'''
# Load and preprocess data
X_train, y_train = ...

# Train the model
model_ridge = Ridge(alpha=.1)
model_ridge.fit(X_train, y_train)

# Create the /models folder if it doesn't exist
if not os.path.exists("../models"):
    os.makedirs("../models")

# Save the trained model to the /models folder
model_file = '../models/linear_regression_model.joblib'
dump(model, model_file)

print("Model saved successfully.")
'''