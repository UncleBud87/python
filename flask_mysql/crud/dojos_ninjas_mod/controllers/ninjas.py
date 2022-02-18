
from flask import render_template,redirect,request,session

from dojos_ninjas_mod import app

from dojos_ninjas_mod.models.ninja import Ninja

@app.route("/user/new")
def new():
    return render_template("new_user.html")

@app.route('/create/ninja',methods=['POST'])
def create():
    print(request.form)
    id=Ninja.save(request.form)
    return redirect('/dojos')
