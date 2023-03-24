from project.mammal import Mammal
from unittest import main, TestCase


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("TestName", "TestType", "TestSound")

    def test_initialisation_is_correct(self):
        self.assertEqual("TestName", self.mammal.name)
        self.assertEqual("TestType", self.mammal.type)
        self.assertEqual("TestSound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_method(self):
        result = self.mammal.make_sound()
        expected_result = "TestName makes TestSound"

        self.assertEqual(result, expected_result)

    def test_get_kingdom_method(self):
        result = "animals"
        expected_result = self.mammal.get_kingdom()

        self.assertEqual(result, expected_result)

    def test_ifo_method(self):
        result = "TestName is of type TestType"
        expected_result = self.mammal.info()

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    main()
