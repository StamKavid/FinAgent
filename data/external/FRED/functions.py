from fredapi import Fred
import pandas as pd
from statsmodels.tsa.seasonal import STL

def load_and_process_seasonal_data(data_fetcher, series_id, value_column, start_date='2018-01-01', 
                          resample_frequency='D', seasonal=7):
    """
    Loads and processes time series data from a given data source, handles missing values, 
    resamples to a given frequency, and applies STL decomposition.
    """
    series_data = data_fetcher(series_id)
    series_data.name = value_column
    df = series_data.to_frame().reset_index()

    df['index'] = pd.to_datetime(df['index'])
    df = df.set_index('index')
    df = df[df.index >= start_date]

    df_resampled = df.resample(resample_frequency).mean()
    df_resampled[value_column] = df_resampled[value_column].ffill().bfill().interpolate(method='linear')

    stl = STL(df_resampled[value_column], seasonal=seasonal, robust=True)
    result = stl.fit()

    df_adjusted = result.trend.to_frame(name=f'{value_column}_adjusted')

    return df_resampled.reset_index(), df_adjusted.reset_index()

def process_time_series_data(df, date_column='Date', value_column='Value', start_date='2018-01-01', resample_frequency='D', interpolate_method='linear'):
    """
    Processes time series data by filtering, cleaning, and resampling.
    """
    df[date_column] = pd.to_datetime(df[date_column])
    df.set_index(date_column, inplace=True)

    filtered_df = df[df.index >= start_date].dropna(subset=[value_column])

    resampled_df = filtered_df.resample(resample_frequency).interpolate(method=interpolate_method)

    return resampled_df.reset_index()
