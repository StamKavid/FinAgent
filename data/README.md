# 📊 Cryptocurrency Data Processing - Summary 📈

## Overview

This folder focuses on processing and analyzing cryptocurrency data, particularly Bitcoin (BTC), along with various economic indicators and social media sentiment. 

It combines data from multiple sources to create a comprehensive dataset for analysis and machine learning purposes.

## Key Components

1. Data Acquisition and Preprocessing
2. Feature Engineering
3. Target Variable Creation
4. Data Merging and Consolidation

## Functionality

### 1. Data Acquisition and Preprocessing

- Loads data from various sources:
  - Yahoo Finance (cryptocurrency historical prices)
  - Fear and Greed Index
  - FRED (Federal Reserve Economic Data)
  - Technical Indicators
  - Social Media (Twitter) data
  - Raw cryptocurrency data
- Resampling of time series data to DATE 
- Handles missing values using backward fill (bfill) and linear interpolation
- Aligns all data sources to a common date range

### 2. Feature Engineering

- Calculates additional features:
  - Daily absolute price change
  - Daily returns percentage
  - Log difference of prices
- Computes local price extrema (minima and maxima) for various time windows

### 3. Target Variable Creation

- Creates target variables for potential predictive modeling:
  - Daily absolute change in adjusted closing price
  - Daily returns percentage
  - Log difference of adjusted closing price
- Identifies local price minima and maxima for different time windows

### 4. Data Merging and Consolidation

- Merges all processed datasets into a single comprehensive DataFrame
- Removes duplicate columns and renames for consistency
- Reorders columns for better organization

## Dependencies

- pandas
- numpy
- matplotlib
- scipy
- dotenv

## File Structure

- `data/`
  - `external/`: Contains data from external sources
  - `raw/`: Raw data files
  - `processed/`: Processed and consolidated data

## Output

The script generates a consolidated parquet file containing all processed data, ready for analysis or machine learning tasks.

## Note

Ensure all file paths are correctly set up before running the scripts. You may need to adjust paths based on your project structure.