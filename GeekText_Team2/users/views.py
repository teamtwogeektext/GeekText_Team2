from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from GeekText_Team2 import db
from werkzeug.security import generate_password_hash, check_password_hash
from GeekText_Team2.models import User, Address
from GeekText_Team2.users.forms import RegistrationForm, LoginForm, UpdateUserForm, UpdateShippingForm
from GeekText_Team2.users.picture_handler import add_profile_pic

users = Blueprint('users', __name__, template_folder='templates/')

@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logged out')
    return redirect(url_for('core.home'))

@users.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first()
        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        if user is not None:
            if user.check_password(form.password.data) and user is not None:
            # log in the user
                login_user(user)
            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
                next = request.args.get('next')
            # if that next exists we go to it, otherwise we'll go to
            # the welcome page.
                if next == None or not next[0]=='/':
                    next = url_for('books.list')

            return redirect(next)
    return render_template('login.html', form=form)


@users.route('/register', methods=['GET','POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()

        u_address = Address(user_id=user.id,
                          address=form.address.data,
                          city=form.city.data,
                          state=form.state.data,
                          postal_code=form.zip_code.data,
                          phone_num=form.phone_num.data)


        print(u_address)
        print(user)

        db.session.add(u_address)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)


@users.route('/shipping_info', methods=['GET','POST'])
@login_required
def shipping_info():
    form = UpdateShippingForm()
    addresses = current_user.address
    if form.validate_on_submit():
        new_address = Address(user_id=current_user.id,
                              address=form.address.data,
                              city=form.city.data,
                              state=form.state.data,
                              postal_code=form.zip_code.data,
                              phone_num=form.phone_num.data)

        user = User.query.filter_by(address=form.email.data).first()

        print(new_address.address)
        db.session.add(new_address)
        db.session.commit()
        addresses = current_user.address
        redirect(url_for('users.shipping_info', form=form, addresses=addresses))

    return render_template('shipping.html', form=form,addresses=addresses)

@users.route('/account', methods=['GET','POST'])
@login_required
def account():

    form = UpdateUserForm()
    c_email = current_user.email
    c_username = current_user.username
    existing_email = None
    existing_username = None
    f_name = current_user.first_name
    l_name = current_user.last_name

    if form.validate_on_submit():

        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic
            flash('Picture updated')
            db.session.commit()

        u_name = form.username.data
        email = form.email.data
        fname = form.firstname.data
        lname = form.lastname.data

        existing_user_name = User.query.filter_by(username=u_name).first()
        existing_user_email = User.query.filter_by(email=email).first()

        current_user.first_name = form.firstname.data
        current_user.last_name = form.lastname.data
        db.session.commit()

        if(existing_user_name is not None):
            existing_username = existing_user_name.username

        if(existing_user_email is not None):
            existing_email = existing_user_email.email

        if existing_email == c_email and existing_username == c_username:
            return redirect(url_for('users.account'))

        if existing_email is None:
            current_user.email = form.email.data
        elif existing_email is not None and existing_email != c_email:
            print(existing_email)
            flash('A user already exists with that email')
            return redirect(url_for('users.account'))

        if existing_username is None:
            current_user.username = form.username.data
        elif existing_username is not None and existing_username != c_username:
            flash('A user already exists with that username')
            return redirect(url_for('users.account'))

        db.session.commit()
        print(existing_email," | ", c_email)
        print(existing_username, " | ", c_username)
        flash('User Account Updated')
        return redirect(url_for('users.account'))


    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static', filename='profile_pics/' + current_user.profile_image)
    return render_template('account.html', profile_image=profile_image, form=form, f_name=f_name, l_name=l_name)




    #This returns a list of all the post done by the same author
@users.route("/<username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)            # Limits the number of post that appears initially
    user = User.query.filter_by(username=username).first_or_404()   #Checks it is the right user
    # Returns a list of post, only done by our user
    blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    return render_template('user_blog_posts.html', blog_posts=blog_posts, user=user)
