from project.movie_specification.movie import Movie


class User:

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: [Movie] = []
        self.movies_owned: [Movie] = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value.strip() == "":
            raise ValueError("Invalid username!")

        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")

        self.__age = value

    def __str__(self):
        liked_movies_data = '\n'.join([m.details() for m in self.movies_liked])
        liked_movies = liked_movies_data if liked_movies_data else "No movies liked."
        owned_movies_data = '\n'.join([m.details() for m in self.movies_owned])
        owned_movies = owned_movies_data if owned_movies_data else "No movies owned."

        message = [f"Username: {self.username}, Age: {self.age}", "Liked movies:",
                   liked_movies, f"Owned movies:", owned_movies]

        return '\n'.join(message)


