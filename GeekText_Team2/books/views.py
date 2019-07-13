from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user,login_required
from GeekText_Team2 import db
from sqlalchemy import func
from GeekText_Team2.models import Book
from GeekText_Team2.models import BlogPost
from GeekText_Team2.blog_posts.forms import BlogPostForm
from GeekText_Team2.models import User

books_blueprint = Blueprint('books', __name__, template_folder='templates/books')

@books_blueprint.route('/browse')
def list():
    #grab list of books from db
    books = Book.query.all()
    return render_template('list.html', books=books)

@books_blueprint.route('/browse/<ISBN>', methods=['GET','POST'])
@login_required
def browse(ISBN):       #was named details
    #grab book details
    books = Book.query.filter_by(ISBN=ISBN)
    form = BlogPostForm()

    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
            # Returns an instance of the main page


    if form.validate_on_submit():
        rating = request.form.get("rating", None)
        true_private = request.form.get('true_private')
        blog_post = BlogPost(title=form.title.data,# must add here
                             text=form.text.data,
                             user_id=current_user.id,        # Must use the ID of the currently logged in user
                             rating = form.rating.data,
                             true_private = form.true_private.data
                             )
        db.session.add(blog_post)                           # Add changes to the database by creating a blog post
        db.session.commit()                                 # Confirming these changes
        flash("Blog Post Created")

        if true_private == 'true_private':
            blog_post = BlogPost(title=form.title.data,# must add here
                                 text=form.text.data,
                                 user_id= 'annonymous',        # Must use the ID of the currently logged in user
                                 rating = form.rating.data,
                                 true_private = form.true_private.data
                                 )
        db.session.add(blog_post)                           # Add changes to the database by creating a blog post
        db.session.commit()

        page = request.args.get('page', 1, type=int)
        blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
        # Returns an instance of the main page


    return render_template('bookentry.html', ISBN=ISBN, books=books,blog_posts=blog_posts, form = form, )

@books_blueprint.route('/browse/authors/<author>')
def author(author):
    #grab list of books based on author from db
    books = Book.query.filter_by(author=author)
    return render_template('list.html', author=author, books=books)
