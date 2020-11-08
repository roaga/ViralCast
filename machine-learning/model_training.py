from sklearn.linear_model import Ridge, LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from matplotlib import pyplot as plt
import numpy as np
import csv
import joblib
import os


"""
Pre-process the data here
"""
path = os.path.join(os.getcwd(), "processed_data", "data.csv")
with open(path, 'r') as csv_data:
    next(csv_data)
    data = np.loadtxt(csv_data, delimiter=',')

# print(data)

# Data organization
features = data[:, :-2]
retweets = data[:, -2].reshape(-1, 1)
favorites = data[:, -1].reshape(-1, 1)

# poly = PolynomialFeatures(degree=1, include_bias=True)
# features_poly = poly.fit_transform(features)

print(features.shape)
# print(retweets.shape)
# print(favorites.shape)

# Splitting train data and test data
# Retweets Data Split
retweets_features_train, retweets_features_test, retweets_train, retweets_test = train_test_split(
    features, retweets, test_size=0.2, shuffle=True
    )

# Favorites Data Split
favorites_features_train, favorites_features_test, favorites_train, favorites_test = train_test_split(
    features, favorites, test_size=0.2, shuffle=True
)

 # Algorithm 
retweet_linear_regression = LinearRegression(normalize=True)
favorites_linear_regression = LinearRegression(normalize=True)

retweet_linear_regression.fit(retweets_features_train, retweets_train)
favorites_linear_regression.fit(favorites_features_train, favorites_train)

retweets_pred = retweet_linear_regression.predict(retweets_features_test)
favorites_pred = favorites_linear_regression.predict(favorites_features_test)
print(retweets_pred - retweets_test)
print(favorites_pred - retweets_test)

retweet_dump = joblib.dump(retweet_linear_regression, "/models/retweet_model.joblib,pkl", compress=9)
favorite_dump = joblib.dump(favorites_linear_regression, "/models/favorites_model.joblib,pkl", compress=9)

retweets_score = retweet_linear_regression.score(retweets_features_test, retweets_test)
favorites_score = favorites_linear_regression.score(favorites_features_test, favorites_test)
# print("Retweets Score: " + str(retweets_score))
# print("Favorites Score: " + str(favorites_score))