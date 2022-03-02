
from flask_app import app

from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():

    return render_template("index.html")

@app.route('/user/register', methods=['POST'])
def register_user():

    if not User.validate_new_user(request.form):
        print('validation fails')
        return redirect('/')

    else:
        print('validation is good')
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : bcrypt.generate_password_hash(request.form['password'])
        }
        print(data)
        User.create_new_user(data)
        flash(' Registration Complete', 'register')
        return redirect('/')

@app.route('/user/login', methods=['POST'])
def user_login():
    #determine if user exist

    user = User.get_user_by_email(request.form)

    if not user:
        flash('Email is not registered.', 'login')
        return redirect('/')
    #check password agains db
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Password is Incorrect', 'login')
        return redirect('/')
    #user is logged in

    session['user_id'] = user.id
    session['user_email'] = user.email
    session['user_first_name'] = user.first_name
    #use only information that will be called on during session

    return redirect('/home')

@app.route('/home')
def recipes():

    if not 'user_id' in session: #keeps from bypassing log in
        flash('Please log in', 'login')
        return redirect('/')

    return render_template('home.html')

@app.route('/user/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'login')
    return redirect('/')