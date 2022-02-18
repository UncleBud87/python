
from flask import render_template,redirect,request,session
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/dojo/show/<int:id>')
def show(id):
    data ={ 
        "dojo.id" : "id",
        "ninja.first_name" : "first_name",
        "ninja.last_name" : "last_name",
        "ninja.age" : "age"

    }
    return render_template("dojos_ninjas.html",dojo=Dojo.get_one(data))