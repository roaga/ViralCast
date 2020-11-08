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
            data = []
            data.append(row[2])
            data.append(row[3])
            data.append(row[4])
            data.append(row[11])
            data.append(row[14])
            data.append(row[15])

            writer.writerow(data)