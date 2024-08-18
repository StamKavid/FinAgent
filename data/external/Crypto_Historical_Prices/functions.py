import pandas as pd
import yfinance as yf
from dotenv import load_dotenv
import os

def load_environment_variables():
    """
    Load environment variables and return them as a dictionary.
    """
    load_dotenv()
    env_vars = {
        'start_date': os.getenv('start_date'),
        'end_date': os.getenv('end_date'),
        'btc_etf_start_date': os.getenv('btc_etf_start_date'),
        'btc_etf_end_date': os.getenv('btc_etf_end_date')
    }
    return env_vars

def download_data(tickers, start_date, end_date):
    """
    Download data for the given tickers within the specified date range.
    """
    data = {}
    for ticker in tickers:
        try:
            data[ticker] = yf.download(ticker, start=start_date, end=end_date)
        except Exception as e:
            print(f"Error downloading {ticker}: {e}")
    return data

def create_dataframe(data, columns):
    """
    Create a dataframe from the downloaded data and specify columns names.
    """
    df = pd.concat(data, axis=1)
    df.columns = columns
    return df

def calculate_gas_usd(df):
    """
    Calculates the GAS-USD price from a DataFrame containing ETH-USD and GAS-ETH prices.

    :param df: A pandas DataFrame with 'ETH_ADJ_CLOSE' and 'GAS_ADJ_CLOSE' columns.
    :return: A pandas DataFrame with an additional 'GAS_USD' column representing the calculated GAS-USD price.
    """
    if 'ETH_ADJ_CLOSE' in df.columns and 'GAS_ADJ_CLOSE' in df.columns:
        df['GAS_USD'] = df['ETH_ADJ_CLOSE'] * df['GAS_ADJ_CLOSE']
        return df
    else:
        raise ValueError("DataFrame must contain 'ETH_ADJ_CLOSE' and 'GAS_ADJ_CLOSE' columns")

def main():
    env_vars = load_environment_variables()
    
    # Define tickers for each category
    commodities = ['GC=F', 'SI=F', 'CL=F']
    currencies = ['EURUSD=X', 'JPY=X', 'GBPUSD=X', 'CNY=X']
    financial_indices = ['^VIX', '^TNX', '^FVX', '^RUT', 'TLT', '^IRX']
    stocks = ['TSLA', 'AMD', 'INTC', 'AAPL', 'NVDA', 'META', 'GOOG']
    btc_etfs = ['GBTC', 'ARKB', 'BITB', 'FBTC', 'BTCO', 'IBIT', 'HODL', 'BITO']
    cryptos = ['BTC-USD', 'ETH-USD', 'USDT-USD', 'USDC-USD', 'DOGE-USD', 'XRP-USD', 'SOL-USD', 'GAS-ETH']

    # Download data
    commodities_data = download_data(commodities, env_vars['start_date'], env_vars['end_date'])
    currencies_data = download_data(currencies, env_vars['start_date'], env_vars['end_date'])
    financial_indices_data = download_data(financial_indices, env_vars['start_date'], env_vars['end_date'])
    stocks_data = download_data(stocks, env_vars['start_date'], env_vars['end_date'])
    btc_etfs_data = download_data(btc_etfs, env_vars['btc_etf_start_date'], env_vars['btc_etf_end_date'])
    cryptos_data = download_data(cryptos, env_vars['start_date'], env_vars['end_date'])

    # Create dataframes
    df_commodities = create_dataframe([commodities_data[ticker]['Adj Close'] for ticker in commodities] +
                                      [commodities_data[ticker]['Volume'] for ticker in commodities],
                                      ['GOLD_ADJ_CLOSE', 'SILVER_ADJ_CLOSE', 'OIL_ADJ_CLOSE',
                                       'GOLD_VOLUME', 'SILVER_VOLUME', 'OIL_VOLUME'])
    
    df_currencies = create_dataframe([currencies_data[ticker]['Adj Close'] for ticker in currencies],
                                     ['EUR_USD_ADJ_CLOSE', 'USD_JPY_ADJ_CLOSE', 'GBP_USD_ADJ_CLOSE', 'USD_CNY_ADJ_CLOSE'])

    df_financial_ind = create_dataframe([financial_indices_data[ticker]['Adj Close'] for ticker in financial_indices] +
                                        [financial_indices_data['^RUT']['Volume'], financial_indices_data['TLT']['Volume']],
                                        ['VIX_ADJ_CLOSE', 'CBOE_INTEREST_RATE_ADJ_CLOSE', 'TREASURY_YIELD_5YRS_ADJ_CLOSE',
                                         'RUSSEL_2000_ADJ_CLOSE', 'ISHARES_20YR_ADJ_CLOSE', 'TREASURY_BILL_13WK_ADJ_CLOSE',
                                         'RUSSEL_2000_VOLUME', 'ISHARES_20YR_VOLUME'])

    df_stocks = create_dataframe([stocks_data[ticker]['Adj Close'] for ticker in stocks] +
                                 [stocks_data[ticker]['Volume'] for ticker in stocks],
                                 ['TESLA_ADJ_CLOSE', 'AMD_ADJ_CLOSE', 'INTEL_ADJ_CLOSE', 'APPLE_ADJ_CLOSE', 'NVIDIA_ADJ_CLOSE', 'META_ADJ_CLOSE', 'GOOGLE_ADJ_CLOSE',
                                  'TESLA_VOLUME', 'AMD_VOLUME', 'INTEL_VOLUME', 'APPLE_VOLUME', 'NVIDIA_VOLUME', 'META_VOLUME', 'GOOGLE_VOLUME'])

    df_btc_etf = create_dataframe([btc_etfs_data[ticker]['Adj Close'] for ticker in btc_etfs] +
                                  [btc_etfs_data[ticker]['Volume'] for ticker in btc_etfs],
                                  ['GBTC_ADJ_CLOSE', 'ARKB_ADJ_CLOSE', 'BITB_ADJ_CLOSE', 'FBTC_ADJ_CLOSE', 'BTCO_ADJ_CLOSE', 'IBIT_ADJ_CLOSE', 'HODL_ADJ_CLOSE', 'BITO_ADJ_CLOSE',
                                   'GBTC_VOLUME', 'ARKB_VOLUME', 'BITB_VOLUME', 'FBTC_VOLUME', 'BTCO_VOLUME', 'IBIT_VOLUME', 'HODL_VOLUME', 'BITO_VOLUME'])

    # Start by extracting BTC data with specific columns
    btc_data = cryptos_data['BTC-USD'][['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
    btc_data.columns = ['BTC_OPEN', 'BTC_HIGH', 'BTC_LOW', 'BTC_CLOSE', 'BTC_ADJ_CLOSE', 'BTC_VOLUME']

    # Now process other cryptocurrencies
    other_crypto_data = []
    for ticker in cryptos[1:]:  # Assuming 'cryptos' list starts with 'BTC-USD'
        ticker_data = cryptos_data[ticker][['Adj Close', 'Volume']]
        ticker_data.columns = [f'{ticker[:-4]}_ADJ_CLOSE', f'{ticker[:-4]}_VOLUME']
        other_crypto_data.append(ticker_data)

    # Concatenate BTC data with other cryptocurrencies data
    df_crypto_hist = pd.concat([btc_data] + other_crypto_data, axis=1)

    df_crypto_hist.columns = ['BTC_OPEN', 'BTC_HIGH', 'BTC_LOW', 'BTC_CLOSE', 'BTC_ADJ_CLOSE', 'BTC_VOLUME',
                              'ETH_ADJ_CLOSE', 'ETH_VOLUME', 'USDT_ADJ_CLOSE', 'USDT_VOLUME',
                              'USDC_ADJ_CLOSE', 'USDC_VOLUME', 'DOGE_ADJ_CLOSE', 'DOGE_VOLUME',
                              'XRP_ADJ_CLOSE', 'XRP_VOLUME', 'SOL_ADJ_CLOSE', 'SOL_VOLUME', 'GAS_ADJ_CLOSE', 'GAS_VOLUME']
   
    # Concatenate all dataframes into a single dataframe
    df_yfinance = pd.concat([df_commodities, df_currencies, df_financial_ind, df_stocks, df_btc_etf, df_crypto_hist], axis=1)
    
    result_df = calculate_gas_usd(df_yfinance)
    result_df.reset_index(inplace=True)
    return result_df
    