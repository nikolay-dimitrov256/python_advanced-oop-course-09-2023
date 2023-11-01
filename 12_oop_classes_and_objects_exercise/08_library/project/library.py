from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        def search_rented_books():
            for us_name, data in self.rented_books.items():
                if book_name in data:
                    return (f'The book "{book_name}" is already rented and will be available in '
                            f'{self.rented_books[us_name][book_name]} days!')

        if author in self.books_available:
            for book in self.books_available[author]:
                if book == book_name:
                    user.books.append(book_name)
                    self.books_available[author].remove(book)

                    if user.username not in self.rented_books:
                        self.rented_books[user.username] = {}
                    self.rented_books[user.username][book_name] = days_to_return

                    return f"{book_name} successfully rented for the next {days_to_return} days!"

            result = search_rented_books()
            if result:
                return result

        else:
            result = search_rented_books()
            if result:
                return result

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
            user.books.remove(book_name)

        else:
            return f"{user.username} doesn't have this book in his/her records!"
