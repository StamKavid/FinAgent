from dotenv import load_dotenv
import os
from functools import reduce
import pandas as pd
from fredapi import Fred
from functions import load_and_process_seasonal_data, process_time_series_data

load_dotenv()
api_key = os.getenv('FRED_API_KEY')
fred = Fred(api_key= api_key)

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

dataframes = [sp500_adjusted, processed_gdp, processed_real_gdp, processed_unrate_df, processed_cpi_df, int_rate_adjusted, treasure_df_adjusted, inflation_rate_adjusted, processed_sticky_cpi_df, m2_money_stock_adjusted]
merged_df = reduce(lambda left, right: pd.merge(left, right, on='index', how='outer'), dataframes)

merged_df_processed = merged_df.bfill().ffill().interpolate(method='pad')

# merged_df_processed.to_csv('fred_processed.csv', index=True)

merged_df_processed.to_parquet('fred_processed.parquet.gzip', compression='gzip')