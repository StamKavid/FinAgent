# Description: This file contains the code to scrap data from the web.
from fredapi import Fred
from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Pandas options
pd.set_option('display.max_columns', None)  # or use a specific number if you know the column count
pd.set_option('display.max_rows', None)  # or use a specific number if you know the row count
pd.set_option('display.max_colwidth', None)  # or use a large number like 1000

# Matplotlib style
plt.style.use('ggplot')

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('FRED_API_KEY')
fred = Fred(api_key= api_key)

## Data Fetching
# Fetch the SP500 index Daily data
sp500 = fred.get_series(series_id='SP500')
sp500.name = ('sp500')

# Fetch the GDP index Quarterly data
gdp = fred.get_series('GDP')
gdp.name = ('gdp')

# Fetch the Real GDP index Quarterly data
real_gdp = fred.get_series('GDPC1')
real_gdp.name = ('rgdp')

# Fetch the Unemployment rate Monthly data
unrate_df = fred.get_series(series_id= 'UNRATE')
unrate_df.name = ('UNRATE')

# Fetch the Consumer Price Index Monthly data
cpi_df = fred.get_series(series_id= 'CPIAUCSL')
cpi_df.name = ('CPI')

# Fetch the 10-year Real Interest Rate Monthly Data
int_rate_df = fred.get_series(series_id= 'REAINTRATREARAT10Y')
int_rate_df.name = ('INT_RATE')

# Fetch the 10-year Treasury Constant Maturity Rate Daily Data
treasure_df = fred.get_series(series_id= 'T10Y2Y')
treasure_df.name = ('TREASURE')

# Fetch the 10-year Inflation Rate Daily Data
inflation_df = fred.get_series(series_id= 'T10YIE')
inflation_df.name = ('INFLATION')

# Fetch Sticky Price Consumer Price Index Monthly Data
sticky_cpi_df = fred.get_series(series_id= 'CORESTICKM159SFRBATL')
sticky_cpi_df.name = ('STICKY_CPI')

# Fetch M2 Money Stock Weekly Data
m2_df = fred.get_series(series_id= 'WM2NS')
m2_df.name = ('M2')