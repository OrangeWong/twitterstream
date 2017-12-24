# Twitter Sentiment Analysis

This is a programming assignment in Data Science at Scale at Coursere. 
The core concepts learnt are the cycle of appliying analysis on social media 
using Twitter as an example.

## Data Gathering via API
Use Python-OAuth2 library for accessing the Twitter API, and obtain some 
real-time tweets via streaming. The script is written in twitterstream.py.

## Tweet Sentiment
Use Python to perform a basic sentiment analysis on the streamed data. The sentiment
can be calculated by using the following commanrd: 
$ python tweet_sentiment.py AFINN-111.txt output.txt

## Sentiment for New Words
A simple Python script is written to assign the sentiment for new word that is not 
in AFINN-111.txt. The new sentiment is printed by using the following command:
$ python term_sentiment.py AFINN-111.txt output.txt

## Frequency of the Word in Tweets
A simple Python script is written to calculate the relative frequency of the word
in tweets. The relative frequency is calculated by the following commands:
$ python frequency.py output.txt

## The Happiest State
We rank the states by using the average sentiment in tweets. The following command
will print the happiest state and its sentiment.
$ python happiest_state.py AFINN-111.txt output.txt

## The Top Ten Hashtags
We can rank the hashtags and print out the first top ten hashtags in the output.txt
by the following command:
$ python top_ten.py output.txt

## tweets in MongoDB (tweets_in_mongodb.ipynb)
1. A MongoDB database is developed to store the tweets. Then, we perform the same sentiment anlysis by using pipeline in MongoDB. 
