# import os
# from flask import Flask, render_template, session
# from wtforms import Form, BooleanField, StringField, PasswordField, validators
# from flask_sqlalchemy import SQLAlchemy

# ## Saves the file as the name of the main file ##
# ## __file__ --> geek_text.py ##
# basedir = os.path.abspath(os.path.dirname(__file__))

# app=Flask(__name__)

# ## Sets up the database location file
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

# ## if there is an update it wont track every change or modification
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)


# #########  MODELS #############

# class User(db.Model):

#     user_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Text)
#     email = db.Column(db.Text)
#     password = db.Column(db.Text)

#     def __init__(self,name,email,password):
#         self.name = name
#         self.email = email
#         self.password = password

# class Book(db.Model):

#     ISBN = db.Column(db.String(13), primary_key=True, unique=True, nullable=False)
#     title = db.Column(db.Text, nullable=False)
#     genre = db.Column(db.Text)
#     pubYear = db.Column(db.String(4))
#     price = db.Column(db.Numeric(10,2))
#     stock = db.Column(db.Integer)
#     pub_id = db.Column(db.Integer, db.ForeignKey('publisher.publisher_id'), nullable=False)
#     auth_id = db.Column(db.Integer, db.ForeignKey('author.author_id'), nullable=False)

# class Publisher(db.Model):

#     publisher_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Text, nullable=False)
#     address = db.Column(db.Text)
#     books = db.relationship('Book', backref='publisher', lazy=True)

#     def __init__(self, name, address):
#         self.name = name
#         self.address = address

# class Author(db.Model):

#     author_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Text, nullable=False)
#     books = db.relationship('Book', backref='author', lazy=True)

#     def __init__(self, name):
#         self.name = name

# ##############################

# @app.route('/')
# def homepage():
#     return render_template('layout.html')

# if __name__ == '__main__':
#     app.run(debug=True)
