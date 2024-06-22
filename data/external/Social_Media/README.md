# 📊 Social Media Extraction (Twitter) Analysis 📉

## ℹ️ __Introduction__

In the era of big data and social media, Twitter has become a valuable source of real-time information and public sentiment. This folder focuses on extracting and analyzing Twitter data to gain insights into user behavior, sentiment trends, and engagement metrics. 

By leveraging Python libraries and natural language processing techniques, we aim to provide a comprehensive analysis of Twitter data from 2021-02-05 to 2023-03-05.

The core objectives include extracting tweets using specific keywords or hashtags, performing sentiment analysis on the collected tweets, and analyzing user engagement metrics such as unique users, follower counts, and tweet frequency over time.

## 🎯 __Project Objectives__

• __*Data Acquisition*__

Automate the extraction of tweets using the Kaggle Dataset, filtering by specific keywords or hashtags for BTC.


• __*Sentiment Analysis*_

Perform sentiment analysis on the collected tweets using pre-trained FinBert to categorize tweets as positive, negative, or neutral.

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
labels = ["positive", "negative", "neutral"]
# os.environ["TOKENIZERS_PARALLELISM"] = "false"

pipe = pipeline("text-classification", model= model, tokenizer= tokenizer)

def estimate_sentiment_single(news):
    if news:
        sentiment  = pipe(news)
        return sentiment[0]['label']
    else:
        return 'neutral'

print("Inserting sentiment")
```

• __*User and Engagement Metrics*_

Extract and analyze metrics such as unique users, follower counts, and tweet frequency.


• __*Data Visualization*_

Create visualizations to represent sentiment distribution, user engagement trends, and tweet frequency over time.
pythonCopyimport matplotlib.pyplot as plt

```python
# Sentiment distribution pie chart
sentiment_counts = tweets_data['sentiment'].value_counts()
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%')
plt.title('Sentiment Distribution')
plt.show()

# Tweet frequency over time
tweet_count_per_day.plot(kind='line')
plt.title('Tweet Frequency Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Tweets')
plt.show()
```

## 🛠 __Tech Stack & Packages Used__

• __*Python*__

Primary programming language for data extraction and analysis.

```
python == 3.10.7
```

• __*Pandas*__

For data manipulation and handling of time series.

```
pandas == 2.2.1
```

• __*Transformers*__

For the pre-trained FinBert model.

```
transformers == 4.33.2
```

• __*Matplotlib*__

For creating data visualizations.

```
matplotlib == 3.8.3
```

## 📚 __Data Sources__

The Twitter data is sourced directly from the Kaggle repository (https://www.kaggle.com/datasets/kaushiksuresh147/bitcoin-tweets), allowing for real-time extraction of tweets based on specified criteria.

## 📄 __License__

This project is open-source, licensed under the MIT License. See the LICENSE file for more details.