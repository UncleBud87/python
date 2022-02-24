from flask_app import app

from flask import render_template, redirect, request, session, flash

from flask_app.models.car import Car

from flask_app.models.user import User

@app.route('/home')
def cars():

    if not 'user_id' in session: #keeps from bypassing log in
        flash('Please log in', 'login')
        return redirect('/')
    cars = Car.get_all_cars()
    print(cars)
        # get cars from database

    return render_template('home.html', cars = cars)


@app.route('/cars/new')
def sell_car():

    return render_template('sell_car.html')


@app.route('/cars/create', methods=['POST'])
def create_car():
    #validate data
    if not Car.validate_car(request.form):
        return redirect('/cars/new')
    #then create recipe
    data = {
        'price' : request.form['car_price'],
        'model' : request.form['car_model'],
        'make' : request.form['car_make'],
        'year' : request.form['car_year'],
        'description' : request.form['car_description'],
        'seller' : session['user_first_name'],
        'users_id' : session['user_id']
    }
    Car.create_car(data)
    return redirect('/home')

@app.route('/cars/<int:car_id>')
def single_car(car_id):
    data = {
        'id': car_id
    }

    car = Car.get_car_by_id(data)
    return render_template('view_car.html', car = car)

@app.route('/cars/<int:car_id>/edit')
def edit_car(car_id):
    data = {
        'id': car_id
    }
    car = Car.get_car_by_id(data)
    return render_template('edit_car.html', car = car)

@app.route('/cars/<int:car_id>/update', methods=['POST'])
def update_car(car_id):
    
    if not Car.validate_car(request.form):
        return redirect(f'/cars/{car_id}/edit')

    else:
        data = {
            'car_id': car_id,
            'car_model': request.form['car_model'],
            'car_make': request.form['car_make'],
            'car_description': request.form['car_description'],
            'car_year': request.form['car_year'],
            'car_price': request.form['car_price'],
        }
        Car.update_car(data)
        print('validation for edit is OK')
        return redirect(f'/cars/{car_id}')

@app.route('/cars/<int:car_id>/delete')
def delete_car(car_id):
    data = {
        'id': car_id
    }
    Car.delete_car(data)
    return redirect('/home')