
from flask import render_template,redirect,request,session

from flask_app import app

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route("/")
def index():
    return redirect('/dojos')


@app.route("/dojos")
def dojo():
    return render_template("dojos.html", dojos=Dojo.get_all())

@app.route("/dojos/<int:id>/ninjas")
def dojos_ninjas(name):
    data ={
        'name' : name
    }
    return render_template("dojos_ninjas.html", dojos=Dojo.get_all(), ninja=Ninja.get_all())