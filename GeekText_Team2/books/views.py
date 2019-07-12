from flask import Blueprint, render_template, redirect, url_for
from GeekText_Team2 import db
from GeekText_Team2.models import Book

books_blueprint = Blueprint('books', __name__, template_folder='templates/books')

@books_blueprint.route('/browse')
def list():
    #grab list of books from db
    books = Book.query.all()
    return render_template('list.html', books=books)

@books_blueprint.route('/browse/<ISBN>')
def details(ISBN):
    #grab book details
    books = Book.query.filter_by(ISBN=ISBN)
    return render_template('bookentry.html', ISBN=ISBN, books=books)

@books_blueprint.route('/browse/authors/<author>')
def author(author):
    #grab list of books based on author from db
    books = Book.query.filter_by(author=author)
    return render_template('list.html', author=author, books=books)
