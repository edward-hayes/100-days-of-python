from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/goodbye')
def say_bye():
    return 'GoodBye'

if __name__ == "__main__":
    app.run()