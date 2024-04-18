import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os

def load_environment_variables():
    """Load environment variables from .env file."""
    load_dotenv()

def read_data(file_path):
    """Read data from a CSV file."""
    return pd.read_csv(file_path)

def clean_btc_dominance(btc_dominance, start_date):
    """Clean Bitcoin dominance data."""
    btc_dominance['DateTime'] = pd.to_datetime(btc_dominance['DateTime']).dt.strftime("%Y-%m-%d")
    btc_dominance = btc_dominance[btc_dominance['DateTime'] >= start_date].reset_index(drop=True)
    btc_dominance.rename(columns={'DateTime': 'Date'}, inplace=True)
    return btc_dominance

def clean_date_column(data_frame, column_name):
    """Clean date column in a DataFrame."""
    data_frame[column_name] = pd.to_datetime(data_frame[column_name]).dt.strftime("%Y-%m-%d")
    data_frame.rename(columns={column_name: 'Date'}, inplace=True)
    return data_frame

def convert_year_to_period_index(data_frame, column_name):
    """Convert 'year' column to PeriodIndex with frequency 'Q'."""
    data_frame[column_name] = pd.PeriodIndex(data_frame[column_name], freq='Q')
    data_frame[column_name] = data_frame[column_name].astype('datetime64[ns]')
    data_frame[column_name] = data_frame[column_name].dt.strftime('%Y-%m-%d')
    data_frame.rename(columns={column_name: 'Date'}, inplace=True)
    return data_frame

def merge_data_frames(*data_frames):
    """Merge multiple DataFrames."""
    merged_df = pd.merge(data_frames[0], data_frames[1], on='Date', how='left')
    for df in data_frames[2:]:
        merged_df = pd.merge(merged_df, df, on='Date', how='left')
    return merged_df

def main():
    # Load environment variables
    load_environment_variables()
    
    # Import environment variables
    start_date = os.getenv('start_date')
    end_date = os.getenv('end_date')

    # Define the folder containing the CSV files
    data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')

    # Print the data_folder path to check
    print("data_folder:", data_folder)

    # Read data from CSV files
    btc_dominance = read_data(os.path.join(data_folder, r'bitcoin-dominance_(Coinmarketcap).csv'))
    data_gpr = read_data(os.path.join(data_folder,r'data_gpr_export.csv'))
    market_cap = read_data(os.path.join(data_folder,r'market-cap_20130429_20240413_(Coinmarketcap).csv'))
    market_volume = read_data(os.path.join(data_folder,r'volume-24h_20130429_20240413_(Coinmarketcap).csv'))
    wtui_df = read_data(os.path.join(data_folder,r'WTUI_Data.csv'))
    wui_df = read_data(os.path.join(data_folder,r'WUI_Data.csv'))

    # Clean data
    btc_dominance = clean_btc_dominance(btc_dominance, start_date)
    data_gpr = clean_date_column(data_gpr, 'month')
    market_cap = clean_date_column(market_cap, 'DateTime')
    market_volume = clean_date_column(market_volume, 'DateTime')
    wtui_df = convert_year_to_period_index(wtui_df, 'year')
    wui_df = convert_year_to_period_index(wui_df, 'year')

    # Create a dummy DataFrame with the date range
    dummy_df = pd.DataFrame({'Date': pd.date_range(start=start_date, end=end_date)})
    dummy_df['Date'] = pd.to_datetime(dummy_df['Date']).dt.strftime("%Y-%m-%d")

    # Merge all DataFrames
    merged_df = merge_data_frames(dummy_df, btc_dominance, data_gpr, market_cap, market_volume, wtui_df, wui_df)

    return merged_df