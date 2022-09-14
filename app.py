from flask import Flask, request, jsonify, render_template
import util
import pickle
import numpy as np
from collections.abc import Mapping
from collections.abc import MutableMapping
from collections.abc import Sequence
app=Flask(__name__)

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

@app.route('/')
def hello():
    return render_template("app.html")

@app.route('/get_location_names')
def get_location_names():
    response =jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price':get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
