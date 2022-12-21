from flask import Flask, jsonify, render_template, redirect, request
import config
from utils import LaptopPrice
import numpy as np

app = Flask(__name__)
@app.route('/')
def man():
    return render_template('home.html')



@app.route('/predict', methods = ['GET','POST'])

def home():

    data = request.form

    print('data :', data)

    lap_price = LaptopPrice(data)
    price = lap_price.get_predicted_price()
    
    price = np.around(np.exp(price),0)
    #print("this ",price)

    return render_template('after.html', data=price)

    #return jsonify({"Price :": price})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5004)