from flask import render_template,request,Blueprint
from flask_login import login_required


core = Blueprint('core',__name__)

@core.route('/')
def home():
    return render_template('home.html')

@core.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')


@core.route('/info')
def info():
    '''
    Example view of any other "core" page. Such as a info page, about page,
    contact page. Any page that doesn't really sync with one of the models.
    '''
    return render_template('info.html')
