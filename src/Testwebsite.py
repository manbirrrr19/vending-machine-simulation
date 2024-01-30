from flask import Flask
from flask import render_template

profits = 10

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")



profits = 200

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5001)

