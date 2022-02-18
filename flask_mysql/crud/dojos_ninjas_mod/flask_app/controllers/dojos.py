
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

@app.route('/dojo/show/<int:id>')
def show(id):
    data = {
        "id" : id
    }
    return render_template("dojos_ninjas.html",dojo=Dojo.get_dojo_with_ninjas(data),ninjas=Ninja.get_all())


