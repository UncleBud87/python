
from flask import render_template,redirect,request,session

from dojos_ninjas_mod import app

from dojos_ninjas_mod.models.dojo import Dojo

@app.route("/")
def index():
    return redirect('/dojos')


@app.route("/dojos")
def dojo():
    return render_template("dojos.html", dojo=Dojo.get_all())