import pandas as pd
from datetime import datetime
from functools import reduce
import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from datetime import datetime, timedelta

end_date = '2024-04-01'
end_date = datetime.strptime(end_date, '%Y-%m-%d')  # Convert end_date to datetime object
new_date = end_date - timedelta(days=1)  # Subtract 1 day from end_date

new_date_str = new_date.strftime('%Y-%m-%d')  # Convert new_date back to string format

# Load environment variables from .env file
load_dotenv()

# Import environment variables
start_date = os.getenv('start_date')
end_date = os.getenv('end_date')

cwd = os.getcwd()  # get current working directory

# Create a dummy DataFrame with the date range
dummy_df = pd.DataFrame({'Date': pd.date_range(start=start_date, end=new_date_str)})
dummy_df['Date'] = pd.to_datetime(dummy_df['Date']).dt.strftime("%Y-%m-%d")
dummy_df['Date'] = dummy_df['Date'].astype('datetime64[ns]')

df_yahoo = pd.read_parquet("data\\external\\Crypto_Historical_Prices\\files\\yahoo_finance.parquet.gzip")

# Fill missing values with the previous value and interpolate the rest
df_yahoo = df_yahoo.bfill().interpolate(method='linear')

merged_df_1 = pd.merge(dummy_df, df_yahoo, on='Date', how='left')

df_fear = pd.read_parquet("data\\external\\Fear_and_Greed_Index\\files\\btc_fear_and_greed.parquet.gzip")

df_fear = df_fear[['timestamp', 'value', 'value_classification']]
df_fear.rename(columns={'timestamp': 'Date'}, inplace=True)
df_fear.sort_values(by='Date', inplace=True)
df_fear.reset_index(drop=True, inplace=True)    

merged_df_2 = pd.merge(dummy_df, df_fear, on='Date', how='left')

# Fill missing values with the previous value and interpolate the rest
merged_df_2 = merged_df_2.bfill().interpolate(method='linear')

df = pd.DataFrame(merged_df_2)

# Pivot the dataframe to get counts of each value classification for each date
pivot_df = df.pivot_table(index='Date', columns='value_classification', aggfunc='size', fill_value=0)

# Join the pivot table with the original dataframe
df = df.merge(pivot_df, on='Date')

# Rename the columns
df.columns = df.columns.str.replace(' ', '_')  # Replace spaces with underscores

df_fred = pd.read_parquet('data\\external\\FRED\\files\\fred_processed.parquet.gzip')

df_fred.rename(columns={'index': 'Date'}, inplace=True)
df_fred.sort_values(by='Date', inplace=True)
df_fred.reset_index(drop=True, inplace=True) 

merged_df_3 = pd.merge(dummy_df, df_fred, on='Date', how='left')

df_tech_ind = pd.read_parquet('data\\external\\Technical_Indicators\\files\\btc_technical_indicators.parquet.gzip')

# Check for missing values
df_tech_ind.isna().sum()

merged_df_4 = pd.merge(dummy_df, df_tech_ind, on='Date', how='left')

# Fill missing values with the previous value and interpolate the rest
merged_df_4 = merged_df_4.bfill().interpolate(method='linear')

## Social Media - Aggregations Twitter

df_tweet_grouped = pd.read_parquet('data\\external\\Social_Media\\files\\Bitcoin_tweets_grouped.parquet.gzip')

df_tweet_grouped.rename(columns={'date': 'Date'}, inplace=True)

df_tweet_grouped['Date'] = pd.to_datetime(df_tweet_grouped['Date'])

merged_df_5 = pd.merge(dummy_df, df_tweet_grouped, on='Date', how='left')

# Fill missing values with the previous value and interpolate the rest
merged_df_5 = merged_df_5.bfill().interpolate(method='linear')

df_raw = pd.read_parquet('data\\raw\\files\\raw_data.parquet.gzip')

df_raw['Date'] = df_raw['Date'].astype('datetime64[ns]')

merged_df_6 = pd.merge(dummy_df, df_raw, on='Date', how='left')

# Fill missing values with the previous value and interpolate the rest
merged_df_6 = merged_df_6.bfill().interpolate(method='linear')

## Target Creation

df_target = pd.read_parquet('data\\processed\\files\\btc_target.parquet.gzip')

df_target['Date'] = df_target['Date'].astype('datetime64[ns]')

merged_df_7 = pd.merge(dummy_df, df_target, on='Date', how='left')

# Fill missing values with the previous value and interpolate the rest
merged_df_7 = merged_df_7.bfill().interpolate(method='linear')

df_processed = pd.concat([merged_df_1, df, merged_df_3, merged_df_4, merged_df_5, merged_df_6, merged_df_7], axis=1)

# Remove duplicate columns
df_processed = df_processed.loc[:, ~df_processed.columns.duplicated()]

columns_to_delete = ['BTC_OPEN', 'BTC_HIGH', 'BTC_LOW', 'BTC_CLOSE', 'BTC_ADJ_CLOSE']

# Delete the specified columns
df_processed = df_processed.drop(columns=columns_to_delete)

df_processed.rename(columns={'Market cap': 'MARKET_CAP', 'Volume (24h)' : 'CRYPTO_VOLUME_24' }, inplace=True)

del df_processed['var_name'], df_processed['var_label']

# Columns to move to the beginning
columns_to_move = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

# Reorder columns
df_processed = df_processed[columns_to_move + [col for col in df_processed if col not in columns_to_move]]

# df_processed.to_parquet('data\\processed\\files\\processed_data.parquet.gzip', compression='gzip')