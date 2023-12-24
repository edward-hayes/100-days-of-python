from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def name_card_website():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)