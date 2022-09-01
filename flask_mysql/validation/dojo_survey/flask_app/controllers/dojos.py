from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route('/')
def dojo_survey():
    return render_template('info.html')

@app.route('/create', methods=['POST'])
def create_dojo():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    Dojo.create(request.form)
    return redirect("/result")

@app.route('/result')
def result():
    return render_template('result.html', dojos = Dojo.read())