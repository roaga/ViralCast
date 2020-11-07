import csv
import os

path = os.path.join(os.getcwd(), "tweet_data.csv")
with open(path, 'r') as r:
    reader = csv.reader(r)
    index_to_keep = [4, 9, 10, 16, 17, 18, 20, 11, 12]

    with open('tweets_cleaned.csv', 'w') as w:
        writer = csv.writer(w)

        for line in reader:
            row = []
            for element in line:
                if line.index(element) in index_to_keep:
                    row.append(element)
            writer.writerow(row)
