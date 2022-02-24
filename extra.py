    data = {
        "id" : id
    }
    ninjas = Ninja.dojos_ninjas(data)
    return render_template("dojos_ninjas.html",dojo=Dojo.get_dojo_with_ninjas(data),ninjas=ninjas)