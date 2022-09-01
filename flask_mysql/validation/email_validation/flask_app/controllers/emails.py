from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.email import Email

@app.route('/')
def email():
    return render_template('email.html')

@app.route('/register', methods=['POST'])
def register():
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.create(request.form)
    return redirect ('/dashboard')

@app.route('/dashboard')
def result():
    return render_template('dashboard.html', emails = Email.read())

@app.route('/delete/<int:id>')
def delete_email(id):
    data = {'id' : id}
    Email.delete(data)
    return redirect ('/dashboard')