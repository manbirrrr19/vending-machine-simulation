from flask import Flask
from flask import render_template

profits = 10

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

profits = 200

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5001)

