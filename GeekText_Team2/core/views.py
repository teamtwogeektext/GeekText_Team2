from flask import render_template, request, Blueprint
from flask_login import login_required
from GeekText_Team2.models import Book
from sqlalchemy import func


core = Blueprint('core', __name__)


@core.route('/')
def home():
    bestsellers = Book.query.filter(Book.average_rating >= 4.0).limit(4).all()
    b1 = bestsellers[0]
    b2 = bestsellers[1]
    b3 = bestsellers[2]
    b4 = bestsellers[3]
    return render_template('home.html', b1=b1, b2=b2, b3=b3, b4=b4)


@core.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')


@core.route('/info')
def info():
    '''
    Example view of any other "core" page. Such as a info page, about page,
    contact page. Any page that doesn't really sync with one of the models.
    '''
    return render_template('info.html')
