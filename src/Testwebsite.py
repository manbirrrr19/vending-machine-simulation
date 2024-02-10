from flask import Flask, render_template, request
import datetime
import json
import time

app = Flask(__name__)

sales_file = 'sales_data.json'

# Load sales data from file
def load_sales_data():
    try:
        with open(sales_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save sales data to file
def save_sales_data(sales_data):
    with open(sales_file, 'w') as f:
        json.dump(sales_data, f)

# Load stock data from file
def load_stock():
    try:
        with open('stock.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "coke": 10,
            "sprite": 10,
            "fanta": 10,
            "green_tea": 10,
            "milo": 10,
            "pepsi": 10
        }

# Save stock data to file
def save_stock(stock):
    with open('stock.json', 'w') as f:
        json.dump(stock, f)

# Update stock based on user selection
def test_update_stock(): 
    drinks = ["coke", "sprite", "fanta", "green_tea", "milo", "pepsi"]
    while True:
        print ("1.Coke \n 2.Sprite \n 3.Fanta \n 4.Green Tea \n 5.Milo \n 6.Pepsi")
        choice = int(input("Enter choice: ")) - 1
        if choice in range(6):
            selected_drink = drinks[choice]
            stock = load_stock()
            if stock[selected_drink] == 0:
                print("Sorry, we are out of stock for this drink. Please select another drink.")
                continue
            stock[selected_drink] -= 1
            save_stock(stock)
            return selected_drink

# Update sales data with new sale
def update_sales_data(selected_drink):
    sales_data = load_sales_data()
    timestamp = datetime.datetime.now()
    price = 1.50
    sale = {'id': len(sales_data), 'timestamp': str(timestamp), 'item': selected_drink, 'price': price}
    sales_data.append(sale)
    save_sales_data(sales_data)

# Calculate total profits from sales data
def calculate_profits(sales_data):
    return sum(sale['price'] for sale in sales_data)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/inventory')
def inventory():
    selected_drink = test_update_stock()
    update_sales_data(selected_drink)
    stock = load_stock()
    return render_template("inventory.html", stock=stock)

@app.route('/order')
def order():
    return render_template("order.html")

@app.route('/sales')
def sales():
    sales_data = load_sales_data()
    profits = round(calculate_profits(sales_data),2)
    return render_template("sales.html", sales_data=sales_data,profits=profits)

def website_run():
    app.run(debug=True,host='0.0.0.0', port=5001, use_reloader=False)
    time.sleep(10)

if __name__ == "__main__":
    website_run()