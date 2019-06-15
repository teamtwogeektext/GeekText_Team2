# models.py under GeekText_Team2 folder
# IMPORT THE DATABASE
from GeekText_Team2 import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

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
    ISBN = db.Column(db.String(13), primary_key=True, unique=True, nullable=False)
    title = db.Column(db.Text, nullable=False)
    genre = db.Column(db.Text)
    pubYear = db.Column(db.String(4))
    price = db.Column(db.Numeric(10,2))
    stock = db.Column(db.Integer)
    pub_id = db.Column(db.Integer, db.ForeignKey('publisher.publisher_id'), nullable=False)
    # auth_id = db.relationship(db.Integer,'Author', backref='Book', lazy=True)
    auth_id = db.Column(db.Integer, db.ForeignKey('author.author_id'), nullable=False)

    def __init__(self,title,genre,pubYear,price,stock,pub_id,auth_id):
        self.title = title
        self.genre = genre
        self.pubYear = pubYear
        self.price = price
        self.stock = stock
        self.pub_id = pub_id
        self.auth_id = auth_id


############### PUBLISHER MODEL #############################
class Publisher(db.Model):

    __tablename__ = 'publisher'

    publisher_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    address = db.Column(db.Text)
    books = db.relationship('Book', backref='publisher', lazy=True)

    def __init__(self, name, address):
        self.name = name
        self.address = address

############################################################


############### AUTHOR MODEL #############################
class Author(db.Model):

    __tablename__ = 'author'

    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

    def __init__(self, name):
        self.name = name
############################################################
