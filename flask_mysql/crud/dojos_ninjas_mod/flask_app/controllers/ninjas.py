
from flask import render_template,redirect,request,session

from flask_app import app

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/user/new")
def new():
    return render_template("new_user.html")

@app.route('/create/ninja',methods=['POST'])
def create():
    print(request.form)
    id=Ninja.save(request.form)
    return redirect('/dojos')
