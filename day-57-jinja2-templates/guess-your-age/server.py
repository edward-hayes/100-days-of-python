from flask import Flask
from flask import render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/guess/<name>')
def guess(name):

    params = {
        "name": name
    }
    age_url = "https://api.agify.io/"
    gender_url = "https://api.genderize.io"

    age_response = requests.get(url=age_url,params=params)
    age = age_response.json()['age']

    gender_response = requests.get(url=gender_url,params=params)
    gender = gender_response.json()['gender']

    return render_template("guess.html", name=name.title(), gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)