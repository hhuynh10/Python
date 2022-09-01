from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, adventure

@app.route('/adventures')
def adventures():
    if 'user_id' not in session:
        return redirect ('/logout')
    return render_template('add_adventure.html')

@app.route('/adventures/create', methods = ['POST'])
def create_adventures():
    if adventure.Adventure.create_adventure(request.form):
        return redirect ('/dashboard')
    return redirect ('/adventures')

@app.route('/delete/<int:id>')
def delete(id):
    adventure.Adventure.delete_adventure(id)
    return redirect ('/dashboard')

@app.route('/all_adventures')
def view_all():
    return render_template('all_adventures.html', adventures = adventure.Adventure.view_all_adventures())

@app.route('/edit/<int:id>')
def edit(id):
    this_user = user.User.get_user_by_id(session['user_id'])
    return render_template("edit_adventure.html", this_user = this_user, adventure = adventure.Adventure.view_one_adventure(id))

@app.route('/edit/adventure', methods = ['POST'])
def edit_adventure():
    id = request.form['id']
    if not adventure.Adventure.validate_reg_data(request.form):
        return redirect (f'/edit/{id}')
    adventure.Adventure.update_adventure(request.form)
    return redirect ('/dashboard')

@app.route('/view/<int:id>')
def view(id):
    return render_template('view_adventure.html', adventure = adventure.Adventure.view_one_adventure(id))


