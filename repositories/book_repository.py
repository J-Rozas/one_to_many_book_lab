from models.book import Book
from models.author import Author
from repositories import author_repository
from db.run_sql import run_sql

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'],row['cover'],row['price'],author, row['id'])
        books.append(book)
    return books

def save(book):
    sql = "INSERT INTO books (title, cover, price, author_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.cover, book.price, book.author.id]

    result = run_sql(sql, values)
    
    id = result[0]["id"]
    book.id = id
