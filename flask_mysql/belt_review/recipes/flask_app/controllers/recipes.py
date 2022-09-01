from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, recipe

@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect ('/logout')
    return render_template('add_recipe.html')

@app.route('/recipes/create', methods = ['POST'])
def create_recipes():
    if recipe.Recipe.create_recipe(request.form):
        return redirect ('/dashboard')
    return redirect ('/recipes')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect ('/logout')
    this_user = user.User.get_user_by_id(session['user_id'])
    return render_template('dashboard.html', this_user = this_user, recipes = recipe.Recipe.view_all_recipes())

@app.route('/delete/<int:id>')
def delete(id):
    recipe.Recipe.delete_recipe(id)
    return redirect ('/dashboard')

@app.route('/view/<int:id>')
def view(id):
    this_user = user.User.get_user_by_id(session['user_id'])
    return render_template('view_recipe.html',this_user = this_user, recipe = recipe.Recipe.view_one_recipe(id))

@app.route('/edit/<int:id>')
def edit(id):
    return render_template("edit.html", recipe = recipe.Recipe.view_one_recipe(id))

@app.route('/edit/recipe', methods = ['POST'])
def edit_recipe():
    id = request.form['id']
    if not recipe.Recipe.validate_rep_data(request.form):
        return redirect (f"/edit/{id}")
    recipe.Recipe.update_recipe(request.form)
    return redirect ('/dashboard')

