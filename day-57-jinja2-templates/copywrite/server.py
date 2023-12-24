from flask import Flask
from flask import render_template
import datetime as dt

app = Flask(__name__)

@app.route('/')
def home():
    year = dt.datetime.now().year
    print(year)
    return render_template("index.html", year=year)

@app.route('/guess/<name>')
def guess():
    ...

if __name__ == "__main__":
    app.run(debug=True)