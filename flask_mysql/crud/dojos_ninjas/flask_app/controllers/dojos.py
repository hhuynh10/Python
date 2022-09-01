from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route('/')
def dojo():
    return render_template("dojos.html", dojos = Dojo.read_dojo())

@app.route('/dojos', methods = ['POST'])
def create():
    Dojo.create_dojo(request.form)
    return redirect ('/')

@app.route('/dojos/<int:id>')
def get_ninjas(id):
    data = {"id" : id}
    return render_template("list_ninjas.html", dojo = Dojo.get_dojo_with_ninjas(data))
