from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': 9218309183 ,'price': 200},
        {'id': 2, 'name': 'Laptop', 'barcode': 3217983198 ,'price': 600},
        {'id': 3, 'name': 'Keyboard', 'barcode': 8372198321 ,'price': 20}
    ]
    return render_template('market.html', items=items)