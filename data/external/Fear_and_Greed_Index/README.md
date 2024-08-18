# 📊Bitcoin Fear & Greed Index Analysis 📉


[Learn about how the Fear & Greed Index is Calculated](https://alternative.me/crypto/fear-and-greed-index/#api)

## ℹ️ __Introduction__

The Fear and Greed Index for Bitcoin (BTC) is a popular metric used to gauge the market's emotional sentiment towards cryptocurrency. This folder is dedicated to scrapping the Fear and Greed Index data from the Alternative.me API and analyzing it to understand how market sentiments correlate with price movements of Bitcoin.

The project employs Python for data scraping, handling, and saving the data into a CSV format, enabling further analysis on how the sentiments change over time and how they might influence market behavior.

<p align="center">
  <img src="https://github.com/StamKavid/MLCryptoPredictor/blob/dev/data/external/Fear_and_Greed_Index/Images/fear-and-greed-index.png" alt="alt text">
</p>

**Figure 1**: BTC Fear and Greed Index for 12 April 2024.

## 🎯 __Project Objectives__


• __*Data Acquisition*__

Automatically retrieve the Fear and Greed Index for Bitcoin using the provided API and Python scripting.

```python
# Importing necessary libraries
import pandas as pd
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def fetch_fear_and_greed_index():
    # Base URL for the Fear and Greed Index API
    base_url = "https://api.alternative.me/fng/?limit=0"
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []
```

• __*Data Processing*__

Extract, transform, and save the retrieved data into a CSV file for ease of analysis, focusing on entries since the user-specified start date.

```python
def save_to_csv(data, filename, start_date):
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df = df[df['timestamp'] >= start_date]
    df.to_csv(filename, index=False)
    print(f"Data successfully saved to {filename}")
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

• __*Requests*__

To perform HTTP requests to the API.

```
requests == 2.31.0
```

## 📚 __Data Sources__

Data is sourced directly from the Alternative.me API, which provides the Fear and Greed Index.

## 📄 __License__

This project is open-source, licensed under the MIT License. See the LICENSE file for more details.
