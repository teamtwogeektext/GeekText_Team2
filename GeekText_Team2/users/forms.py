from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms.fields.html5 import EmailField
# FOR IMAGE VALIDATION
from flask_wtf.file import FileField, FileAllowed
from flask_bootstrap import Bootstrap
# User Based Imports
from flask_login import current_user
from GeekText_Team2.models import User
from pygeocoder import Geocoder
import re


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired(), Email(message="Must input a valid email")])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6, max=15)])
    submit = SubmitField('LogIn')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first() is None:
            raise ValidationError("That email doesn't exist")

    def validate_password(self, password):
        user = User.query.filter_by(email=self.email.data).first()
        if user is not None:
            checked = user.check_password(password.data)
            if checked == False:
                raise ValidationError("Wrong password")


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), Length(
        min=6, max=15, message="Must be between 6 and 10 characters and unique")])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo(
        'pass_confirm', message='Passwords do not match!'), Length(min=6, max=15, message="Must be between 6 and 10 characters")])
    pass_confirm = PasswordField(
        'Confirm password', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip_code = IntegerField('ZIP', validators=[DataRequired()])
    phone_num = IntegerField('Phone', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError("That username is taken!")

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("That email is already registerd")

    def validate_phone_num(self, phone_num):
        Pattern = re.compile("^\d{3}-\d{3}-\d{4}$")
        if Pattern.match(phone_num) == False:
            raise ValidationError(
                "Invalid phone number: 10 digits, with dashes or no dashes")

        # def validate_address(self, address):
        #addr = Geocoder.geocode(address)
        # print(addr)
        # if addr == False:
        #raise ValidationError("Address not valid")


class UpdateUserForm(FlaskForm):

    email = StringField('Email')
    firstname = StringField('FirstName')
    lastname = StringField('FirstName')
    username = StringField('UserName')
    picture = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Update")

### CHECK TO SEE IF USERNAME AND EMAIL ARE ALREADY TAKEN ###

    def validate_username(self, username):
        if username is not None:
            existing_user = User.query.filter_by(
                username=username.data).first()
            current_username = current_user.username
            if existing_user is not None:
                if existing_user.username != current_username:
                    raise ValidationError("That username is taken!")

    def validate_email(self, email):
        if email is not None:
            existing_user = User.query.filter_by(
                email=email.data).first()
            current_email = current_user.email
            if existing_user is not None:
                if existing_user.email != current_email:
                    raise ValidationError("That email is taken!")

    def check_email(self, field):
        if current_user.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self, field):
        if current_user.query.filter_by(email=field.data).first():
            raise ValidationError('Your username has been registered already!')


class ForgotForm(FlaskForm):
    email = EmailField('Email', validators=[Email(), DataRequired()])
    submit = SubmitField("Send")


class PasswordResetForm(FlaskForm):
    current_password = PasswordField("Current Password", validators=[
                                     DataRequired(), Length(min=6, max=15)])


class ChangePassword(FlaskForm):
    password = PasswordField("Current Password", validators=[
                             DataRequired(), Length(min=6, max=15)])
    new_password = PasswordField("New Password", validators=[DataRequired(), EqualTo(
        'new_password_confirm', message='Passwords do not match!'), Length(min=6, max=15, message="Must be between 6 and 10 characters")])
    new_password_confirm = PasswordField(
        'Confirm password', validators=[DataRequired()])
    submit = SubmitField("Submit")

    def validate_password(self, password):
        if current_user.check_password(password.data) is False:
            raise ValidationError("Incorrect Password. Try Again")

    def validate_new_password(self, new_password):
        if current_user.check_password(new_password.data):
            raise ValidationError("Please use a new password")


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
