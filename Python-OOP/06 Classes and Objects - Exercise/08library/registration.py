class Registration:

    @staticmethod
    def add_user(user, library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)


    @staticmethod
    def remove_user(user, library):
        if user not in library.user_records:
            return "We could not find such user to remove!"

        library.user_records.remove(user)


    @staticmethod
    def change_username(user_id, new_username, library):
        for user in library.user_records:
            if user.user_id == user_id:
                if user.username != new_username:
                    user.username = new_username
                    if user.username in library.rented_books:
                        old_user_books = library.rented_books[user.username]
                        del library.rented_books[user.username]
                        library.rented_books[new_username] = old_user_books

                    return f"Username successfully changed to: {new_username} for user id: {user_id}"

                return f"Please check again the provided username - it should be different than the username used so far!"

        return f"There is no user with id = {user_id}!"
