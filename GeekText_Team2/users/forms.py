from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
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
    submit = SubmitField('Log In')


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
    #city =
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

    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('First Name', validators=[DataRequired()])
    username = StringField('UserName', validators=[DataRequired()])
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
