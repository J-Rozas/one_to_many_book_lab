from models.book import Book
from models.author import Author

from repositories import author_repository, book_repository

author1 = Author("Author_1")
author2 = Author("Author_2")

author_repository.save(author1)
author_repository.save(author2)

book1 = Book("Book_1", "Hardcase", 29.99, author2)
book2 = Book("Book_2", "Hardcase", 19.99, author2)

book_repository.save(book1)
book_repository.save(book2)