import csv

with open("tweets.csv", 'r') as r:
    reader = csv.reader(r)
    index_to_keep = [4, 9, 10, 11, 12, 17, 18, 20]

    with open('tweets_cleaned.csv', 'w') as w:
        writer = csv.writer(w)

        for line in reader:
            row = []
            for element in line:
                if line.index(element) in index_to_keep:
                    row.append(element)
            writer.writerow(row)
        