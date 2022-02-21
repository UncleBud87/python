from flask import render_template,redirect,request,session, url_for,flash
from flask_app import app
from flask_app.models.user import User


@app.route("/")
def index():
    return redirect('/login')

@app.route("/login")
def login():
    return render_template("login.html", users=User.get_all())

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)