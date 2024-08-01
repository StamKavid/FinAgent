import json
import os
from langchain.tools import tool
import joblib
import pandas as pd

class ForecastingTool():
    @tool("Forecasting Tool")
    def predict(date: str) -> str:
        """
        Use this tool to make a prediction for BTC price on a specific date using the Prophet model.
        The input to this tool should be a date in the format 'YYYY-MM-DD'.
        """
        try:
            # Load the trained Prophet model
            model = joblib.load('prophet_model.joblib')

            # Prepare the input data
            input_date = pd.to_datetime(date)
            future = pd.DataFrame({'ds': [input_date]})

            # Use the model to make a prediction
            forecast = model.predict(future)

            # Extract the prediction and confidence interval
            prediction = forecast['yhat'].iloc[0]
            # Return the prediction as a formatted string
            return json.dumps({
                "date": date,
                "prediction": prediction
            })
        except Exception as e:
            return json.dumps({
                "error": str(e)
            })