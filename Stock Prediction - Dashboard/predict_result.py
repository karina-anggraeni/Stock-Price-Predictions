import pandas as pd
import numpy as np 

def prediction_bbca():
    prediction_bbca = pd.read_csv('../Datasets/prediction_bbca.csv')
    prediction_bbca.drop(columns = ['Unnamed: 0'], axis = 1, inplace = True)
    prediction_bbca.columns = ['Price']
    return prediction_bbca['Price']

def prediction_bbri():
    prediction_bbri = pd.read_csv('../Datasets/prediction_bbri.csv')
    prediction_bbri.drop(columns = ['Unnamed: 0'], axis = 1, inplace = True)
    prediction_bbri.columns = ['Price']
    return prediction_bbri['Price']

def prediction_bnii():
    prediction_bnii = pd.read_csv('../Datasets/prediction_bnii.csv')
    prediction_bnii.drop(columns = ['Unnamed: 0'], axis = 1, inplace = True)
    prediction_bnii.columns = ['Price']
    return prediction_bnii['Price']

print(prediction_bbca().iloc[-1])
print(prediction_bbri().iloc[-1])
print(prediction_bnii().iloc[-1])