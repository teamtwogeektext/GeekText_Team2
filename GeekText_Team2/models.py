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

    __tablename__ = 'users' #override tablename
    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(25), nullable=False,default='default_profile.png')
    name = db.Column(db.Text)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self,name,email,username,password):
        self.name = name
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"This is {self.name} with email -> {self.email}"

########################################################

############### BOOK MODEL #############################
class Book(db.Model):

    __tablename__ = 'books'
    id =db.Column(db.Integer, primary_key=True,unique=True,nullable=False, autoincrement=True)
    ISBN = db.Column(db.String(13),unique=False, nullable=True)
    stock = db.Column(db.Integer)
    author = db.Column(db.String(50))
    publication_year = db.Column(db.String(4))
    title = db.Column(db.Text, nullable=False)
    #genre = db.Column(db.Text)
    #price = db.Column(db.Numeric(10,2))

    #pub_id = db.Column(db.Integer), nullable=False)
    language_code = db.Column(db.String(10), nullable=False)

    #auth_id = db.Column(db.Integer, db.ForeignKey('author.author_id'), nullable=False)
    # AVERAGE OF 1-5
    average_rating = db.Column(db.Float, nullable=False)
    ratings_count = db.Column(db.Integer, nullable=False)
    #### TOTAL # OF EACH RATING ###
    rating_1 = db.Column(db.Integer)
    rating_2 = db.Column(db.Integer)
    rating_3 = db.Column(db.Integer)
    rating_4 = db.Column(db.Integer)
    rating_5 = db.Column(db.Integer)
    image_url = db.Column(db.String(150))
    small_image_url = db.Column(db.String(150))
    ###############################
        # auth_id = db.relationship(db.Integer,'Author', backref='Book', lazy=True)


    def __init__(self,ISBN,stock,author,publication_year,title,language_code,average_rating,ratings_count,rating_1,rating_2,rating_3,rating_4,rating_5,image_url,small_image_url):
        self.ISBN = ISBN
        self.stock = stock
        self.author = author
        self.publication_year = publication_year
        self.title = title
        self.language_code = language_code
        self.average_rating = average_rating
        self.ratings_count = ratings_count
        self.rating_1 = rating_1
        self.rating_2 = rating_2
        self.rating_3 = rating_3
        self.rating_4 = rating_4
        self.rating_5 = rating_5
        self.image_url = image_url
        self.small_image_url = small_image_url
        #self.price = price




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
class Author(db.Model):

    __tablename__ = 'author'

    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    #books = db.relationship('Book', backref='author', lazy=True)

    def __init__(self, name):
        self.name = name
############################################################
