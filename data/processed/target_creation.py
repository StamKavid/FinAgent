import pandas as pd
from datetime import datetime
from functools import reduce
import os
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
from scipy.signal._peak_finding import _boolrelextrema


df_processed = pd.read_parquet('C:\\Users\\Stamatis\\Desktop\\MLCryptoPredictor\\MLCryptoPredictor\\data\\processed\\processed_data.parquet.gzip')

# Rename the columns
df_processed.columns = df_processed.columns.str.replace(' ', '_')  # Replace spaces with underscores

df_processed = df_processed.ffill()

# Target creation
btc_target = df_processed[['Date', 'Adj_Close']].copy()  # Create DataFrame with specified columns and make a copy

# Calculate absolute change in adjusted closing price and add as a new column - Method 1 (Stationary)
btc_target['btc_daily_absolute_change'] = np.diff(btc_target['Adj_Close'], prepend=np.nan)

# Calculate relative change in adjusted closing price and add as a new column - Method 2 (Daily Returns)
btc_target['btc_daily_returns_perc'] = btc_target['Adj_Close'].pct_change() * 100

# Calculate log difference in adjusted closing price and add as a new column
btc_target['btc_log_difference'] = np.diff(np.log(btc_target['Adj_Close']), prepend=np.nan)

# Set 'Date' column as index inplace
btc_target.set_index('Date', inplace=True)

# Calculate local extrema for different window sizes and add as new columns
window_sizes = [7, 14, 21, 30, 60]
for window_size in window_sizes:
    btc_target[f'btc_price_min_{window_size}d'] = _boolrelextrema(np.array(btc_target.Adj_Close), np.less, order=window_size) * 1
    btc_target[f'btc_price_max_{window_size}d'] = _boolrelextrema(np.array(btc_target.Adj_Close), np.greater, order=window_size) * 1

btc_target.reset_index(inplace=True)

# btc_target.to_parquet('C:\\Users\\Stamatis\\Desktop\\MLCryptoPredictor\\MLCryptoPredictor\\data\\processed\\btc_target.parquet.gzip', compression='gzip')