from flask import Blueprint, render_template, redirect, url_for
from GeekText_Team2 import db
from GeekText_Team2.models import Book

books_blueprint = Blueprint('books', __name__, template_folder='templates/books')

@books_blueprint.route('/browse')
def list():
    #grab list of books from db
    books = Book.query.all()
    return render_template('list.html', books=books)
