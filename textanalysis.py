import os
import csv
import json
from dotenv import load_dotenv
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions, EntitiesOptions

load_dotenv()
IBM_CLOUD_KEY = os.getenv('IBM_CLOUD_KEY')

authenticator = IAMAuthenticator(IBM_CLOUD_KEY)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2020-08-01',
    authenticator=authenticator
)
natural_language_understanding.set_service_url('https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/90774996-ec17-4440-b524-2c61f3a14481')

curdir = os.getcwd()
path = curdir + '\data'
with open(path, 'r') as csvinput, open(path, 'w') as csvoutput:
    writer = csv.writer(csvoutput, lineterminator='\n')
    reader = csv.reader(csvinput)

    all = []
    row = next(reader)
    row.append('Sentiment')
    row.append('Entity_Num')
    row.append('Word_Count')
    all.append(row)

    for row in reader: 
        text = row[0];

        # get analysis
        sentiment = 0.0
        magnitude = 0.0
        entity_num = 0.0
        word_count = len(text.split())

        # sentiment analysis
        sentiment_response = natural_language_understanding.analyze(
            text=text,
            features=Features(sentiment=SentimentOptions())).get_result()
        sentiment = sentiment_response['sentiment']['document']['score']

        entities_response = natural_language_understanding.analyze(
            text=text,
            features=Features(entities=EntitiesOptions())).get_result()
        sentiment_sum = 0
        for entity in entities_response['entities']:
            sentiment_sum += entity['sentiment']['score']
            entity_num += 1

        sentiment = sentiment + sentiment_sum / 2

        # append that analysis
        row.append(sentiment)
        row.append(entity_num)
        row.append(word_count)
        all.append(row)

    writer.writerows(all)