import textanalysis
import concurrent.futures
import threading
import os
import csv

path = os.path.join(os.getcwd(), "data.csv")

with open(path, 'r') as csvinput:
    with open(os.path.join(os.getcwd(), "less_features.csv"), 'w') as csvoutput:
        rows = csv.reader(csvinput)
        writer = csv.writer(csvoutput, lineterminator='\n')

        # header = ["sentiment", "entity_num", "word_count",
        #           "avg_word_len", "char_count", "anger", "disgust", "fear", "joy", 
        #           "sadness", "is_quote", "followers", "friends", "verified",
        #           "retweets", "favorites"]

        for row in rows:
            row.pop(1)
            row.pop(2)
            row.pop(3)
            row.pop(4)
            writer.writerow(row)