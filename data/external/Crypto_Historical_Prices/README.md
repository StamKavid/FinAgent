
📈 Historical Crypto Data Analysis Using Yahoo Finance 📊
View the Crypto Data Analysis Report

ℹ️ Introduction
This repository is dedicated to the extraction and analysis of historical cryptocurrency data from Yahoo Finance, leveraging the yfinance Python library. The focus is on examining the price dynamics and market behavior of leading cryptocurrencies over time, utilizing statistical and machine learning techniques to uncover trends and patterns.

The initiative involves downloading historical price information, performing extensive exploratory data analysis (EDA), and applying quantitative analysis to understand the volatility and relationships between different cryptocurrencies.

🎯 Project Objectives
• Data Acquisition

Automate the retrieval of historical price data for various cryptocurrencies using the yfinance library.

python
Copy code
import yfinance as yf

# Example to fetch historical data for Bitcoin
btc_data = yf.download("BTC-USD", start="2018-01-01", end="2023-12-31")
• Data Preprocessing

Clean and preprocess the acquired data to ensure accuracy and reliability for further analysis.

• Exploratory Data Analysis (EDA)

Conduct an in-depth EDA to examine trends, correlations, and distribution characteristics of cryptocurrency data.

• Quantitative Analysis

Apply statistical models and machine learning algorithms to analyze and predict market movements.

• Visualization

Create comprehensive and interactive visualizations to represent the data insights clearly.

🛠 Tech Stack & Packages Used
• Python

Primary language for scripting and analysis.

makefile
Copy code
python == 3.10.7
• yfinance

For fetching historical market data.

makefile
Copy code
yfinance == 0.1.70
• Pandas

For data manipulation and analysis.

makefile
Copy code
pandas == 2.2.1
• NumPy

For numerical computing.

makefile
Copy code
numpy == 1.23.3
• Matplotlib/Seaborn

For data visualization.

makefile
Copy code
matplotlib == 3.8.3
seaborn == 0.12.0
• Quantstats

For performance and risk statistics, and generating report sheets.

makefile
Copy code
quantstats == 0.1.1
📚 Data Sources
Historical cryptocurrency data fetched from Yahoo Finance using the yfinance library.

📄 License
This project is open-sourced under the MIT License. Refer to the LICENSE file for more information.

📈 Analysis Insights
Focused on major cryptocurrencies like Bitcoin (BTC) and Ethereum (ETH) to track price changes and volatility since 2018.
Developed candlestick charts for detailed price movement analysis.
Constructed a correlation matrix to understand inter-relationships between different cryptocurrencies.
