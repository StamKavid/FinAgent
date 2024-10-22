''' Importing the necessary libraries'''
import pandas as pd
import requests
import csv
import time
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Import environment variables
start_date = os.getenv('start_date')
end_date = os.getenv('end_date')

def fetch_fear_and_greed_index():
    # Base URL for the Fear and Greed Index API
    # Replace this with the actual API endpoint URL.
    base_url = "https://api.alternative.me/fng/?limit=0"
    response = requests.get(base_url)
    
    # Check if the response was successful
    if response.status_code == 200:
        data = response.json()
        return data['data']
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []

def main():
    # Convert list of dictionaries to DataFrame
    df = pd.DataFrame(fetch_fear_and_greed_index())
    
    # Convert Unix timestamps to human-readable date format "YYYY-MM-DD HH:MM:SS"
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

    # Filter the DataFrame for entries with a timestamp after January 1, 2018
    df = df[df['timestamp'] >= start_date]

    return df






