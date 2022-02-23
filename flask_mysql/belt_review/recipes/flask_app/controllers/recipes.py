from flask_app import app

from flask import render_template, redirect, request, session, flash

from flask_app.models.recipe import Recipe

@app.route('/recipe/new')
def new_recipe():

    return render_template('new_recipe.html')