from flask import render_template,redirect,request,session, url_for,flash
from flask_app import app
from flask_app.models.user import User


@app.route("/")
def index():
    return redirect('/login')

@app.route("/login")
def login():
    return render_template("index.html")

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route("/new/registration")
def save():
    User.save(request.form)
    return redirect('/welcome')


@app.route('/login', methods=['GET', 'POST'])
def new_login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'email' or \
                request.form['password'] != 'password':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('welcome.html', error=error)