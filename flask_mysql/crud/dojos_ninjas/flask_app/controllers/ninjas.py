from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def ninja():
    return render_template("ninjas.html", dojos = Dojo.read_dojo())

@app.route('/ninjas/create', methods = ["POST"])
def create_ninjas():
    Ninja.create_ninja(request.form)
    return redirect ('/ninjas')

