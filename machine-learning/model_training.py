from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as pyplot
import numpy as np
import csv
import joblib
import os


"""
Pre-process the data here
"""
path = os.path.join(os.getcwd(), "processed_data/tweet_data.csv")
with open(path, 'r') as csv_data:
    data = np.loadtxt(csv_data, delimiter=',')

# Data organization
features = np.random.randint(2, 200, (500, 10))
retweets = np.random.randint(2, 200, (500, 1))
favorites = np.random.randint(2, 200, (500, 1))

# Splitting train data and test data
# Retweets Data Split
retweet_features_train, retweet_features_test, retweets_train, retweets_test = train_test_split(
    features, retweets, test_size=0.2, shuffle=True)

# Favorites Data Split
favorites_features_train, favorite_features_test, favorites_train, favorites_test = train_test_split(
    features, favorites, test_size=0.2, shuffle=True
)

# Algorithm 
# ridge_regression = Ridge()
# fit_model = ridge_regression.fit(X_train, y_train)

# print(fit_model.coef_)
# print(fit_model.intercept_)
# print(fit_model.predict(X_test))

# model_predictions = fit_model.predict(X_test)
# accuracy = np.count_nonzero(y_train == model_predictions)
# print(accuracy)