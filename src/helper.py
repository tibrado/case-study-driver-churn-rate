import pandas as pd
import numpy as np 
from sklearn.metrics import accuracy_score, precision_score, r2_score, recall_score

### ---------------------------------------------------------------
# Helpers 
### ---------------------------------------------------------------
# get data
def get_data(csv_file):
    data = pd.read_csv(csv_file)
    data.head()

    return data
    
# get data index 
def get_index():
    pass

# change to date 
def to_date(column):
    return pd.to_datetime(column)


def model():
    pass

def get_dummies(data, column):
    return pd.get_dummies(data, columns = column)
###
###
def data_clean(file):
    ''' Takes a raw data frame, cleans the data, and creates working columns
        that can be input into a model. 

        Parameters: file: path to data source

        Returns: X: data with dummy variables for categorical data, 
                    all clean data with no nan.
                 y: Target data - churn boolean
    '''
    data = get_data(file)
    
    data['last_trip_date'] = to_date(data['last_trip_date'])
    data['signup_date'] = to_date(data['signup_date'])

    # Create Churn Column
    thirty_days_ago = pd.to_datetime('2014-06-01') - pd.to_timedelta(30,unit='d')
    data['churn'] = pd.to_datetime(data['last_trip_date']) > thirty_days_ago
    
    # Create duymmy variables 
    data = get_dummies(data, ['city'])
    
    # Remap column 
    data = data.rename(columns = {'phone':'is_iphone'})
    data['is_iphone'] = data['is_iphone'].map(lambda phone: True if phone == 'iPhone' else False)
    # data['luxury_car_user'] = data['luxury_car_user'].map({True: 1, False: 0})

    # Change last trip and signup date to day and month 

    # Impute NaN to 0 
    data['avg_rating_by_driver'].fillna(0, inplace = True)
    data['avg_rating_of_driver'].fillna(0, inplace = True)

    # get day, month, year columns 

    data['last_trip_day'] = data['last_trip_date'].dt.day
    data['last_trip_month'] = data['last_trip_date'].dt.month


    data['signup_day'] = data['signup_date'].dt.day
    data['signup_month'] = data['signup_date'].dt.month
    data.drop(columns = ['last_trip_date', 'signup_date'], inplace=True)

    # Returns data and target
    return data.drop(columns = 'churn'), data['churn']




### TO DO
# 1. Cleaning/EDA

# What is the best way to stop or decrease churning 
###
'''
1. Cleaning/EDA
2. Model Creation
    a. RandomForest
    b. GradientBoosting
    c. LogisticRegression
3. Model Validation
    a. Error
4. Feature importance
'''