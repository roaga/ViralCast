from os import curdir
import pandas as pd
import os

df = pd.read_csv('tweet_data.csv')

cols_to_drop = ['status_id', 'user_id', 'created_at','screen_name','source','reply_to_status_id'
,'reply_to_user_id','reply_to_screen_name','is_retweet','country_code','place_full_name',
'place_type','account_lang','account_created_at','lang']

for col in cols_to_drop:
    df.drop(col, axis=1, inplace=True)

df = df[:100]
df.to_csv('cleaned_tweets.csv', index=False)
