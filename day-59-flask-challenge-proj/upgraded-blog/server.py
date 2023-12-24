from flask import Flask
from flask import render_template
from post import Post

app = Flask(__name__)

json = Post()
blog_posts = json.all_posts

@app.route('/')
def home():
    title = "My Blog"
    subtitle = "A collection of random musings"
    return render_template("index.html", title=title, subtitle=subtitle, posts=blog_posts)

@app.route('/post/<int:num>')
def post(num):
    blog_post = [blog_post for blog_post in blog_posts if blog_post['id'] == num][0]
    return render_template("post.html", blog_post = blog_post)

@app.route('/about')
def about():
    title = "About Me"
    return render_template("about.html",title=title)

@app.route('/contact')
def contact():
    title = "Contact Me"
    return render_template("contact.html", title=title)

if __name__ == "__main__":
    app.run(debug=True)