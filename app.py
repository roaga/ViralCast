from flask import Flask, redirect, url_for, render_template
from dotenv import load_dotenv
import os
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

app = Flask(__name__)

@app.route('/')
def home():
    return "Test Body"

@app.route('/features/<text>/<int:followers>')
def extractFeatures(text, followers):
    sentiment = 0.0
    entity_num = 0.0
    word_count = len(text.split())
    char_count = len(text)
    avg_word_len = char_count / word_count
    follower_count = followers
    anger = 0.0
    disgust = 0.0
    fear = 0.0
    joy = 0.0
    sadness = 0.0
    is_quote = 0.0

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
        pass 

    return(
        {
            "sentiment": sentiment,
            "entity_num": entity_num,
            "word_count": word_count,
            "char_count": char_count,
            "avg_word_len": avg_word_len,
            "follower_count": follower_count,
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
            "is_quote": is_quote
        }
    )

if __name__ == "__main__":
    app.run()