from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from GeekText_Team2 import db
from GeekText_Team2.models import Cart, User, Book


cart_blueprint = Blueprint('cart', __name__)

@cart_blueprint.route('/cart')
@login_required
def cart():
    items = Book.query.join(Cart).filter_by(userId=current_user.id)
    totalPrice = 0
    for row in items:
        totalPrice += row.price
    return render_template('cart.html',totalPrice=totalPrice, items=items)

@cart_blueprint.route('/addToCart',  methods=['GET','POST'])
@login_required
def addToCart():
    bookId = request.args.get('ISBN')
    item = Cart(userId=current_user.id,ISBN=bookId)
    db.session.add(item)
    db.session.commit()
    flash('Book added to your shopping cart')
    return redirect(url_for('books.list'))

   

@cart_blueprint.route('/removeFromCart')
@login_required
def removeFromCart():
    item = Cart.query.filter_by(userId=current_user.id, ISBN=request.args.get('ISBN')).first()
    db.session.delete(item)
    db.session.commit()
    flash('Book removed from your shopping cart')
    return redirect(url_for('cart.cart'))


