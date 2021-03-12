import pandas as pd
import numpy as np 
from sklearn.metrics import accuracy_score, precision_score, r2_score, recall_score
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
    


def get_model_errors(model, X, y):
    y_pred = model.predict(X)
    accuracy = accuracy_score(y, y_pred)
    precision = precision_score(y, y_pred)
    r2 = r2_score(y, y_pred)
    recall = recall_score(y_pred)
    return accuracy, precision, r2, recall

def 