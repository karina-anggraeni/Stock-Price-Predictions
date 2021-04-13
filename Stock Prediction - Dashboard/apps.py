from flask import Flask, render_template, request
import pickle
import pandas as pd
from dataset import compiled_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template ('home.html')

@app.route('/dataset')
def data():
    data = compiled_data()
    return render_template ('dataset.html', data = data)

@app.route('/plot')
def plot():
    return render_template ('plot.html')

@app.route('/prediction')
def prediction():
    return render_template ('prediction.html')

if __name__ == '__main__':
    app.run(debug=True,port=2000)