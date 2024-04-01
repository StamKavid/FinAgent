# 📈 __US Macro-economic Indices Using FRED Data__ 📊


## ℹ️ __Introduction__

Since the release of the FRED API, researchers and economists have gained unprecedented access to a wealth of economic data. This repository focuses on the systematic analysis of macroeconomic variables to understand their influence on economic indicators over time.

The core of this project is to preprocess the extensive datasets available in FRED and prepare them for time series analysis, which involves steps like data scraping via the API, resampling to different time frequencies, interpolation to fill missing values, and decomposition to identify trends and seasonal effects.


## 🎯 __Project Objectives__

• __*Data Acquisition*__

Automate the extraction of time series data from the FRED API, selecting relevant macroeconomic indicators as per the project's scope.


• __*Data Preprocessing*__

Implement methods to clean and standardize the raw data, making it suitable for analysis. This includes handling missing values, outliers, and anomalies.


• __*Time Series Decomposition*__

Break down the economic time series into trend, seasonal, and residual components to better understand the underlying patterns.


• __*Data Resampling and Interpolation*__

Modify the data's temporal resolution to match analysis needs and apply interpolation techniques to estimate missing data points.


• __*Exploratory Data Analysis (EDA)*__

Conduct thorough analysis to gain insights and understand the data's structure, distribution, and main characteristics.


## 🛠 __Tech Stack & Packages Used__

• __*Python*__

Primary programming language for data processing and analysis.

• __*Pandas*__

For data manipulation and handling of time series.

• __*Matplotlib/Plotly*__

For generating insightful visualizations of the data.

• __*Statsmodels*__

For time series decomposition and statistical analysis.

• __*FredAPI*__

To access and interact with the FRED API.

## 📚 __Data Sources__

All time series data used in this project are sourced from the FRED database, accessible through the FRED API.

## 📄 __License__

The project is open-source, licensed under the MIT License. See the LICENSE file for more details.
