from sklearn.linear_model import LinearRegression
from joblib import dump
import os
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/historical_hourly_weather_processed.csv")
data.head()

# Load and preprocess data
X_train, y_train = ...

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Create the /models folder if it doesn't exist
if not os.path.exists('../models'):
    os.makedirs('../models')

# Save the trained model to the /models folder
model_file = '../models/linear_regression_model.joblib'
dump(model, model_file)

print("Model saved successfully.")