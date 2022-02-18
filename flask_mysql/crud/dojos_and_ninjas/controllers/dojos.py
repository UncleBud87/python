from flask import render_template,redirect,request,session

from dojos_and_ninjas import app

from dojos_and_ninjas.models.dojo import Dojo

@app.route("/")
def index():
    return redirect('/dojos')


@app.route("/dojos")
def dojos():
    return render_template("dojos.html", dojos=Dojo.get_all())


@app.route("/new/dojos")
def new():
    return render_template("#######.html")

@app.route('/create/dojos',methods=['POST'])
def create():
    print(request.form)
    id=Dojo.save(request.form)
    return redirect(f'/show/{id}/dojos_ninjas')