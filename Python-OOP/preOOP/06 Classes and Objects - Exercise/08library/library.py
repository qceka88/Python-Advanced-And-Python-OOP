from project.user import User


class Library:
    def __init__(self):
        self.user_records = []  # list with objects
        self.books_available = {}  # {author: [books]}
        self.rented_books = {}  # ({usernames: {book names: days to return}}).

    def get_book(self, author: str, book_name: str, days_to_return: int, user_obj: User):
        if book_name in self.books_available[author]:
            user_obj.books.append(book_name)
            self.books_available[author].remove(book_name)
            if user_obj.username not in self.rented_books:
                self.rented_books[user_obj.username] = {}
            if book_name not in self.rented_books[user_obj.username]:
                self.rented_books[user_obj.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for user, books in self.rented_books.items():
            if book_name in books:
                return f'The book "{book_name}" is already rented and will be available in {books[book_name]} days!'

    def return_book(self, author: str, book_name: str, user_obj: User):
        if book_name not in user_obj.books:
            return f"{user_obj.username} doesn't have this book in his/her records!"
        else:
            user_obj.books.remove(book_name)
            del self.rented_books[user_obj.username][book_name]
            if author in self.books_available:
                self.books_available[author].append(book_name)
