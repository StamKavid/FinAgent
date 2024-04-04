from fredapi import Fred
from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from statsmodels.tsa.seasonal import seasonal_decompose, STL
from functools import reduce

plt.style.use('ggplot')

# Pandas options
pd.set_option('display.max_columns', None)  # or use a specific number if you know the column count
pd.set_option('display.max_rows', None)  # or use a specific number if you know the row count
pd.set_option('display.max_colwidth', None)  # or use a large number like 1000

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('FRED_API_KEY')
fred = Fred(api_key= api_key)

# Function to fetch a time series from FRED and seasonal decompose it
def load_and_process_seasonal_data(data_fetcher, series_id, value_column, start_date='2018-01-01', 
                          resample_frequency='D', seasonal=7):
    """
    Loads and processes time series data from a given data source, handles missing values, 
    resamples to a given frequency, and applies STL decomposition.

    Parameters:
    - data_fetcher: Function to fetch the time series data (e.g., fred.get_series)
    - series_id: Identifier for the series to fetch (e.g., 'SP500')
    - value_column: Desired name for the value column in the output DataFrame
    - start_date: The start date for filtering the data
    - resample_frequency: The frequency to which the data should be resampled (e.g., 'D' for daily)
    - seasonal: Seasonal period for STL decomposition

    Returns:
    - A tuple of DataFrames: the resampled original and the seasonally adjusted data
    """
    # Fetch the time series data and set the column name
    series_data = data_fetcher(series_id)
    series_data.name = value_column
    df = series_data.to_frame().reset_index()

    # Convert the date column to datetime, set as index, and filter the data
    df['index'] = pd.to_datetime(df['index'])
    df = df.set_index('index')
    df = df[df.index >= start_date]

    # Resample and interpolate the data to handle missing values
    df_resampled = df.resample(resample_frequency).mean()
    df_resampled[value_column] = df_resampled[value_column].bfill().interpolate(method='linear')

    # Apply STL decomposition to extract the trend component
    stl = STL(df_resampled[value_column], seasonal=seasonal, robust=True)
    result = stl.fit()

    # Extract the seasonally adjusted series and convert to DataFrame
    df_adjusted = result.trend.to_frame(name=f'{value_column}_adjusted')

    return df_resampled.reset_index(), df_adjusted.reset_index()

# Function to fetch a time series from FRED and resample it
def process_time_series_data(df, date_column='Date', value_column='Value', start_date='2018-01-01', resample_frequency='D', interpolate_method='linear'):
    """
    Processes time series data by filtering, cleaning, and resampling.

    Parameters:
    - df: DataFrame containing the time series data.
    - date_column: The column name in the DataFrame that contains the date information.
    - value_column: The column name in the DataFrame that contains the value to process.
    - start_date: The start date for filtering the data.
    - resample_frequency: The frequency to which the data should be resampled.
    - interpolate_method: The method used for interpolation during resampling.

    Returns:
    - A DataFrame with processed time series data.
    """
    # Convert date column to datetime and set as index
    df[date_column] = pd.to_datetime(df[date_column])
    df.set_index(date_column, inplace=True)

    # Filter based on start date and drop rows with missing target values
    filtered_df = df[df.index >= start_date].dropna(subset=[value_column])

    # Resample and interpolate the data
    resampled_df = filtered_df.resample(resample_frequency).interpolate(method=interpolate_method)

    # Reset the index to turn the date index back into a column
    return resampled_df.reset_index()

# Macroeconomic Indicators
sp500_processed, sp500_adjusted = load_and_process_seasonal_data(fred.get_series, 'SP500', 'sp500')

gdp_df = fred.get_series('GDP').to_frame('gdp').reset_index()
processed_gdp = process_time_series_data(gdp_df, date_column='index', value_column='gdp')

real_gdp_df = fred.get_series('GDPC1').to_frame('rgdp').reset_index()
processed_real_gdp = process_time_series_data(real_gdp_df, date_column='index', value_column='rgdp')

unrate_df = fred.get_series('UNRATE').to_frame('unrate').reset_index()
processed_unrate_df = process_time_series_data(unrate_df, date_column='index', value_column='unrate')

cpi_df = fred.get_series('CPIAUCSL').to_frame('cpi').reset_index()
processed_cpi_df = process_time_series_data(cpi_df, date_column='index', value_column='cpi')

int_rate_processed, int_rate_adjusted = load_and_process_seasonal_data(fred.get_series, 'REAINTRATREARAT10Y', 'interest_rate')

treasure_df_processed, treasure_df_adjusted = load_and_process_seasonal_data(fred.get_series, 'T10Y2Y', 'treasure_maturity')

inflation_rate_processed, inflation_rate_adjusted = load_and_process_seasonal_data(fred.get_series, 'T10YIE', 'inflation_rate')

sticky_cpi_df = fred.get_series('CORESTICKM159SFRBATL').to_frame('sticky_cpi').reset_index()
processed_sticky_cpi_df = process_time_series_data(sticky_cpi_df, date_column='index', value_column='sticky_cpi')

m2_money_stock_processed, m2_money_stock_adjusted = load_and_process_seasonal_data(fred.get_series, 'WM2NS', 'm2_money_stock')

# Merge dataframes
# List of dataframes to merge
dataframes = [sp500_adjusted, processed_gdp, processed_real_gdp, processed_unrate_df, processed_cpi_df, int_rate_adjusted, treasure_df_adjusted, inflation_rate_adjusted, processed_sticky_cpi_df, m2_money_stock_adjusted]
merged_df = reduce(lambda left, right: pd.merge(left, right, on='index', how='outer'), dataframes)

merged_df_processed = merged_df.interpolate(method='linear')

# merged_df_processed.to_csv('fred_processed_data.csv', index=True)