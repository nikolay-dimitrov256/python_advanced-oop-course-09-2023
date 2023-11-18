from typing import List


class Book:
    def __init__(self, title, autor):
        self.title = title
        self.autor = autor
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return f'{self.title} by {self.autor}'


class Library:
    def __init__(self, address, *books):
        self.address = address
        self.books: List[Book] = list(books)

    def enter_book(self, book: Book):
        self.books.append(book)

    def find_book(self, title):
        book = next((b for b in self.books if b.title == title), None)

        return book
