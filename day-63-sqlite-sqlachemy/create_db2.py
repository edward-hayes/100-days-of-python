from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True


db = SQLAlchemy(app)

class Book(db.Model):
    query: db.Query
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float)

# ------------- CREATE DB ---------- #
#db.create_all()

# ------------- ADD Record ----------# 
# harry_potter = Book(title="Harry Potter", author="JK Rowling")
# db.session.add(harry_potter)
# db.session.commit()

# --------------- READ All Records ------------ #
all_books = db.session.query(Book).all()
print(all_books)

# --------------- READ A Particle Record By Query ------- #
book = Book.query.filter_by(title="Harry Potter").first()
print(book.title)

# --------  Update A Particular Record By Query ----- #
book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()  

#------  Update A Record By PRIMARY KEY --- #
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()  

#------ Delete A Particular Record By PRIMARY KEY ---- #
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()