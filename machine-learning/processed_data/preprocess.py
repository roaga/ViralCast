import textanalysis
import concurrent.futures
import threading
import os
import csv

path = os.path.join(os.getcwd(), "cleaned_tweets.csv")

with open(path, 'r') as csvinput:
    with open(os.path.join(os.getcwd(), "data.csv"), 'a') as csvoutput:
        rows = csv.reader(csvinput)
        writer = csv.writer(csvoutput, lineterminator='\n')
        # next(rows)

        # header = ["sentiment", "entity_num", "word_count",
        #           "avg_word_len", "char_count", "anger", "disgust", "fear", "joy", 
        #           "sadness", "is_quote", "followers", "friends", "verified",
        #           "retweets", "favorites"]

        textanalysis.process_rows(rows, writer)