# __init__ underneath GeekText_Team2 folder
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

app=Flask(__name__)

app.config['SECRET_KEY']='mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'geektext.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

login_manager.init_app(app)

login_manager.login_view = "login"

from GeekText_Team2 import models

# from myproject.puppies.views import puppies_blueprint
# from myproject.owners.views import owners_blueprint

# app.register_blueprint(owners_blueprint,url_prefix='/owners')
# app.register_blueprint(puppies_blueprint,url_prefix='/puppies')