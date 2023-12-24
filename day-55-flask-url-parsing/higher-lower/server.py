import random
from flask import Flask

app = Flask(__name__)

right_num = random.randint(1,10)
wrong_num = [i for i in range(1,11) if i !=right_num]

print(right_num)
print(wrong_num)


@app.route(f'/guess/<int:guess>')
def page_wrong(guess):
    page = '<h1 style="text-align: center color=red">Wrong!</h1>' \
        '<img src="https://media.giphy.com/media/14jl0GoiVQXQ5O/giphy.gif" width=400>'
    if guess in wrong_num:
        return page

@app.route(f'/guess/{right_num}')
def page_right():
    page = '<h1 style="text-align: center color=red">You got it!</h1>' \
            '<img src="https://media.giphy.com/media/l0HlFZ3c4NENSLQRi/giphy.gif" width=400>'
    return page

if __name__ == "__main__":
     app.run(debug=True)

