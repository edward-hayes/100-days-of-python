from flask import Flask, render_template, request
from post import Post
from mailer import Email

app = Flask(__name__)
json = Post()
mail = Email()
blog_posts = json.all_posts
TO_ADDRESS = "hayesejh@gmail.com"

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

@app.route('/contact', methods=["GET","POST"])
def contact():
    if request.method =='POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        mail.send_msg(
            to_address=TO_ADDRESS,
            subject=f"{name} sent you a message",
            message=f"Name: {name}\nEmail: {email}\n\n{message}"
        )
        return render_template("feedback.html",title=f"Thanks, {name}")
    else:
        title = "Contact Me"
        return render_template("contact.html", title=title)

if __name__ == "__main__":
    app.run(debug=True)