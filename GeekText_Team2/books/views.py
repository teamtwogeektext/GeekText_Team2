from flask import Blueprint, render_template, redirect, url_for, request
from GeekText_Team2 import db
from GeekText_Team2.models import Book

books_blueprint = Blueprint('books', __name__, template_folder='templates/books')

@books_blueprint.route('/browse')
def list():
    books = Book.query.all()
    return render_template('list.html', books=books)

    
@books_blueprint.route('/browse/sortby/<string:sort_by>')
def book_sort(sort_by):
    books = Book.query.order_by(sort_by)
    
    return render_template('list.html', books=books)

@books_blueprint.route('/browse/genre')
def genre_filter():
    genre = request.args.get('genre')

    if genre == 'all':
        books = Book.query.all()
    else:
        books = Book.query.filter_by(genre=genre)

    return render_template('list.html', books=books)
