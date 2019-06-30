# models.py under GeekText_Team2 folder
# IMPORT THE DATABASE
from GeekText_Team2 import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
##################################
from numpy import genfromtxt
from time import time
from datetime import datetime
from sqlalchemy import Column, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#############################################
############ DATABASE MODELS ################
#############################################


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(user_id)

############### USER MODEL #############################


class User(db.Model, UserMixin):

    __tablename__ = 'users'  # override tablename
    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(
        db.String(25), nullable=False, default='level_one_geeker.png')
    name = db.Column(db.Text)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, name, email, username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"This is {self.name} with email -> {self.email}"

########################################################

############### BOOK MODEL #############################


class Book(db.Model):

    __tablename__ = 'books'
    ISBN = db.Column(db.String(13), primary_key=True,
                     unique=True, nullable=True)
    title = db.Column(db.Text, nullable=False)
    author = db.Column(db.Text)
    genre = db.Column(db.Text)
    publication_year = db.Column(db.String(4))
    price = db.Column(db.Numeric(10, 2))
    stock = db.Column(db.Integer)
    description = db.Column(db.String(500))
    average_rating = db.Column(db.Float, nullable=False)
    ratings_count = db.Column(db.Integer, nullable=False)
    ratings_1 = db.Column(db.Integer)
    ratings_2 = db.Column(db.Integer)
    ratings_3 = db.Column(db.Integer)
    ratings_4 = db.Column(db.Integer)
    ratings_5 = db.Column(db.Integer)
    image_url = db.Column(db.Text)
    small_image_url = db.Column(db.Text)

    def __init__(self, title, author, genre, publication_year, price, stock, description, average_rating, ratings_count, ratings_1, ratings_2, ratings_3, ratings_4, ratings_5, image_url, small_image_url):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.price = price
        self.stock = stock
        self.description = description
        self.average_rating = average_rating
        self.ratings_count = ratings_count
        self.ratings_1 = ratings_1
        self.ratings_2 = ratings_2
        self.ratings_3 = ratings_3
        self.ratings_4 = ratings_4
        self.ratings_5 = ratings_5
        self.image_url = image_url
        self.small_image_url = small_image_url


############### PUBLISHER MODEL #############################
# class Publisher(db.Model):
#
#     __tablename__ = 'publisher'
#
#     publisher_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Text, nullable=False)
#     address = db.Column(db.Text)
#     books = db.relationship('Book', backref='publisher', lazy=True)
#
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address

############################################################


############### AUTHOR MODEL #############################
# class Author(db.Model):

 #   __tablename__ = 'author'

  #  author_id = db.Column(db.Integer, primary_key=True)
   # name = db.Column(db.Text, nullable=False)
    #books = db.relationship('Book', backref='author', lazy=True)

    # def __init__(self, name):
     #   self.name = name
############################################################
