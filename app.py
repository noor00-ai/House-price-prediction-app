from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# ==========================================================
# Create FastAPI Application
# ==========================================================
app = FastAPI(
    title="House Price Prediction API",
    description="Predict House Prices using a trained Machine Learning Regression Model",
    version="1.0"
)

# ==========================================================
# Load Saved Model and Scalers
# ==========================================================
model = joblib.load("house_price_model.pkl")
scaler = joblib.load("scaler.pkl")
target_scaler = joblib.load("target_scaler.pkl")

# ==========================================================
# Input Data Schema
# ==========================================================
class HouseData(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    parking: int

    mainroad_yes: int
    guestroom_yes: int
    basement_yes: int
    hotwaterheating_yes: int
    airconditioning_yes: int
    prefarea_yes: int

    furnishingstatus_semi_furnished: int
    furnishingstatus_unfurnished: int


# ==========================================================
# Home Route
# ==========================================================
@app.get("/")
def home():
    return {
        "message": "House Price Prediction API is Running!"
    }


# ==========================================================
# Prediction Route
# ==========================================================
@app.post("/predict")
def predict_price(data: HouseData):

    try:

        # Arrange features exactly as used during training
        features = [[
            data.area,
            data.bedrooms,
            data.bathrooms,
            data.stories,
            data.parking,
            data.mainroad_yes,
            data.guestroom_yes,
            data.basement_yes,
            data.hotwaterheating_yes,
            data.airconditioning_yes,
            data.prefarea_yes,
            data.furnishingstatus_semi_furnished,
            data.furnishingstatus_unfurnished
        ]]

        # Scale Features
        scaled_features = scaler.transform(features)

        # Predict
        prediction = model.predict(scaled_features)

        # Convert prediction back to original price
        prediction = np.array(prediction).reshape(-1, 1)
        original_price = target_scaler.inverse_transform(prediction)

        # Return Result
        return {
            "Predicted House Price": round(float(original_price[0][0]), 2)
        }

    except Exception as e:
        return {
            "Error": str(e)
        }