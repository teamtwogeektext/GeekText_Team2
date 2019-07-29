from flask import Blueprint, flash, request, render_template, redirect, url_for
from GeekText_Team2 import db
from GeekText_Team2.models import Wishlist, Wishlist2, Wishlist3, Wishlist1, Address, Book, User
from GeekText_Team2.Wishlist.forms import wishlistPostForm
from GeekText_Team2.users.views import current_user

wishlist_posts = Blueprint('wishlist_posts', __name__,
                           template_folder='templates/wishlist')


# @wishlist_posts.route('/create', methods=['GET', 'POST'])
# # @login_required
# def create_wish():

#     form = wishlistPostForm()

# 	if form.validate_on_submit():
# 		 wishlist_post = Wishlist(
# 		 	title=form.title.data,
# 		 	user_id=current_user.id,

# 		 						)
# 		 db.session.add(wishlist_post)
# 		 db.session.commit()
# 		 flash('Wishlist created')
# 		 return redirect(url_for('wishlist_posts.viewallw'))
# 		 # redirect(url_for('Wishlist_posts.list', wishlist_post_id= wishlist_post.id))

#     return render_template('addWish.html', form=form)


@wishlist_posts.route('/delete', methods=['GET'])
def delete():

    item = Wishlist.query.filter_by(
        title="h", user_id=current_user.id, ISBN=request.args.get('ISBN')).first()

    db.session.delete(item)
    db.session.commit()
    flash('Wishlist post Deleted')
    return redirect(url_for('wishlist_posts.viewallw'))


@wishlist_posts.route('/delete1', methods=['GET'])
def delete1():

    item = Wishlist1.query.filter_by(
        title="h", user_id=current_user.id, ISBN=request.args.get('ISBN')).first()

    db.session.delete(item)
    db.session.commit()
    flash('Wishlist post Deleted')
    return redirect(url_for('wishlist_posts.viewallw'))


@wishlist_posts.route('/delete2', methods=['GET'])
def delete2():

    item = Wishlist2.query.filter_by(
        title="h", user_id=current_user.id, ISBN=request.args.get('ISBN')).first()

    db.session.delete(item)
    db.session.commit()
    flash('Wishlist post Deleted')
    return redirect(url_for('wishlist_posts.viewallw'))


@wishlist_posts.route('/delete3', methods=['GET'])
def delete3():

    item = Wishlist3.query.filter_by(
        title="h", user_id=current_user.id, ISBN=request.args.get('ISBN')).first()

    db.session.delete(item)
    db.session.commit()
    flash('Wishlist post Deleted')
    return redirect(url_for('wishlist_posts.viewallw'))


@wishlist_posts.route('/viewall')
def viewallw():
    wishlist_post = Wishlist.query.all()
    items = Book.query.join(Wishlist).filter_by(user_id=current_user.id)
    items1 = Book.query.join(Wishlist1).filter_by(user_id=current_user.id)
    items2 = Book.query.join(Wishlist2).filter_by(user_id=current_user.id)
    items3 = Book.query.join(Wishlist3).filter_by(user_id=current_user.id)
    return render_template('wlist.html', wishlist=wishlist_post, items=items, items1=items1, items2=items2, items3=items3)


@wishlist_posts.route("/addtowishlist", methods=['GET', 'POST'])
def addtowishlist():

    bookId = request.args.get('ISBN')
    item = Wishlist(title="h", user_id=current_user.id, ISBN=bookId)
    db.session.add(item)
    db.session.commit()
    flash('Book added to your wishlist')

    return redirect(url_for('books.list'))


@wishlist_posts.route("/addtowishlist2", methods=['GET', 'POST'])
def addtowishlist2():

    bookId = request.args.get('ISBN')
    item = Wishlist2(title="h", user_id=current_user.id, ISBN=bookId)
    db.session.add(item)
    db.session.commit()
    flash('Book added to your wishlist')

    return redirect(url_for('books.list'))


@wishlist_posts.route("/addtowishlist1", methods=['GET', 'POST'])
def addtowishlist1():

    bookId = request.args.get('ISBN')
    item = Wishlist1(title="h", user_id=current_user.id, ISBN=bookId)
    db.session.add(item)
    db.session.commit()
    flash('Book added to your wishlist')

    return redirect(url_for('books.list'))


@wishlist_posts.route("/addtowishlist3", methods=['GET', 'POST'])
def addtowishlist3():

    bookId = request.args.get('ISBN')
    item = Wishlist3(title="h", user_id=current_user.id, ISBN=bookId)
    db.session.add(item)
    db.session.commit()
    flash('Book added to your wishlist')

    return redirect(url_for('books.list'))


@wishlist_posts.route("/addtowhichlist", methods=['GET', 'POST'])
def addtowhichlist():

    bookId = request.args.get('ISBN')
    item = Wishlist(title="h", user_id=current_user.id, ISBN=bookId)
    db.session.add(item)
    db.session.commit()
    flash('Book added to your wishlist')
    wishlist_post = Wishlist.query.all()
    items = Book.query.join(Wishlist).filter_by(user_id=current_user.id)
    return render_template('whichlist.html', wishlist=wishlist_post, items=items)
