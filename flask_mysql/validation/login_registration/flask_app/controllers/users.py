from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

# CREATE USERS
@app.route('/users/register', methods = ['POST'])
def register_users():
    if User.create_user(request.form):
        return redirect ('/users/profile')
    return redirect ('/')

# READ USERS
@app.route('/')
def index():
    return redirect ('/users')

@app.route('/users')
def users():
    return render_template('index.html')

@app.route('/users/profile')
def user_profile():
    data = {'id' : session['user_id']}
    return render_template('profile.html', user = User.read_user_by_id(data))

@app.route('/users/logout')
def user_logout():
    session.clear()
    return redirect('/')

@app.route('/users/login', methods = ['POST'])
def user_login():
    if User.login(request.form):
        return redirect ('/users/profile')
    return redirect ('/')

# UPDATE USERS

# DELETE USERS
