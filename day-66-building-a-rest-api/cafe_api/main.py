from random import randint
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self,column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")

## HTTP GET - Read Record
@app.route("/random", methods=['GET'])
def random():
    num_rows = db.session.query(Cafe).count()
    query = db.session.query(Cafe).get(randint(1,num_rows))
# ---- Method 2 ----- #
    return jsonify(cafe=query.to_dict())

# --- Method 1 ---- #
    # rand_cafe = {
    #     "id": query.id,
    #     "name": query.name,
    #     "map_url": query.map_url,
    #     "img_url": query.img_url,
    #     "location": query.location,
    #     "seats": query.seats,
    #     "has_toilet": query.has_toilet,
    #     "has_wifi": query.has_wifi,
    #     "has_sockets": query.has_sockets,
    #     "can_take_calls": query.can_take_calls,
    #     "coffee_price": query.coffee_price
    # }
    # return jsonify(cafe=rand_cafe)

@app.route("/all")
def all():
    all_cafes = db.session.query(Cafe).all()
    cafe_list = [cafe.to_dict() for cafe in all_cafes]
    return jsonify(cafes = cafe_list)

@app.route("/search")
def search():
    location = request.args.get("loc")
    cafes_in_location = db.session.query(Cafe).filter_by(location=location)
    cafe_list = [cafe.to_dict() for cafe in cafes_in_location]
    if cafe_list:
        return jsonify(cafes = cafe_list)
    else:
        errors = {
            "Not Found": "Sorry, we don't have a cafe at that location."
        }
        return jsonify(error = errors)

## HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(    
        name = request.form.get('name'),
        map_url = request.form.get('map_url'),
        img_url = request.form.get('img_url'),
        location = request.form.get('location'),
        seats = request.form.get('seats'),
        has_toilet = bool(request.form.get('has_toilet')),
        has_wifi = bool(request.form.get('has_wifi')),
        has_sockets = bool(request.form.get('has_sockets')),
        can_take_calls = bool(request.form.get('can_take_calls')),
        coffee_price = request.form.get('cofee_price'),
    )
    try: 
        db.session.add(new_cafe)
        db.session.commit()
        message = {
            "success": "Succesfully added the new cafe"
        }
    except Exception as e:
        message = {
            "error": e
        }
    finally:
        return jsonify(response=message)

## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = request.args.get("new_price")
        db.session.commit()
        message = {
            "Success": "Succesfully updated the price"
        }
        response_code = 200
    else:
        message = {
            "Not Found": "Sorry a cafe with that id was not found in the database"
        }
        response_code = 404
    return jsonify(response = message), response_code

## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    api_key = request.args.get('api-key')
    if api_key == 'TopSecretAPIKey':
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            message = {
                "Success": "Cafe successfully deleted"
            }
            response_code = 200
        else:
            message = {
                "Not Found": "Sorry a cafe with that id was not found in the database"
            }
            response_code = 404
    else:
        message = {
            "error": "Sorry, that's not allowed. Make sure you have the correct api_key"
        }
        response_code = 403

    return jsonify(response = message), response_code

if __name__ == '__main__':
    app.run(debug=True)
