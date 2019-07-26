from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from GeekText_Team2 import db
from GeekText_Team2.models import Cart, User, Book, Orders, SavedItems


cart_blueprint = Blueprint('cart', __name__)

@cart_blueprint.route('/cart')
@login_required
def cart():
    items = Book.query.join(Cart).filter_by(userId=current_user.id)
    totalPrice = 0
    for row in items:
        item = Cart.query.filter_by(ISBN=row.ISBN).first()
        totalPrice += row.price*item.quantity
    savedItems = Book.query.join(SavedItems).filter_by(userId=current_user.id)
    return render_template('cart.html',totalPrice=totalPrice, items=items, savedItems=savedItems)

@cart_blueprint.route('/addToCart',  methods=['GET','POST'])
@login_required
def addToCart():
    bookId = request.args.get('ISBN')
    item = Cart(userId=current_user.id,ISBN=bookId, quantity=1)
    db.session.add(item)
    db.session.commit()
    flash('Book added to your shopping cart')
    return redirect(url_for('books.list'))

@cart_blueprint.route('/addToSaved',  methods=['GET','POST'])
@login_required
def addToSaved():
    bookId = request.args.get('ISBN')
    item = SavedItems(userId=current_user.id,ISBN=bookId)
    db.session.add(item)
    db.session.commit()
    flash('Book saved')
    return redirect(url_for('books.list'))


@cart_blueprint.route('/moveToCart')
@login_required
def moveToCart():
    bookId = request.args.get('ISBN')
    item = Cart(userId=current_user.id,ISBN=bookId,quantity=1)
    savedItem = SavedItems.query.filter_by(userId=current_user.id,ISBN=bookId).first()
    db.session.add(item)
    db.session.delete(savedItem)
    db.session.commit()
    flash('Book moved to cart')
    return redirect(url_for('cart.cart'))

   

@cart_blueprint.route('/removeFromCart')
@login_required
def removeFromCart():
    item = Cart.query.filter_by(userId=current_user.id, ISBN=request.args.get('ISBN')).first()
    db.session.delete(item)
    db.session.commit()
    flash('Book removed from your shopping cart')
    return redirect(url_for('cart.cart'))


@cart_blueprint.route('/removeFromSaved')
@login_required
def removeFromSaved():
    item = SavedItems.query.filter_by(userId=current_user.id, ISBN=request.args.get('ISBN')).first()
    db.session.delete(item)
    db.session.commit()
    flash('Book removed from your shopping cart')
    return redirect(url_for('cart.cart'))


@cart_blueprint.route('/checkout', methods=['GET','POST'])
@login_required
def checkout():
    items = Book.query.join(Cart).filter_by(userId=current_user.id)
    totalPrice = 0
    for row in items:
        item = Cart.query.filter_by(userId=current_user.id, ISBN=row.ISBN).first()
        totalPrice += row.price*item.quantity
        order = Orders(userId=current_user.id, ISBN=row.ISBN, quantity=item.quantity)
        db.session.add(order)
        db.session.delete(item)
    db.session.commit()
    return render_template('checkout.html',totalPrice=totalPrice, items=items)



@cart_blueprint.route('/clearOrders')
@login_required
def orderErase():
    orders = Orders.query.filter_by(userId=current_user.id)
    for row in orders:
        order = Orders.query.filter_by(userId=current_user.id, ISBN=row.ISBN).first()
        db.session.delete(order)
    db.session.commit()
    return redirect(url_for('cart.cart'))