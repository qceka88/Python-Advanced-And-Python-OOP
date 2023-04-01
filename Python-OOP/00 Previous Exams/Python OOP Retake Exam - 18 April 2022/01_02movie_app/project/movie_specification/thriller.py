from project.movie_specification.movie import Movie


class Thriller(Movie):

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = 16):
        super().__init__(title, year, owner, age_restriction)

    @property
    def restriction(self):
        AGE_RESTRICTION = 16
        return AGE_RESTRICTION
