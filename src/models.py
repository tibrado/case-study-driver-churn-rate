import pandas as pd
import numpy as np 
from sklearn.metrics import accuracy_score, precision_score, r2_score, recall_score
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
    
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
import textwrap
from sklearn.ensemble import GradientBoostingClassifier


X_train, X_test, y_train, y_test = train_test_split(X, y)

# X is X_train, y is y_train
def get_model_errors(model, X, y):
    y_pred = model.predict(X)
    accuracy = accuracy_score(y, y_pred)
    precision = precision_score(y, y_pred)
    recall = recall_score(y, y_pred)
    return accuracy, precision, recall


def Gradient_Boosting_Regressor(X, y, learning_rate, n_estimators):
    # loss could be lad, huber, or quantile. default is ls
    model = GradientBoostingClassifier(learning_rate=learning_rate,   
                                  n_estimators=n_estimators,
                                  random_state=1)
    model.fit(X, y) 
    return model

grad_model = Gradient_Boosting_Regressor(X_train, y_train, 0.1, 100)
accuracy, precision, recall = get_model_errors(grad_model, X_train, y_train)


# returns R^2, MSE
def MSE_R2(model):
    R2 = cross_val_score(model, X_train, y_train).mean()
    MSE = abs(cross_val_score(model, X_train, y_train, scoring = 'neg_mean_squared_error').mean())
    return R2, MSE