from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as pyplot
import numpy as np
import csv
import joblib

# To-do: Import cleaned data and turn into numpy arrays
X = np.random.rand(100, 50)
y = np.random.rand(100,1)

# Splitting train data and test data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, shuffle=True)

# Algorithm 
ridge_regression = Ridge()
fit_model = ridge_regression.fit(X_train, y_train)

print(fit_model.coef_)
print(fit_model.intercept_)
print(fit_model.predict(X_test))

model_predictions = fit_model.predict(X_test)
accuracy = np.count_nonzero(y_train == model_predictions)
print(accuracy)