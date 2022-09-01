from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import book
from flask_app.models import author

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    return render_template('authors.html', authors = author.Author.read_authors())

@app.route('/authors/add', methods = ['POST'])
def create_author():
    author.Author.add_author(request.form)
    return redirect ('/')

@app.route('/authors/<int:id>')
def get_author(id):
    data = {"id" : id}
    return render_template('author_profile.html', author = author.Author.get_author_with_books(data))
