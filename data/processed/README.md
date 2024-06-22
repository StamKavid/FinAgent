# Cryptocurrency Processed Data Generation

## Overview

This folder focuses on creating a comprehensive processed dataset for cryptocurrency analysis, particularly Bitcoin (BTC). 

It combines data from multiple sources and generates various technical indicators and target variables for potential predictive modeling.

## Key Components

1. Data Loading and Preprocessing
2. Feature Engineering
3. Target Variable Creation

## Functionality

### 1. Data Loading and Preprocessing

- Loads processed data from parquet files:
  - Bitcoin technical indicators
- Renames columns for consistency (replaces spaces with underscores)
- Handles missing values using forward fill (ffill)

### 2. Feature Engineering

- Calculates additional features based on the adjusted closing price:
  - Daily absolute change: `btc_daily_absolute_change`
  - Daily returns percentage: `btc_daily_returns_perc`
  - Log difference: `btc_log_difference`

### 3. Target Variable Creation

- Creates potential target variables for predictive modeling:
  - Local price minima and maxima for different time windows (7, 14, 21, 30, 60 days)
- Uses `scipy.signal._peak_finding._boolrelextrema` to identify local extrema

## Usage

1. Ensure the input parquet file `btc_technical_indicators.parquet.gzip` is in the correct directory.
2. Run the main function to generate the processed dataset.