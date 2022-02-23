
from flask_app import app

from flask import render_template, redirect, request, session

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
        return redirect('/')