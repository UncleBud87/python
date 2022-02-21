from flask import render_template,redirect,request,session
from flask_app import app
from flask_app.models.user import User


@app.route("/")
def index():
    return redirect('/login')



@app.route("/login")
def login():
    return render_template("login.html", users=User.get_all())