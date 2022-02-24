from flask_app import app

from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User

@app.route('/home')
def recipes():

    if not 'user_id' in session: #keeps from bypassing log in
        flash('Please log in', 'login')
        return redirect('/')

        # get recipes from database

    return render_template('home.html')
