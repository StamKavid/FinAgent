import os
import pandas as pd
import numpy as np
import polars as pl
import re
import swifter
from tqdm.auto import tqdm

# Visualization
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from plotly import graph_objs as go

# NLP
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from transformers import pipeline

# Dask
import dask.dataframe as dd
from dask.distributed import Client, LocalCluster

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from functools import lru_cache

# Set the display options to show the full text
pd.set_option('display.max_colwidth', None)


@lru_cache(maxsize=1000)
def load_stop_words():
    return set(stopwords.words('english'))

@lru_cache(maxsize=1000)
def load_lemmatizer():
    return WordNetLemmatizer()

def preprocess_tweet(tweet):
    # Compile regular expressions only once
    url_regex = re.compile(r'http\S+')
    username_regex = re.compile(r'@\w+')
    hashtag_regex = re.compile(r'#\w+')
    punctuation_regex = re.compile(r'[^\w\s]')

    # Remove URLs
    tweet = url_regex.sub('', tweet)
    
    # Remove usernames
    tweet = username_regex.sub('', tweet)
    
    # Remove hashtags
    tweet = hashtag_regex.sub('', tweet)
    
    # Remove punctuation
    tweet = punctuation_regex.sub('', tweet)
    
    # Convert to lowercase
    tweet = tweet.lower()
    
    # Tokenize the tweet
    tokens = word_tokenize(tweet)
    
    # Load stop words and lemmatizer only once
    stop_words = load_stop_words()
    lemmatizer = load_lemmatizer()
    
    # Remove stopwords
    tokens = [token for token in tokens if token not in stop_words]
    
    # Lemmatize the tokens
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Join the tokens back into a string
    tweet = ' '.join(tokens)
    
    return tweet

data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')

#Create a function to clean the tweets
def clean_text(text):
    text = re.sub(r'@[A-Za-z0–9]+', '', text) #Remove @mentions replace with blank
    text = re.sub(r'#', '', text) #Remove the ‘#’ symbol, replace with blank
    text = re.sub(r'RT[\s]+', '', text) #Removing RT, replace with blank
    text = re.sub(r'https?:\/\/\S+', '', text) #Remove the hyperlinks
    text = re.sub(r':', '', text) # Remove :
    return text

def deEmojify(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)

def sentiment_group_processing():
    # Load the data
    df = pl.read_csv(os.path.join(data_folder, r'Bitcoin_tweets.csv'), ignore_errors=True)
    df_2 = pl.read_csv(os.path.join(data_folder, r'Bitcoin_tweets_dataset_2.csv'), ignore_errors=True, ignore_errors=True)

    print("Data Load completed")

    # Concatenate the two dataframes
    df_concat_tweet = pd.concat([df.to_pandas(), df_2.to_pandas()], ignore_index=True)

    df_concat_tweet['date'] = pd.to_datetime(df_concat_tweet['date'], errors='coerce')
    df_concat_tweet['date'] = df_concat_tweet['date'].dt.strftime("%Y-%m-%d")
    df_concat_tweet = df_concat_tweet.dropna(subset=['date'])

    df_concat_tweet.dropna(axis=0 ,subset=['date','text'],inplace = True)
    df_concat_tweet.reset_index(drop= True,inplace=True)

    df_concat_tweet.drop_duplicates(inplace = True)
    df_concat_tweet.reset_index(drop=True,inplace=True)

    df_concat_tweet['clean_text'] = df_concat_tweet['text'].swifter.apply(preprocess_tweet)
    df_concat_tweet['text'] = df_concat_tweet['text'].swifter.progress_bar(True).apply(clean_text)
    df_concat_tweet['text'] = df_concat_tweet['text'].swifter.progress_bar(True).apply(deEmojify)


    ## Features for the model

    df_group = df_concat_tweet.copy()
    df_group = df_group.groupby('date').agg({'user_name': 'nunique', 'user_followers': 'sum', 'text' : 'count'}).reset_index()
    df_group.columns = ['date', 'unique_users', 'followers', 'tweet_count']

    # FinBERT
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

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

    df_concat_tweet['sentiment'] = df_concat_tweet['text'].swifter.apply(estimate_sentiment_single)

    return df_group, df_concat_tweet