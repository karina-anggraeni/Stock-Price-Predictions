import pandas as pd
import numpy as np 

def compiled_data():
    compiled_clean = pd.read_csv('../Datasets/compiled_clean.csv')
    compiled_clean.drop(columns = 'Unnamed: 0', axis = 1, inplace = True)
    compiled_clean = compiled_clean.sort_values('Date')
    return compiled_clean

def bbca():
    compiled_clean = pd.read_csv('../Datasets/compiled_clean.csv')
    compiled_clean.drop(columns = 'Unnamed: 0', axis = 1, inplace = True)
    bbca = compiled_clean[compiled_clean['Saham'] == 'BBCA'].sort_values('Date')
    return bbca

def mega():
    compiled_clean = pd.read_csv('../Datasets/compiled_clean.csv')
    compiled_clean.drop(columns = 'Unnamed: 0', axis = 1, inplace = True)
    mega = compiled_clean[compiled_clean['Saham'] == 'MEGA'].sort_values('Date')
    return mega

def bbri():
    compiled_clean = pd.read_csv('../Datasets/compiled_clean.csv')
    compiled_clean.drop(columns = 'Unnamed: 0', axis = 1, inplace = True)
    bbri = compiled_clean[compiled_clean['Saham'] == 'BBRI'].sort_values('Date')
    return bbri

def bmri():
    compiled_clean = pd.read_csv('../Datasets/compiled_clean.csv')
    compiled_clean.drop(columns = 'Unnamed: 0', axis = 1, inplace = True)
    bmri = compiled_clean[compiled_clean['Saham'] == 'BMRI'].sort_values('Date')
    return bmri

def sdra():
    compiled_clean = pd.read_csv('../Datasets/compiled_clean.csv')
    compiled_clean.drop(columns = 'Unnamed: 0', axis = 1, inplace = True)
    sdra = compiled_clean[compiled_clean['Saham'] == 'SDRA'].sort_values('Date')
    return sdra

def bnii():
    compiled_clean = pd.read_csv('../Datasets/compiled_clean.csv')
    compiled_clean.drop(columns = 'Unnamed: 0', axis = 1, inplace = True)
    bnii = compiled_clean[compiled_clean['Saham'] == 'BNII'].sort_values('Date')
    return bnii