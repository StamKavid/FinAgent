
# 📈 __Historical Crypto Data Analysis Using Yahoo Finance__ 📊

[View the BTC - EDA Report]()

## __Introduction__

This repository is dedicated to the extraction and analysis of historical cryptocurrency data from Yahoo Finance, leveraging the yfinance Python library. The focus is on examining the price dynamics and market behavior of leading cryptocurrencies over time, utilizing statistical and machine learning techniques to uncover trends and patterns.

The initiative involves downloading historical price information, performing extensive exploratory data analysis (EDA), and applying quantitative analysis to understand the volatility and relationships between different cryptocurrencies.

## 💡 __Analysis Insights__

• Focused on major cryptocurrencies like Bitcoin (BTC) and Ethereum (ETH) to track price changes and volatility since 2018.

• Developed candlestick charts for detailed price movement analysis.

• Constructed a correlation matrix to understand inter-relationships between different cryptocurrencies.


## 🎯 __Project Objectives__

• __*Data Acquisition*__

Automate the retrieval of historical price data for various cryptocurrencies using the yfinance library.

```python
import yfinance as yf

# Example to fetch historical data for Bitcoin
btc_data = yf.download("BTC-USD", start="2018-01-01", end="2023-12-31")
```

• __*Data Preprocessing*__

Clean and preprocess the acquired data to ensure accuracy and reliability for further analysis.

• __*Exploratory Data Analysis (EDA)*__

Conduct an in-depth EDA to examine trends, correlations, and distribution characteristics of cryptocurrency data.

![alt text](https://github.com/StamKavid/MLCryptoPredictor/blob/dev/data/external/Crypto_Historical_Prices/Images/Adjusted_close_prices_BTC_ETH.png)

**Figure 1**: Adjusted Close prices for BTC and ETH for 2018 - 2024.


![alt text](https://github.com/StamKavid/MLCryptoPredictor/blob/dev/data/external/Crypto_Historical_Prices/Images/trading_volume_BTC_ETH.png)

**Figure 2**: Trading volume for BTC and ETH for 2018 - 2024.


![alt text](https://github.com/StamKavid/MLCryptoPredictor/blob/dev/data/external/Crypto_Historical_Prices/Images/BTC_Cnadlestick_chart.png)

**Figure 3**: BTC Candlestick chart for 2024.


![alt text](https://github.com/StamKavid/MLCryptoPredictor/blob/dev/data/external/Crypto_Historical_Prices/Images/correlation_adjusted_close_BTC_ETH.png)


**Figure 4**: Correlation Adjusted Close prices for BTC and ETH for 2018 - 2024.


## 🛠 __Tech Stack & Packages Used__

• __*Python*__

Primary language for scripting and analysis.

```
python == 3.10.7
```

• __*yfinance*__

For fetching historical market data.

```
yfinance == 0.2.37
```

• __*mplfinance*__

Matplotlib utilities for the visualization, and visual analysis, of financial data

```
mplfinance == 0.12.10b0
```

• __*Pandas*__

For data manipulation and analysis.

```
pandas == 2.2.1
```

• __*NumPy*__

For numerical computing.

```
numpy == 1.26.4
```

• __*Matplotlib/Seaborn*__

For data visualization.

```
matplotlib == 3.8.3
seaborn == 0.13.2
```

• __*Quantstats*__

For performance and risk statistics, and generating report sheets.

```
quantstats == 0.0.62
```

## 📚 __Data Sources__

Historical cryptocurrency data fetched from Yahoo Finance using the yfinance library.

## 📄 __License__

This project is open-sourced under the MIT License. Refer to the LICENSE file for more information.
