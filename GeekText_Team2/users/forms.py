from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField,TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import ValidationError
# FOR IMAGE VALIDATION
from flask_wtf.file import FileField, FileAllowed
from flask_bootstrap import Bootstrap

# User Based Imports
from flask_login import current_user
from GeekText_Team2.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired(), Email(message="Must input a valid email")])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6, max=15)])
    submit = SubmitField('LogIn')


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo(
        'pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField(
        'Confirm password', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip_code = IntegerField('ZIP', validators=[DataRequired()])
    phone_num = IntegerField('Phone', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')
            return False
        return True


class UpdateUserForm(FlaskForm):

    email = StringField('Email', validators=[Email()])
    firstname = StringField('FirstName')
    lastname = StringField('FirstName')
    username = StringField('UserName')
    #new_password = StringField('NewPassword', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Update")

### CHECK TO SEE IF USERNAME AND EMAIL ARE ALREADY TAKEN ###
    def check_email(self, field):
        if current_user.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self, field):
        if current_user.query.filter_by(email=field.data).first():
            raise ValidationError('Your username has been registered already!')

class AddPaymentInfo(FlaskForm):
    card_num = StringField('Card Number', validators=[DataRequired()])
    name = StringField('Card Holder', validators=[DataRequired()])
    exp_date = StringField('Expiration', validators=[DataRequired()])
    csv = IntegerField('CSV', validators=[DataRequired()])
    zip = IntegerField('ZIP', validators=[DataRequired()])
    submit = SubmitField('Add Card')


class UpdateShippingForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip_code = IntegerField('ZIP', validators=[DataRequired()])
    phone_num = IntegerField('Phone', validators=[DataRequired()])
    submit = SubmitField('Update')

class UpdateAddressForm(FlaskForm):
    address = StringField('Address')
    city = StringField('City')
    state = StringField('State')
    zip_code = IntegerField('ZIP')
    phone_num = IntegerField('Phone')
    submit = SubmitField('Update')


class wishlistPostForm(FlaskForm):
	title = StringField('title', validators=[DataRequired()])
	submit = SubmitField('Wishlist')
