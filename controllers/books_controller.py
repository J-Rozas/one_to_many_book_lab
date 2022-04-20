from flask import Flask, render_template, Blueprint
from models.book import Book
from repositories import book_repository


books_blueprint = Blueprint("books",__name__)

@books_blueprint.route('/')
def home():
    return "Hello"

@books_blueprint.route('/allbooks')
def books():
    book_list = book_repository.select_all()
    return render_template('all_books.html', books = book_list)
