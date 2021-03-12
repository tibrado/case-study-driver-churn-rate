import pandas as pd
import numpy as np 
from sklearn.metrics import accuracy_score, precision_score, r2_score, recall_score
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
    
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
import textwrap

def get_model_errors(model, X, y):
    y_pred = model.predict(X)
    accuracy = accuracy_score(y, y_pred)
    precision = precision_score(y, y_pred)
    r2 = r2_score(y, y_pred)
    recall = recall_score(y, y_pred)
    return accuracy, precision, r2, recall


def Gradient_Boosting_Regressor(X, y):
    X.drop(columns=['signup_month', 'signup_year'], inplace=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    model = GradientBoostingRegressor(learning_rate=0.1,
                                  loss='ls',
                                  n_estimators=100,
                                  random_state=1)
    model.fit(X_train, y_train)

# returns R^2, MSE
def MSE_R2(model):
    R2 = cross_val_score(model, X_train, y_train).mean()
    MSE = abs(cross_val_score(model, X_train, y_train, scoring = 'neg_mean_squared_error').mean())
    return R2, MSE