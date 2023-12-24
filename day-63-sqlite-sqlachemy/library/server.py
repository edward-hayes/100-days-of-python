from flask import request
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihCXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
Bootstrap(app)
db = SQLAlchemy(app)

class BookDB(db.Model):
    query: db.Query
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float)

class AddBook(FlaskForm):
    title = StringField(label="Book Name", validators=[DataRequired(), Length(min=0,max=250)])
    author = StringField(label="Book Author",validators=[DataRequired(), Length(min=0,max=250)])
    rating = DecimalField(label="Rating",places=2,rounding=None, validators=[DataRequired(), NumberRange(min=0,max=10)])
    submit = SubmitField('Add Book')

class EditBook(FlaskForm):
    rating = DecimalField(label="Rating",places=2,rounding=None, validators=[DataRequired(), NumberRange(min=0,max=10)])
    submit = SubmitField('Change Rating')

@app.route('/')
def home():
    all_books = db.session.query(BookDB).all()
    return render_template('index.html',all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    add_book_form = AddBook()
    if add_book_form.validate_on_submit():
        new_book = BookDB(
            title = add_book_form.data['title'],
            author = add_book_form.data['author'],
            rating = add_book_form.data['rating']
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=add_book_form)

@app.route('/edit/', methods=['GET', 'POST'])
def edit():
    id = request.args.get('id')
    book = BookDB.query.get(id)
    edit_book_form = EditBook()
    if edit_book_form.validate_on_submit():
        new_rating = edit_book_form.data['rating']
        book.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',book=book,form=edit_book_form)

@app.route('/delete')
def delete():
    id = request.args.get('id')
    book = BookDB.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)

