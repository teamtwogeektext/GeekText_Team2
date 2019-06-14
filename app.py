# app.py at the same level as GeekText_Team2
from GeekText_Team2 import app
from flask import render_template
from GeekText_Team2 import db

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
