from project.tennis_player import TennisPlayer
from unittest import main, TestCase


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.player = TennisPlayer("Yanko", 33, 100.5)
        self.player02 = TennisPlayer("Yanko02", 25, 50.5)
        self.player02.wins = ["RolanGaros", "OpenAustralia", "LondonTennis"]

    def test_initialisation_is_correct(self):
        self.assertEqual("Yanko", self.player.name)
        self.assertEqual(33, self.player.age)
        self.assertEqual(100.5, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            test = TennisPlayer("Ya", 50, 10.5)

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            test = TennisPlayer("Ken", 15, 5.5)

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_for_adding_tournaments(self):
        tournaments = ["RolanGaros", "OpenAustralia", "LondonTennis"]
        for t in tournaments:
            self.player.add_new_win(t)

        self.assertEqual(tournaments, self.player.wins)

    def test_add_new_win_for_adding_existing_tournament(self):
        tournaments = ["RolanGaros", "OpenAustralia", "LondonTennis"]

        for t in tournaments:
            result = self.player02.add_new_win(t)
            self.assertEqual(f"{t} has been already added to the list of wins!", result)

    def test__lt__(self):
        result = self.player < self.player02
        result2 = self.player02 < self.player
        expected_result = f'Yanko is a better player than Yanko02'
        expected_result02 = "Yanko is a top seeded player and he/she is better than Yanko02"

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_result02, result2)

    def test__str__(self):
        expected_result = f"Tennis Player: Yanko02\n" \
                          "Age: 25\n" \
                          "Points: 50.5\n" \
                          "Tournaments won: RolanGaros, OpenAustralia, LondonTennis"

        self.assertEqual(expected_result, str(self.player02))


if __name__ == '__main__':
    main()
