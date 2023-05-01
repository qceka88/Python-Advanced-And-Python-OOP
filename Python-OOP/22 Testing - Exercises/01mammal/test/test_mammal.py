from project.mammal import Mammal
from unittest import main, TestCase


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.test = Mammal("Tom", "Cat", "Meow")

    def test_initialisation_is_correct(self):
        self.assertEqual("Tom", self.test.name)
        self.assertEqual("Cat", self.test.type)
        self.assertEqual("Meow", self.test.sound)
        self.assertEqual("animals", self.test._Mammal__kingdom)

    def test_make_sound(self):
        expected_result = "Tom makes Meow"
        result = self.test.make_sound()

        self.assertEqual(expected_result, result)

    def test_get_kingdom(self):
        result = self.test.get_kingdom()
        self.assertEqual("animals", result)

    def test_info(self):
        expected_result = "Tom is of type Cat"
        result = self.test.info()

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
