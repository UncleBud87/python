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

@app.route('/create', methods=['POST'])
def create_account():
    if not User.validate_account(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_has(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    account_in_db = User.get_by_email(request.form['email'])
    if account_in_db:
        flash('Email is already in use','error')
        return redirect('/')
    
    account_id = User.save(data)
    print('+'*20)
    print(account_id)
    session['first_name'] = request.form['first_name']
    session['login'] = True
    return redirect('/home')

@app.route('/{{email}}/login', methods=['GET', 'POST'])
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