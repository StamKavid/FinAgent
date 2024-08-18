# 📊Bitcoin Market Analysis (Technical Indicators) 📉

1) [View the Bitcoin Data Analysis Report](https://htmlpreview.github.io/?https://github.com/StamKavid/FinAgent/blob/main/data/external/Technical_Indicators/Reports/btc_technical_analysis_report.html)

2) [Technical Analysis in Python - Documentation](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.MFIIndicator)

## ℹ️ __Introduction__

With the increasing importance of cryptocurrencies in global markets, particularly Bitcoin, there is a need for robust data analysis tools and techniques to understand their market behaviors. This folder focuses on the extraction and analysis of Bitcoin data from Yahoo Finance, utilizing advanced technical indicators to provide in-depth insights into market trends.

The core objectives include scraping historical Bitcoin prices, computing various technical indicators, and preparing the data for comprehensive analysis. The use of the Python library '__ta__' for generating technical indicators and the '__dataprep__' library for creating detailed visual data reports are key components of this project.


## 🎯 __Project Objectives__


• __*Data Acquisition*__

Automate the extraction of historical Bitcoin data from Yahoo Finance using Python libraries.

```python
import yfinance as yf

# Define the ticker symbol
tickerSymbol = 'BTC-USD'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get historical prices for this ticker
btc_data = tickerData.history(period='1d', start= start_date, end= end_date)
```

• __*Technical Indicator Computation*__

Compute 85 technical indicators using the ta library (https://github.com/bukosabino/ta) to analyze Bitcoin's market dynamics. Indicators include Moving Average Convergence Divergence (MACD), Relative Strength Index (RSI), Money Flow Index (MFI), and Bollinger Bands.

```python
from ta import add_all_ta_features

# Add technical indicators
btc_data = add_all_ta_features(
    df=btc_data,
    open="Open", high="High", low="Low", close="Close", volume="Volume"
)
```

• __*Data Report Creation*__

Utilize the dataprep library (https://github.com/sfu-db/dataprep) to generate a comprehensive HTML report showcasing correlations, missing value analysis, statistical summaries, and various plots such as KDE, Box Plot, Q-Q Plot, and Histograms.

```python
from dataprep.eda import create_report

# Create an HTML data report
report = create_report(btc_data)
report.save(filename="Bitcoin_Analysis_Report.html")
```

## 🛠 __Tech Stack & Packages Used__

• __*Python*__

Primary programming language for data processing and analysis.

```
python == 3.10.7
```

• __*Pandas*__

For data manipulation and handling of time series.

```
pandas == 2.2.1
```

• __*ta*__

Python library for calculating technical indicators.

```
ta == 0.11.0
```

• __*yfinance*__

To access and interact with Yahoo Finance for financial data.

```
yfinance == 0.2.37
```

• __*DataPrep*__

For creating low-code data visualization reports.

```
dataprep == 0.4.5
```

## 📚 __Data Sources__

The Bitcoin data is sourced from Yahoo Finance, utilizing the yfinance library to scrape historical price information.

## 📄 __License__

This project is open-source, licensed under the MIT License. See the LICENSE file for more details.
