from project.movie_specification.movie import Movie


class Action(Movie):

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = 12):
        super().__init__(title, year, owner, age_restriction)

    @property
    def restriction(self):
        AGE_RESTRICTION = 12
        return AGE_RESTRICTION
