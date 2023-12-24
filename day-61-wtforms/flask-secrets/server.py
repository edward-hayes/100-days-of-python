from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap
import email_validator

class MyForm(FlaskForm):
    username = StringField(label='username', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')

app = Flask(__name__)
app.secret_key = ""
Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        email = form.username.data
        password = form.password.data
        if email == 'admin@email.com' and password == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    else:
        return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)