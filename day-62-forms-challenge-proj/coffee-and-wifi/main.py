from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
Bootstrap(app)

def choices(character,amount):
    return [(character*(num)) for num in range(1,amount+1)]

coffee_choices = choices("☕️",5)
wifi_choices = choices("💪",5)
power_choices = choices("🔌",5)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe Location on Google Maps (URL)',validators=[DataRequired(),URL()])
    open_time = StringField(label="Open Time e.g. 8AM", validators=[DataRequired()])
    closing_time = StringField(label="Closing Time e.g. 8AM", validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', choices=coffee_choices,validators=[DataRequired()])
    wifi_rating = SelectField(label='Wifi Strength Rating', choices=wifi_choices,validators=[DataRequired()])
    power_rating = SelectField(label='Power Socket Availability', choices=power_choices,validators=[DataRequired()]) 
    submit = SubmitField('Submit')

# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print(form.data.keys())
        with open('cafe-data.csv','a') as csv_file:
            new_row = csv.DictWriter(csv_file,fieldnames=form.data.keys())
            new_row.writerow(form.data)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
