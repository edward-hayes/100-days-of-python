from flask import Flask, render_template
from post import Post


app = Flask(__name__)
post = Post()

@app.route('/')
def home():
    return render_template("index.html",posts=post.all_posts)

@app.route('/blog/<int:num>')
def blog(num):
    return render_template("post.html",num=num, posts=post.all_posts)

if __name__ == "__main__":
    app.run(debug=True)
