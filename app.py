from flask import Flask, redirect, url_for, render_template, jsonify
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import os
import joblib
import json
import numpy as np
from sklearn.linear_model import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics
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

app = Flask(__name__, static_folder="./build", static_url_path="/")
CORS(app)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/api/features/<text>/<int:followers>/<int:friends>/<verified>')
def extractFeatures(text, followers, friends, verified):
    text = text.replace("-", " ")
    sentiment = 0.0
    entity_num = 0.0
    word_count = len(text.split())
    char_count = len(text)
    avg_word_len = char_count / word_count
    follower_count = float(followers)
    anger = 0.0
    disgust = 0.0
    fear = 0.0
    joy = 0.0
    sadness = 0.0
    is_quote = 0.0
    friends = float(friends)
    verified = 1.0 if verified == "true" else 0.0

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

    dict = {
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
            "is_quote": is_quote,
            "friends": friends,
            "verified": verified
        }
    return(jsonify(dict))

@app.route("/api/predict/<features>", methods = ['GET','POST'])
def makePrediction(features):
    features = json.loads(features.replace("-", " "))
    # make prediction and return favorites, retweets, and whatever data we need for visualization
    curdir = os.getcwd()
    retweet_model = joblib.load(curdir + "/machine-learning/models/retweet_model.joblib.pkl")
    favorites_model = joblib.load(curdir + "/machine-learning/models/favorites_model.joblib.pkl")

    # use this to make a prediction
    input_data = []
    input_data.append(features["sentiment"])
    input_data.append(features["entity_num"])
    input_data.append(features["word_count"])
    input_data.append(features["avg_word_len"])
    input_data.append(features["char_count"])
    input_data.append(features["anger"])
    input_data.append(features["disgust"])
    input_data.append(features["fear"])
    input_data.append(features["joy"])
    input_data.append(features["sadness"])
    input_data.append(features["is_quote"])
    input_data.append(features["follower_count"])
    input_data.append(features["friends"])
    input_data.append(features["verified"])

    input_data = np.array(input_data).reshape(1, -1)

    retweets = retweet_model.predict(input_data)
    favorites = favorites_model.predict(input_data)
    prediction = {"retweets": retweets[0, 0], "favorites": favorites[0, 0]}

    return(jsonify(prediction))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)