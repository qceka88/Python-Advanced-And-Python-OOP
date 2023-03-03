class Library:

    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author, book_name, days_to_return, user):
        if book_name in self.books_available[author]:
            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}

            self.books_available[author].remove(book_name)
            user.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for username, data in self.rented_books.items():
            if book_name in data.keys():
                return f'The book "{book_name}" is already rented and will be available in {data[book_name]} days!'

    def return_book(self, author, book_name, user):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        del self.rented_books[user.username][book_name]

