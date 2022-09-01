from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, report

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users/create', methods = ['POST'])
def register():
    if user.User.create_user(request.form):
        return redirect ('/dashboard')
    return redirect ('/')

@app.route('/users/login', methods = ['POST'])
def login():
    if user.User.login(request.form):
        return redirect('/dashboard')
    return redirect('/')

@app.route('/users/logout')
def logout():
    session.clear()
    return redirect('/')