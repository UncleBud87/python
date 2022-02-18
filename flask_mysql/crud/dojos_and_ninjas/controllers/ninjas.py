from flask import render_template,redirect,request,session

from dojos_and_ninjas import app

from dojos_and_ninjas.models.ninja import Ninja

@app.route("/new/ninjas")
def new():
    return render_template("new_user.html")

@app.route('/create/ninjas',methods=['POST'])
def create():
    print(request.form)
    id=Ninja.save(request.form)
    return redirect(f'/show/{id}/dojos_ninjas')