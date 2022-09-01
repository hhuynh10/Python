from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect ('users')

@app.route('/users')
def read():
    return render_template("all_users.html", users = User.read_all())

@app.route('/users/add')
def add():
    return render_template("new_user.html")

@app.route('/users/create', methods=['POST'])
def create_user():
    User.create(request.form)
    return redirect('/users')

@app.route('/users/delete/<int:id>')
def delete_user(id):
    data = {'id' : id}
    User.delete(data)
    return redirect('/users')

@app.route('/users/show/<int:id>')
def show(id):
    data = {'id' : id}
    return render_template("one_user.html", user = User.read_one(data))

@app.route('/users/edit/<int:id>')
def edit(id):
    data = {'id' : id}
    return render_template("edit_user.html", user = User.read_one(data))

@app.route('/users/update', methods = ['POST'])
def update_user():
    User.update(request.form)
    return redirect('/users')
