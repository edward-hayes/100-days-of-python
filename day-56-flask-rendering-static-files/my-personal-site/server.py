from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("day44-site/index.html")

if __name__ == "__main__":
    app.run(debug=True)