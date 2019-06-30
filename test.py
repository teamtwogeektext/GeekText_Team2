from flask import render_template,request,Blueprint
from flask_login import login_required
from GeekText_Team2.models import Book
from GeekText_Team2 import db
from sqlalchemy import func

core = Blueprint('core',__name__)

books =[]
def QueryTester():
    book = Book.query.filter(Book.average_rating >= 4.7).limit(3).all()

    '''for b in book:
        print(b.title,' - ', b.author)'''

    return print(book[0].title, book[1].title, book[2].title)

QueryTester()
