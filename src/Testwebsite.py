from flask import Flask
import time
from flask import render_template
from threading import Thread
import threading



profits = 100

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/sales')
def sales():
    return render_template("sales.html", profits=profits)

@app.route('/inventory')
def inventory():
    return render_template("inventory.html")

@app.route('/order')
def order():
    return render_template("order.html")

@app.route('/sales_inc')
def inc_sales():
    global profits
    profits += 100
    return render_template("sales.html",profits=profits)

def website_run():
    app.run(debug=True,host='0.0.0.0', port=5001, use_reloader=False)
    time.sleep(10)
    

if __name__ == "__main__":
    website_run()
