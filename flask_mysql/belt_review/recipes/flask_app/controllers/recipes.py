from flask_app import app

from flask import render_template, redirect, request, session, flash

from flask_app.models.recipe import Recipe

from flask_app.models.user import User

@app.route('/recipes')
def recipes():

    if not 'user_id' in session: #keeps from bypassing log in
        flash('Please log in', 'login')
        return redirect('/')

    recipes = Recipe.get_all_recipes()
    print(recipes)

        # get recipes from database

    return render_template('recipes.html', recipes = recipes)

@app.route('/recipes/new')
def new_recipe():

    return render_template('new_recipe.html')


@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    #validate data
    if not Recipe.validate_new_recipe(request.form):
        return redirect('/recipes/new')
    #then create recipe
    data = {
        'name' : request.form['recipe_name'],
        'description' : request.form['recipe_description'],
        'instructions' : request.form['recipe_instructions'],
        'under_30_min' : request.form['recipe_under_30_min'],
        'date_made' : request.form['recipe_date_made'],
        'user_id' : session['user_id']
    }
    Recipe.create_recipe(data)
    return redirect('/recipes/new')