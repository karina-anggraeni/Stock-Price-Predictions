from flask import Flask, render_template, request
import pandas as pd
from dataset import compiled_data, bbca, mega, bbri, bmri, sdra, bnii
from predict_result import prediction_bbca, prediction_bbri, prediction_bnii

app = Flask(__name__)

@app.route('/')
def home():
    return render_template ('home.html')

@app.route('/dataset')
def data():
    data = compiled_data()
    return render_template ('dataset.html', data = data)

@app.route('/bbca')
def bbca_data():
    data = bbca()
    return render_template ('bbca.html', data = data)

@app.route('/mega')
def mega_data():
    data = mega()
    return render_template ('mega.html', data = data)

@app.route('/bbri')
def bbri_data():
    data = bbri()
    return render_template ('bbri.html', data = data)

@app.route('/bmri')
def bmri_data():
    data = bmri()
    return render_template ('bmri.html', data = data)

@app.route('/sdra')
def sdra_data():
    data = sdra()
    return render_template ('sdra.html', data = data)

@app.route('/bnii')
def bnii_data():
    data = bnii()
    return render_template ('bnii.html', data = data)

@app.route('/plot')
def plot():
    return render_template ('plot.html')

@app.route('/prediction_bbca', methods = ['GET', 'POST'])
def predict_bbca():
    return render_template ('prediction_bbca.html')

@app.route('/result_bbca', methods = ['GET', 'POST'])
def result_bbca():
    if request.method == 'POST':
        user = request.form

        buy_price = int(user['Buy'])
        days = int(user['Days'])
        predict_price = prediction_bbca().iloc[days - 1]
        return_ratio = round((predict_price - buy_price)/ buy_price, 3)

        return render_template ('result_bbca.html', data = user, predict_price = predict_price, return_ratio = return_ratio)

@app.route('/prediction_bbri', methods = ['GET', 'POST'])
def predict_bbri():
    return render_template ('prediction_bbri.html')

@app.route('/result_bbri', methods = ['GET', 'POST'])
def result_bbri():
    if request.method == 'POST':
        user = request.form

        buy_price = int(user['Buy'])
        days = int(user['Days'])
        predict_price = prediction_bbri().iloc[days - 1]
        return_ratio = round((predict_price - buy_price)/ buy_price, 3)

        return render_template ('result_bbri.html', data = user, predict_price = predict_price, return_ratio = return_ratio)

@app.route('/prediction_bnii', methods = ['GET', 'POST'])
def predict_bnii():
    return render_template ('prediction_bnii.html')

@app.route('/result_bnii', methods = ['GET', 'POST'])
def result_bnii():
    if request.method == 'POST':
        user = request.form

        buy_price = int(user['Buy'])
        days = int(user['Days'])
        predict_price = prediction_bnii().iloc[days - 1]
        return_ratio = round((predict_price - buy_price)/ buy_price, 3)

        return render_template ('result_bnii.html', data = user, predict_price = predict_price, return_ratio = return_ratio)

if __name__ == '__main__':
    app.run(debug = True, port = 2000)