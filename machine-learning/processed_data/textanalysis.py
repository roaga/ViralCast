import os
import json
import csv
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
natural_language_understanding.set_service_url(
    'https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/90774996-ec17-4440-b524-2c61f3a14481')


def process_rows(rows, writer):
    for row in rows:
        # Text to process
        text = row[0]

        # Initialied skipped tweets
        skipped_tweets = 0

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
        is_quote = 1 if row[1] else 0
        followers = row[4] if row[4] else 0
        friends = row[5] if row[5] else 0
        verified = 1 if row[6] else 0
        favorites = row[2] if row[2] else 0
        retweets = row[3] if row[3] else 0

        # IBM API Analysis
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
                sentiment_sum += entity['sentiment']['score'] * \
                    entity['relevance']
                entity_num += 1
                anger += entity['emotion']['anger'] * entity['relevance']
                disgust += entity['emotion']['disgust'] * \
                    entity['relevance']
                fear += entity['emotion']['fear'] * entity['relevance']
                joy += entity['emotion']['joy'] * entity['relevance']
                sadness += entity['emotion']['sadness'] * \
                    entity['relevance']

            sentiment = sentiment + sentiment_sum / 2
        except:
            skipped_tweets += 1
            continue
        
        # Create new row
        data = []
        data.append(sentiment)
        data.append(magnitude)
        data.append(entity_num)
        data.append(word_count)
        data.append(char_count)
        data.append(avg_word_len)
        data.append(anger)
        data.append(disgust)
        data.append(fear)
        data.append(joy)
        data.append(sadness)
        data.append(is_quote)
        data.append(followers)
        data.append(friends)
        data.append(verified)
        data.append(favorites)
        data.append(retweets)

        writer.writerow(data)
    