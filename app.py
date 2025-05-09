from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the saved model (make sure this file exists)
model = joblib.load('heart_disease_model.pkl')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Heart Disease Prediction API!"

if __name__ == '__main__':
    app.run(debug=True)
