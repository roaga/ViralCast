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

entities_response = natural_language_understanding.analyze(
    text="This is a test saying that I hate CNN, the worst network ever.",
    features=Features(entities=EntitiesOptions(sentiment=True, emotion=True))).get_result()
for entity in entities_response['entities']:
    print(entity['emotion'])

path = os.path.join(os.getcwd(), "tweets_cleaned.csv")

print(path)

with open(path, 'r') as csvinput:
    with open(os.path.join(os.getcwd(), "tweets_data_final.csv"), 'w') as csvoutput:
        reader = csv.reader(csvinput)
        writer = csv.writer(csvoutput, lineterminator='\n')

        all_data = []
        row = next(reader)
        row.append('Sentiment')
        row.append('Entity_Num')
        row.append('Word_Count')
        row.append('Avg_Word_Length')
        row.append('Character_Count')
        row.append("Anger")
        row.append("Digust")
        row.append("Fear")
        row.append("Joy")
        row.append("Sadness")

        all_data.append(row)

        skipped_tweets = 0

        for row in reader: 
            text = row[0]

            # Get analysis
            sentiment = 0.0
            magnitude = 0.0
            entity_num = 0.0
            word_count = len(text.split())
            char_count = len(text)
            avg_word_len = char_count / word_count
            anger = 0.0
            disgust = 0.0
            fear = 0.0
            joy = 0.0
            sadness = 0.0

            try:
                # sentiment analysis
                sentiment_response = natural_language_understanding.analyze(
                    text=text,
                    features=Features(sentiment=SentimentOptions())).get_result()
                sentiment = sentiment_response['sentiment']['document']['score']

                # entity analysis
                entities_response = natural_language_understanding.analyze(
                    text=text,
                    features=Features(entities=EntitiesOptions(sentiment=True, emotion=True))).get_result()
                sentiment_sum = 0
                for entity in entities_response['entities']:
                    sentiment_sum += entity['sentiment']['score'] * entity['relevance']
                    entity_num += 1
                    anger += entity['emotion']['anger'] * entity['relevance']
                    disgust += entity['emotion']['disgust'] * entity['relevance']
                    fear += entity['emotion']['fear'] * entity['relevance']
                    joy += entity['emotion']['joy'] * entity['relevance']
                    sadness += entity['emotion']['sadness'] * entity['relevance']

                sentiment = sentiment + sentiment_sum / 2
            except:
                skipped_tweets += 1

            # append that analysis
            row.append(sentiment)
            row.append(entity_num)
            row.append(word_count)
            row.append(avg_word_len)
            row.append(char_count)
            row.append(anger)
            row.append(disgust)
            row.append(fear)
            row.append(joy)
            row.append(sadness)

            all_data.append(row)

        writer.writerows(all_data)
        
        print(skipped_tweets + " tweets were unable to be analyzed and were ommited")