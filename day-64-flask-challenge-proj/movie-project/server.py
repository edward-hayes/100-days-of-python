from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, IntegerField, TextAreaField, RadioField
from wtforms.validators import DataRequired, Length, NumberRange, URL
from movie_database import Imdb

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-10-movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True

Bootstrap(app)
db = SQLAlchemy(app)
imdb = Imdb()

class Movies(db.Model):
    query: db.Query
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String)
    img_url = db.Column(db.String(250), nullable=False) 

class Review(FlaskForm):
    rating = DecimalField(label="Rating",places=2,rounding=None, validators=[DataRequired(), NumberRange(min=0,max=10)])
    review = TextAreaField(label="Review")
    submit = SubmitField('Add Movie')

class SearchMovie(FlaskForm):
    title = StringField(label="Title", validators=[DataRequired(), Length(min=0,max=250)])
    submit = SubmitField('Search Movie')

class EditMovie(FlaskForm):
    rating = DecimalField(label="Rating",places=2,rounding=None, validators=[DataRequired(), NumberRange(min=0,max=10)])
    review = TextAreaField(label="Review")
    submit = SubmitField('Update')

@app.route("/")
def home():
    movies = Movies.query.order_by(Movies.rating).all()
    for index in range(len(movies)):
        movies[index].ranking = len(movies) - index
    db.session.commit()
    return render_template("index.html", movies=movies)

@app.route("/add", methods=['GET', 'POST'])
def add():
    search_form = SearchMovie()
    if search_form.validate_on_submit():
        search_title = search_form.data['title']
        imdb.get_movies(search_title)
        return render_template("choose_photo.html",results=imdb.first_six_results)
    return render_template("add.html", form=search_form)

@app.route("/add/review", methods=['GET', 'POST'])
def review():
    id = request.args.get('id')
    review_form = Review()
    selected_movie = imdb.first_six_results[int(id)]
    if review_form.validate_on_submit():
        new_movie = Movies(
            title = selected_movie['title'],
            year = selected_movie['release_date'].split("-")[0],
            description = selected_movie['overview'],
            rating = review_form.data['rating'],
            ranking = 11,
            review = review_form.data['review'],
            img_url = f"https://image.tmdb.org/t/p/w500/{selected_movie['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("review.html",movie=selected_movie,form=review_form)
    


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    id = request.args.get('id')
    movie = db.session.query(Movies).get(id)
    edit_form = EditMovie()
    if edit_form.validate_on_submit():
        movie.rating = edit_form.data['rating']
        if edit_form.data['review']:
            movie.review = edit_form.data['review']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=edit_form)

@app.route("/delete")
def delete():
    id = request.args.get('id')
    movie = db.session.query(Movies).get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
