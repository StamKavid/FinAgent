# 📈 __FinAgent: Multi-Agent AI for Bitcoin Analytics & Forecasting__ 📊

## __Introduction__

This repository showcases an AI multi-agent system designed for comprehensive cryptocurrency analysis, with a particular focus on Bitcoin (BTC), tailored for my MBA Dissertation Thesis. The system leverages artificial intelligence agents and machine learning models to extract, process, and analyze historical cryptocurrency data.

Our multi-agent framework consists of several specialized agents working in concert:

• **Financial Analyst Agent**: Collect and summarize recent news articles, press releases, and market analyses related to the cryptocurrency BTC and its industry.

• **Research Analyst Agent**: Conduct a thorough analysis of the cryptocurrency's financial health and market performance.

• **Investment Advisor Agent**: Review and synthesize the analyses provided by the Financial Analyst and the Research Analyst, combining these insights to form a comprehensive investment recommendation, by leveraging an AI model for price prediction.

At the core of our system is a sophisticated ML model, employed by the Investment Advisor Agent, which serves as a powerful tool for price prediction. This model is trained on historical data.

![image](https://github.com/user-attachments/assets/669a3ff8-89f1-4613-980d-a3ed4d73ba9e)



## 💡 __Analysis Insights__

• Focused on major cryptocurrencies like Bitcoin (BTC) and Ethereum (ETH) to track price changes and volatility since 2018.

• Developed candlestick charts for detailed price movement analysis.

• Constructed a correlation matrix to understand inter-relationships between different cryptocurrencies.

• Build up Tree-based model for Feature Selection.

• Build Time-Series model for BTC Price Prediction.

• Build AI multi-agent system for comprehensive BTC reporting.


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

• __*Investment Report Generation*__

The multi-agent approach allows for a more robust, efficient, and comprehensive analysis of cryptocurrency data, enabling us to uncover complex patterns and trends that might be missed by traditional single-model approaches.

![image](https://github.com/user-attachments/assets/2c99ca2f-d31c-403b-8b93-e574cb0a019d)


**Figure 5**: Output Report of Investment Advisor Agent.

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

• __*crewai*__

For multi-agent framework.

```
crewai == 0.35.8
```

## 📚 __Data Sources__

• **Yahoo Finance**: This provides historical data on crypto prices, ETFs, BTC ETFs, gold price etc.

• **Fear and Greed Index**: This index measures the fear and greed sentiment in the BTC market.

• **FRED (Federal Reserve Economic Data)**: This provides data related to GDP, CPI, Inflation rates, mostly for the US market.

• **Social media (Twitter-X)**: This refers to the number of tweets related to the BTC topic, derived from Kaggle.

• **Technical Indicators**: Includes 85 technical indicators to analyze Bitcoin’s market dynamics.

• **CoinMarketCap**: This provides data on different cryptocurrencies, including their market cap, volume, cryptocurrency dominance.

• **Global Policy Uncertainty (GPR)**: This provides data from Global Policy Uncertainty.

• **World Uncertainty Index (WUI)**: This provides data from the World Uncertainty Index.

## 📄 __License__ 

This project is open-sourced under the MIT License. Refer to the LICENSE file for more information.

