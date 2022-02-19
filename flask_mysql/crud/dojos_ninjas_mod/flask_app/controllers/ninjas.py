
from flask import render_template,redirect,request,session
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route("/new_ninja")
def ninja():
    dojos = Dojo.get_all()
    return render_template("new_ninja.html",dojos=dojos)



@app.route("/create/ninja", methods=['POST'])
def ninja_post():
    print(request.form)
    Ninja.save(request.form)
    return redirect("/dojos")




