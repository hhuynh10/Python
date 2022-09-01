from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import author
from flask_app.models import book

@app.route('/books')
def view_books():
    return render_template('books.html', books = book.Book.read_books())

@app.route('/books/add', methods = ['POST'])
def create_book():
    book.Book.add_book(request.form)
    return redirect ('/books')

@app.route('/books/<int:id>')
def get_book(id):
    data = {'id' : id}
    return render_template("book_profile.html", book = book.Book.get_book_with_authors(data), unfavor_author = author.Author.unfavorited_authors(data))

@app.route('/join/author', methods = ['POST'])
def join_author():
    author.Author.add_favorite(request.form)
    return redirect (f"/books/{request.form['book_id']}")