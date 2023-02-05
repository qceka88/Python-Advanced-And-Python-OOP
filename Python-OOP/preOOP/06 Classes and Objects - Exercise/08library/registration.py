from project.library import Library
from project.user import User


class Registration:

    def add_user(self, user_obj: User, library_obj: Library):
        if user_obj in library_obj.user_records:
            return f"User with id = {user_obj.user_id} already registered in the library!"
        library_obj.user_records.append(user_obj)

    def remove_user(self, user_obj: User, library_obj: Library):
        if user_obj not in library_obj.user_records:
            return "We could not find such user to remove!"
        library_obj.user_records.remove(user_obj)

    def change_username(self, user_id: int, new_username: str, library_obj: Library):
        for user_data in library_obj.user_records:
            if user_data.user_id == user_id and user_data.username == new_username:
                return "Please check again the provided username - it should be different than the username used so far!"
            if user_data.user_id == user_id:
                old_name = user_data.username
                if old_name in library_obj.rented_books:
                    taken_book_list = library_obj.rented_books[old_name]
                    del library_obj.rented_books[old_name]
                    library_obj.rented_books[new_username] = taken_book_list
                user_data.username = new_username
                return f"Username successfully changed to: {new_username} for user id: {user_id}"

        return f"There is no user with id = {user_id}!"

#
# user = User(12, 'Peter')
# library = Library()
# registration = Registration()
# registration.add_user(user, library)
# print(registration.add_user(user, library))
# registration.remove_user(user, library)
# print(registration.remove_user(user, library))
# registration.add_user(user, library)
# print(registration.change_username(2, 'Igor', library))
# print(registration.change_username(12, 'Peter', library))
# print(registration.change_username(12, 'George', library))
#
# [print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]
#
# library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
#                                                 'The Prisoner of Azkaban',
#                                                 'The Goblet of Fire',
#                                                 'The Order of the Phoenix',
#                                                 'The Half-Blood Prince',
#                                                 'The Deathly Hallows']})
# print(library.get_book('J.K.Rowling', 'The Deathly Hallows', 17, user))
# print(library.books_available)
# print(library.rented_books)
# print(user.books)
# print(library.get_book('J.K.Rowling', 'The Deathly Hallows', 10, user))
# print(library.return_book('J.K.Rowling', 'The Cursed Child', user))
# print(library.return_book('J.K.Rowling', 'The Deathly Hallows', user))
# exit()
# print(library.books_available)
# print(library.rented_books)
# print(user.books)
