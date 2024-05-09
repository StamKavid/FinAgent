# 📈 **Historical Crypto Data Analysis and Uncertainty Indices** 📊

## ℹ️ **Introduction**

This repository is dedicated to the extraction and analysis of historical cryptocurrency data (BTC Dominance, Market cap e.g.) along with global policy and world uncertainty indices. 
The focus is on examining various aspects of the cryptocurrency market alongside economic and policy uncertainty indicators to identify potential correlations and insights.

## 💡 **Analysis Insights**

• Analyzed BTC dominance compared to other cryptocurrencies sourced from CoinmarketCap.

• Incorporated Global Policy Uncertainty (GPR) data obtained from [Policy Uncertainty](https://www.policyuncertainty.com/gpr.html) to explore its potential impact on cryptocurrency markets.

• Studied crypto market capitalization and trading volume trends sourced from CoinmarketCap.

• Integrated World Trade Uncertainty Index (WTUI) and World Uncertainty Index (WUI) data from [World Uncertainty Index](https://worlduncertaintyindex.com/data/) to assess their relationship with cryptocurrency market dynamics.

## 🎯 **Project Objectives**

• **Data Acquisition**

Automate the retrieval of various datasets including BTC dominance, GPR data, crypto market cap, crypto volume data, WTUI data, and WUI data.

```python
# Example code for data acquisition using pandas
import pandas as pd

btc_dominance_data = pd.read_csv("btc_dominance_data.csv")
gpr_data = pd.read_csv("gpr_data.csv")
crypto_market_cap_data = pd.read_csv("crypto_market_cap_data.csv")
crypto_volume_data = pd.read_csv("crypto_volume_data.csv")
wtui_data = pd.read_csv("wtui_data.csv")
wui_data = pd.read_csv("wui_data.csv")

```
• **Data Preprocessing**

Clean and preprocess the acquired data to handle missing values, outliers, and ensure data consistency.

• **Exploratory Data Analysis (EDA)**

Conduct an in-depth EDA to analyze trends, correlations, and distribution characteristics of the cryptocurrency data alongside uncertainty indices.

## 🛠 __Tech Stack & Packages Used__

• Python

Primary language for scripting and analysis.

```
python == 3.10.7
```

• pandas

For data manipulation and analysis.

```
pandas == 2.2.1
```

• numpy

For numerical computing.

```
numpy == 1.26.4
```

• stationarizer

For stationarizing time series data.

```
stationarizer == 0.0.11
```

• missingno

For visualizing missing data.

```
missingno == 0.5.2
```

• scipy

For scientific computing and statistical analysis.

```
scipy == 1.12.0
```

## 📚 __Data Sources__

• Historical cryptocurrency data fetched from CoinmarketCap.

• Global Policy Uncertainty (GPR) data from Policy Uncertainty.

• World Trade Uncertainty Index (WTUI) and World Uncertainty Index (WUI) data from World Uncertainty Index.

## 📄 __License__

This project is open-sourced under the MIT License. Refer to the LICENSE file for more information.