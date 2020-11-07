import os
import csv

curdir = os.getcwd()
path = curdir + '\data'
with open(path, 'r') as csvinput, open(path, 'w') as csvoutput:
    writer = csv.writer(csvoutput, lineterminator='\n')
    reader = csv.reader(csvinput)

    all = []
    row = next(reader)
    row.append('Score')
    row.append('Magnitude')
    row.append('Embedding')
    row.append('Word_Count')
    all.append(row)

    for row in reader: 
        text = row[0];

        # TODO: get analytics
        score = 0.0
        magnitude = 0.0
        embedding = 0.0
        word_count = 0


        # append that analysis
        row.append(score)
        row.append(magnitude)
        row.append(embedding)
        row.append(word_count)
        all.append(row)

    writer.writerows(all)