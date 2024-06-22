# 📊 Cryptocurrency and Economic Analysis - External Features 📈


## 🌟 Overview

This folder is a comprehensive suite of tools and analyses focused on cryptocurrency markets, economic indicators, and social media sentiment. 
It combines data from various sources to provide in-depth insights into market trends, economic factors, and public sentiment surrounding cryptocurrencies, particularly Bitcoin.


## 🔍 Key Components

1. **Historical Crypto Data Analysis**
   - Uses Yahoo Finance data for cryptocurrencies like Bitcoin and Ethereum
   - Performs extensive Exploratory Data Analysis (EDA)
   - Creates visualizations including candlestick charts and correlation matrices

2. **Bitcoin Fear & Greed Index Analysis**
   - Scrapes data from Alternative.me API
   - Analyzes market sentiment and its correlation with price movements

3. **US Macro-economic Indices Analysis**
   - Utilizes FRED (Federal Reserve Economic Data) API
   - Focuses on time series analysis of macroeconomic variables
   - Includes data preprocessing, resampling, and decomposition

4. **Social Media (Twitter) Sentiment Analysis**
   - Analyzes Twitter data related to cryptocurrencies
   - Performs sentiment analysis using FinBert
   - Extracts user engagement metrics and visualizes trends

5. **Bitcoin Technical Indicator Analysis**
   - Computes 85 technical indicators using the 'ta' library
   - Creates comprehensive HTML reports using the 'dataprep' library


## 🛠️ Technologies and Libraries

- **Python**: Primary programming language (version 3.10.7)
- **Data Manipulation**: Pandas (2.2.1), NumPy (1.26.4)
- **Data Visualization**: Matplotlib (3.8.3), Seaborn (0.13.2), Plotly (5.20.0), mplfinance (0.12.10b0)
- **API Interactions**: yfinance (0.2.37), fredapi (0.5.1), requests (2.31.0)
- **Machine Learning & NLP**: Transformers (4.33.2), Statsmodels (0.14.1)
- **Technical Analysis**: ta (0.11.0)
- **Report Generation**: DataPrep (0.4.5), Quantstats (0.0.62)


## 📊 Data Sources

- Yahoo Finance (cryptocurrency historical data)
- Alternative.me API (Fear & Greed Index)
- FRED (Federal Reserve Economic Data)
- Kaggle dataset for Twitter data


## 🎯 Key Objectives

1. Automate data acquisition from various sources
2. Perform comprehensive data preprocessing and cleaning
3. Conduct in-depth exploratory data analysis
4. Apply advanced analytical techniques (e.g., sentiment analysis, technical indicators)
5. Generate insightful visualizations and reports


## 📈 Analysis Insights

- Tracks price changes and volatility of major cryptocurrencies since 2018
- Examines correlations between different cryptocurrencies
- Analyzes the impact of market sentiment on cryptocurrency prices
- Investigates the relationship between macroeconomic factors and crypto markets
- Provides sentiment analysis of social media discussions about cryptocurrencies


## 📄 License

This project is open-source and licensed under the MIT License. See the LICENSE file for more details.


## 🔗 Additional Resources

- [BTC - EDA Report](.\Technical_Indicators\Reports\btc_technical_analysis_report.html)
- [Economic Indicators (FRED) - EDA Report](.\FRED\Reports\FRED_EDA_Report.html)
- [Technical Analysis in Python Documentation](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html)
- [Fear & Greed Index Calculation](https://alternative.me/crypto/fear-and-greed-index/#api)