from flask import Flask
import time
from flask import render_template
from threading import Thread
import threading

import random
import datetime
import json

num_sales_generated = 0
sales_file = 'sales_data.json'

# Generate sales_data.json randomly as placeholder before implementation with real sales data from payment.py
def load_sales_data():
    try:
        with open(sales_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_sales_data(sales_data):
    with open(sales_file, 'w') as f:
        json.dump(sales_data, f)

# Random generating sales
def generate_sales_data(num_sales):
    global num_sales_generated
    sales_data = load_sales_data()  # Load existing sales data
    for i in range(num_sales_generated, num_sales_generated + num_sales):
        timestamp = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 30))
        item = random.choice(['Coke', 'Sprite', 'Fanta', 'Green Tea', 'Milo', 'Pepsi'])
        price = 1.50
        sale = {'id': i, 'timestamp': str(timestamp), 'item': item, 'price': price}
        sales_data.append(sale)  # Append new sale to existing sales data
    save_sales_data(sales_data)  # Save updated sales data to file
    num_sales_generated += num_sales  # Update num_sales_generated
    return sales_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/inventory')
def inventory():
    return render_template("inventory.html")

@app.route('/order')
def order():
    return render_template("order.html")


@app.route('/sales')
def sales():
    global num_sales_generated  # Access the global variable
    num_sales_generated += 1  # Number of sales data entries to generate

    # Generate mock sales data dynamically
    num_sales = num_sales_generated
    sales_data = generate_sales_data(num_sales=num_sales)

    # Calculate profits 
    profits = round(calculate_profits(sales_data),2)
    return render_template('sales.html', profits=profits, sales_data=sales_data)


def calculate_profits(sales_data):
    # Example function to calculate profits from sales data
    total_profits = sum(sale['price'] for sale in sales_data)
    return total_profits


def website_run():
    app.run(debug=True,host='0.0.0.0', port=5001, use_reloader=False)
    time.sleep(10)
    

if __name__ == "__main__":
    website_run()