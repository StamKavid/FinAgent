import pandas as pd
import yfinance as yf
from dotenv import load_dotenv
import os
from ta import add_all_ta_features

# Load environment variables from .env file
load_dotenv()

def fetch_historical_data(ticker, start_date, end_date):
    """Fetch historical data for a given ticker between start_date and end_date."""
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def add_technical_analysis_features(data):
    """Add technical analysis features to the given data."""
    try:
        return add_all_ta_features(
            data, open="Open", high="High", low="Low", close="Close", volume="Volume"
        )
    except Exception as e:
        print(f"Error adding technical analysis features: {e}")
        return data

def main():
    start_date = os.getenv('start_date')
    end_date = os.getenv('end_date')

    btc_usd_data = fetch_historical_data('BTC-USD', start_date, end_date)
    
    if btc_usd_data is not None:
        btc_usd_data = add_technical_analysis_features(btc_usd_data)
        btc_usd_data.reset_index(inplace=True)
    else:
        btc_usd_data = None
        
    return btc_usd_data



