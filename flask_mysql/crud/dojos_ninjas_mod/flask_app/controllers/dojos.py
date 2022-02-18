
from flask import render_template,redirect,request,session

from flask_app import app

from flask_app.models.dojo import Dojo


@app.route("/")
def index():
    return redirect('/index')


@app.route("/index")
def dojo():
    return render_template("index.html", dojo=Dojo.get_all())