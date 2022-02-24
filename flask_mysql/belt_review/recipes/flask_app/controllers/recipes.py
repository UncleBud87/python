from flask_app import app

from flask import render_template, redirect, request, session, flash

from flask_app.models.recipe import Recipe

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
    if not Recipe.validate_recipe(request.form):
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
    return redirect('/recipes')

@app.route('/recipes/<int:recipe_id>')
def single_recipe(recipe_id):
    data = {
        'id': recipe_id
    }

    recipe = Recipe.get_recipe_by_id(data)
    return render_template('view_recipe.html', recipe = recipe)

@app.route('/recipes/<int:recipe_id>/edit')
def edit_recipe(recipe_id):
    data = {
        'id': recipe_id
    }
    recipe = Recipe.get_recipe_by_id(data)
    return render_template('edit_recipe.html', recipe = recipe)

@app.route('/recipes/<int:recipe_id>/update', methods=['POST'])
def update_recipe(recipe_id):
    
    if not Recipe.validate_recipe(request.form):
        return redirect(f'/recipes/{recipe_id}/edit')

    else:
        data = {
            'recipe_id': recipe_id,
            'recipe_name': request.form['recipe_name'],
            'recipe_description': request.form['recipe_description'],
            'recipe_instructions': request.form['recipe_instructions'],
            'recipe_date_made': request.form['recipe_date_made'],
            'recipe_under_30_min': request.form['recipe_under_30_min'],

        }
        Recipe.update_recipe(data)
        print('validation for edit is OK')
        return redirect(f'/recipes/{recipe_id}')

@app.route('/recipes/<int:recipe_id>/delete')
def delete_recipe(recipe_id):
    data = {
        'id': recipe_id
    }
    Recipe.delete_recipe(data)
    return redirect('/recipes')