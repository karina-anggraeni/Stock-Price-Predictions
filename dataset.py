import pandas as pd
import numpy as np 

def compiled_data():
    compiled_clean = pd.read_csv('../compiled_clean.csv')
    compiled_clean.drop(columns = 'Unnamed: 0', axis = 1, inplace = True)
    compiled_clean = compiled_clean.sort_values('Date')
    return compiled_clean

# def bbca():
#     compiled_clean = pd.read_csv('../compiled_clean.csv')
#     compiled_clean.drop(columns = 'Unnamed: 0', axis = 1, inplace = True)
#     bbca = compiled_clean[compiled_clean['Saham'] == 'BBCA'].sort_values('Date')
#     return bbca