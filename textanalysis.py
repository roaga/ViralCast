import os
import csv
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions

path = "C:\Learning\HackRPI2020\HackRPI2020\data"
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

        # TODO: get analysis
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