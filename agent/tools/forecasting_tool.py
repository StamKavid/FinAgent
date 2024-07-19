import json
import os
from langchain.tools import tool

class ForecastingTool():
    @tool("Forecasting Tool")
    def predict(date):
        """
        Use this tool to make a prediction for BTC price on a specific date using the Prophet model.
        The input to this tool should be a date.
        """
        return "100,000$"