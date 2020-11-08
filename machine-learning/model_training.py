from sklearn.linear_model import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics
from matplotlib import pyplot as plt
import numpy as np
import csv
import joblib
import os


"""
Pre-process the data here
"""
path = os.path.join(os.getcwd(), "processed_data", "less_features.csv")
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
retweets_features_train, retweets_features_test, retweets_train, retweets_test = train_test_split(features, retweets)

# Favorites Data Split
favorites_features_train, favorites_features_test, favorites_train, favorites_test = train_test_split(features, favorites)
 # Algorithm 
retweet_linear_regression = Ridge(max_iter=10000)
favorites_linear_regression = Ridge(max_iter=10000)

retweet_linear_regression.fit(retweets_features_train, retweets_train)
favorites_linear_regression.fit(favorites_features_train, favorites_train)

retweets_pred = retweet_linear_regression.predict(retweets_features_test)
favorites_pred = favorites_linear_regression.predict(favorites_features_test)

r_square_retweets = metrics.r2_score(retweets_test, retweets_pred)
r_square_favorites = metrics.r2_score(favorites_test, favorites_pred)
print(r_square_retweets)
print(r_square_favorites)

retweet_dump = joblib.dump(retweet_linear_regression, "models/retweet_model.joblib,pkl", compress=9)
favorite_dump = joblib.dump(favorites_linear_regression, "models/favorites_model.joblib,pkl", compress=9)

