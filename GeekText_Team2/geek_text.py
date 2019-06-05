import os
from flask import Flask, render_template, session
from wtforms import Form, BooleanField, StringField, validators
from flask_sqlalchemy import SQLAlchemy

## Saves the file as the name of the main file ##
## __file__ --> geek_text.py ##
basedir = os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)

## Sets up the database location file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

## if there is an update it wont track every change or modification
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):

    __tablename__ = 'Users' #override tablename
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    password = db.Column(db.Text)

    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password

@app.route('/')
def homepage():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(debug=True)