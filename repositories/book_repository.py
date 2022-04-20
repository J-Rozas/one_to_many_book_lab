from db.run_sql import run_sql

from models.book import Book
from models.author import Author
from repositories import author_repository

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'],row['cover'],row['price'],author, row['id'])
        books.append(book)
    return books


