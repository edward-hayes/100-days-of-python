from flask import Flask
app = Flask(__name__)

def bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function

def italic(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function

def underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"

@app.route('/hello')
@bold
@italic
def hello():
    return "Hello, World"


@app.route("/username/<name>")
def greet(name):
    return '<h1 style="text-align: center">Hello, World!</h1>' \
            '<p>This is a paragraph </p>' \
            '<img src="https://media.giphy.com/media/14jl0GoiVQXQ5O/giphy.gif" width=400>'

if __name__ == "__main__":
     app.run(debug=True)