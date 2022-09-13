import json
import pickle
from webbrowser import get
import numpy as np
__locations=None
__data_columns=None
__model=None

def get_location_names():
    __data_columns=json.load(open("columns.json",'r'))['data_columns']
    __locations=__data_columns[3:]
    return __locations

def get_estimated_price(location,sqft,bhk,bath):
    __model=pickle.load(open("banglore_home_prices_model.pickle",'rb'))
    try:
        loc_index=__data_columns.index(location=lower())
    except:
        loc_index=-1
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

def load_saved_artifacts():
    print("loading saved artifacts")
    global __locations
    global __data_columns

    __data_columns=json.load(open("columns.json",'r'))['data_columns']
    __locations=__data_columns[3:]

    global __model
    __model=pickle.load(open("banglore_home_prices_model.pickle",'rb'))

    print("Done loading artifacts")
    
if __name__=='__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price("1st Phase JP Nagar",1000,1,1))
