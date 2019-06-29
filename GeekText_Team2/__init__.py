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



###########################
#### BLUEPRINT CONFIGS #######
#########################

# Import these at the top if you want
# We've imported them here for easy reference
from GeekText_Team2.core.views import core
from GeekText_Team2.users.views import users
from GeekText_Team2.books.views import books_blueprint
#from GeekText_Team2.blog_posts.views import blog_posts
#from GeekText_Team2.error_pages.handlers import error_pages

# Register the apps
app.register_blueprint(users)
#app.register_blueprint(blog_posts)
app.register_blueprint(core)
#app.register_blueprint(error_pages)

app.register_blueprint(books_blueprint)


# from myproject.puppies.views import puppies_blueprint
# from myproject.owners.views import owners_blueprint

# app.register_blueprint(owners_blueprint,url_prefix='/owners')
# app.register_blueprint(puppies_blueprint,url_prefix='/puppies')
