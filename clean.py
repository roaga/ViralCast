import pandas as pd
import glob
path = r'C:\Learning\HackRPI2020\HackRPI2020\data'
all_files = glob.glob(path + "/*.csv")
li = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
frame = pd.concat(li, axis=0, ignore_index=True)

cols_to_drop = ['status_id', 'user_id', 'created_at','screen_name','source','reply_to_status_id'
,'reply_to_user_id','reply_to_screen_name','is_quote','is_retweet','country_code','place_full_name',
'place_type','friends_count','account_lang','account_created_at','verified','lang']

for col in cols_to_drop:
    del frame[col]
print(frame.shape)