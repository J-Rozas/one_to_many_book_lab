from db.run_sql import run_sql

from models.book import Book
from models.author import Author



def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if len(results) > 0:
        result = results[0]
        author = Author(result['name'], result['id'])
    return author