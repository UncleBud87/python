from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home_page():
    return render_template("home.html",first_name = session['first_name'])

@app.route('/new_user', methods=['POST'])
def new_user():
    if not User.validate_account(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }

    account_id = User.save(data)
    print('+'*20)
    print(account_id)
    session['first_name'] = request.form['first_name']
    session['login'] = True
    return redirect('/home')


@app.route("/login", methods=['POST'])
def login():
    data = {'email': request.form['email']}
    account_in_db = User.get_by_email(data)

    if not account_in_db:
        flash('Invalid Email/Password', 'bad')
        return redirect('/')
    if not bcrypt.check_password_has(account_in_db.password,request.form['password']):
        flash("Invalid Email/Password", 'bad')
        return redirect('/')
    session['first_name'] = account_in_db.first_name
    session['login'] = True

    return redirect('/home')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')