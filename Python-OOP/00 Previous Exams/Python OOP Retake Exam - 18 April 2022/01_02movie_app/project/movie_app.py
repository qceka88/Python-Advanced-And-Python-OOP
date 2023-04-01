from project.movie_specification.fantasy import Fantasy
from project.movie_specification.action import Action
from project.movie_specification.thriller import Thriller
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection: [Fantasy, Action, Thriller] = []
        self.users_collection: [User] = []

    def register_user(self, username: str, age: int):
        try:
            user = next(filter(lambda u: u.username == username, self.users_collection))
            raise Exception("User already exists!")

        except StopIteration:
            user = User(username, age)
            self.users_collection.append(user)

            return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        try:
            user = next(filter(lambda u: u.username == username, self.users_collection))
            if movie.owner != user:
                raise Exception(f"{username} is not the owner of the movie {movie.title}!")

            if movie in self.movies_collection:
                raise Exception("Movie already added to the collection!")

            self.movies_collection.append(movie)
            user.movies_owned.append(movie)

            return f"{username} successfully added {movie.title} movie."

        except StopIteration:
            raise Exception("This user does not exist!")

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        owner = [o for o in self.users_collection if o.username == username][0]
        if movie.owner != owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attr, value in kwargs.items():
            movie.__setattr__(attr, value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = [u for u in self.users_collection if u.username == username][0]
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        #TODO: test functionality of this method
        user = [u for u in self.users_collection if u.username == username][0]
        if movie.owner == user:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]

        if movie in user.movies_liked:
            movie.likes -= 1
            user.movies_liked.remove(movie)

            return f"{username} disliked {movie.title} movie."
        else:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

    def display_movies(self):
        movies = [m.details() for m in sorted(self.movies_collection, key=lambda x: (-x.year, x.title))]
        return '\n'.join(movies) if movies else "No movies found."

    def __str__(self):
        users_data = ', '.join(u.username for u in self.users_collection)
        movies_data = ', '.join(m.title for m in self.movies_collection)

        users = f"All users: {users_data if users_data else 'No users.'}"
        movies = f"All movies: {movies_data if movies_data else 'No movies.'}"

        return users + '\n' + movies
