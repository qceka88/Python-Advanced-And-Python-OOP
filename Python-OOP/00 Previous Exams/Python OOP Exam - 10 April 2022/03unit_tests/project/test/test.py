from project.movie import Movie
from unittest import main, TestCase


class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie("Rambo", 1988, 7.5)

    def test_initialisation_is_correct(self):
        self.assertEqual("Rambo", self.movie.name)
        self.assertEqual(1988, self.movie.year)
        self.assertEqual(7.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_invalid_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            test = Movie("", 2003, 6.5)

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_invalid_year_setter(self):
        with self.assertRaises(ValueError) as ve:
            test = Movie("Rambo2", 1500, 6.5)

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_for_correct_adding(self):
        actors = ["Asen", "Ivan", "Georgi"]
        [self.movie.add_actor(a) for a in actors]
        self.assertEqual(actors, self.movie.actors)

    def test_add_actor_for_existing_name(self):
        actors = ["Asen", "Ivan", "Georgi"]
        [self.movie.add_actor(a) for a in actors]
        result = self.movie.add_actor("Asen")

        self.assertEqual("Asen is already added in the list of actors!", result)

    def test__gt__movie_is_better_than_other(self):
        other = Movie("Rambo4", 2014, 5.5)
        result = self.movie > other
        self.assertEqual('"Rambo" is better than "Rambo4"', result)

    def test__gt__other_is_better_than_movie(self):
        other = Movie("Dalas", 1979, 9.5)
        result = self.movie > other
        self.assertEqual('"Dalas" is better than "Rambo"', result)

    def test__repr__(self):
        actors = ["Asen", "Ivan", "Georgi"]
        [self.movie.add_actor(a) for a in actors]

        expected_result = "Name: Rambo\nYear of Release: 1988\nRating: 7.50\nCast: Asen, Ivan, Georgi"

        result = repr(self.movie)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
