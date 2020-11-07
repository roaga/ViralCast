import pandas as pd
df = pd.read_csv('2020-04-16 Coronavirus Tweets.csv')
cols_to_drop = ['status_id', 'user_id', 'created_at','screen_name','source','reply_to_status_id'
,'reply_to_user_id','reply_to_screen_name','is_quote','is_retweet','country_code','place_full_name',
'place_type','friends_count','account_lang','account_created_at','verified','lang']

for col in cols_to_drop:
    del df[col]
print(df.shape)