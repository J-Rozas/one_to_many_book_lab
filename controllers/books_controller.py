from flask import redirect, render_template, Blueprint
from repositories import book_repository


books_blueprint = Blueprint("books",__name__)

@books_blueprint.route('/', methods=["GET"])
@books_blueprint.route('/books', methods=["GET"])
def books():
    book_list = book_repository.select_all()
    return render_template('all_books.html', books = book_list)

@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")
