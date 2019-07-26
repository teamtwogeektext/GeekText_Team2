from flask import Blueprint, render_template, redirect, url_for, request
from GeekText_Team2 import db
from GeekText_Team2.models import Book
from sqlalchemy import desc

books_blueprint = Blueprint('books', __name__, template_folder='templates/books')


@books_blueprint.route('/books/all')
def list():
    sort_by = request.args.get('sort_by')

    books = Book.query.order_by(sort_by)

    return render_template('list.html', books=books)

@books_blueprint.route('/books/genre')
def genre():
    genre = request.args.get('genre')
    sort_by = request.args.get('sort_by')

    books = Book.query.filter_by(genre=genre).order_by(sort_by)

    return render_template(genre + '.html', books=books)

@books_blueprint.route('/books/best_rated')
def best_rated():

    books = Book.query.order_by(desc('average_rating')).limit(6).all()

    return render_template('best_rated.html', books=books)

@books_blueprint.route('/browse')
def browse():
    return render_template('browse.html')

# from sqlalchemy import desc
# Book.query.order_by(Book.price) #get all books ordered by price
# Book.query.order_by(desc(Book.price)) 