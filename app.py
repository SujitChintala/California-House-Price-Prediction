import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('regression_model.pkl', 'rb'))
polynomial_features = pickle.load(open('polynomial_features.pkl', 'rb'))
scaler = pickle.load(open('standard_scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    new_data = np.array(list(data.values())).reshape(1, -1)
    poly_data = polynomial_features.transform(new_data)
    scaler_data = scaler.transform(poly_data)
    pred = model.predict(scaler_data.reshape(1, -1))
    return jsonify(pred[0])

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    new_data = np.array(data).reshape(1, -1)
    poly_data = polynomial_features.transform(new_data)
    scaler_data = scaler.transform(poly_data)
    print(scaler_data)
    pred = model.predict(scaler_data.reshape(1, -1))[0]
    return render_template('home.html', prediction_text='The predicted house price is {}'.format(pred))
    
if __name__ == '__main__':
    app.run(debug=True)
    