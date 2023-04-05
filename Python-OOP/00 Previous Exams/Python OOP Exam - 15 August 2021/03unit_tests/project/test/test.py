from project.pet_shop import PetShop
from unittest import main, TestCase


class TestPetShop(TestCase):

    def setUp(self) -> None:
        self.shop = PetShop("Test")
        self.shop02 = PetShop("Test02")
        self.shop02.food = {"food01": 100, "food02": 300, "food03": 400}
        self.shop02.pets = ["dog", "cat", "mouse"]

    def test_initialisation(self):
        self.assertEqual("Test", self.shop.name)

    def test_add_food_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_food("test food", 0)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food_valid_input(self):
        food = {"food01": 100, "food02": 300, "food03": 400}
        for name, quantity in food.items():
            result = self.shop.add_food(name, quantity)
            self.assertEqual(f"Successfully added {quantity:.2f} grams of {name}.", result)

        result02 = self.shop.add_food("food01", 300)
        self.assertEqual(f"Successfully added 300.00 grams of food01.", result02)

        expected_food = {"food01": 400, "food02": 300, "food03": 400}
        self.assertEqual(expected_food, self.shop.food)

    def test_add_pet_for_existing_animal_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.shop02.add_pet('dog')

        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_for_valid_input(self):
        animals = ["dog", "cat", "mouse"]

        for animal_name in animals:
            result = self.shop.add_pet(animal_name)
            self.assertEqual(f"Successfully added {animal_name}.", result)

        self.assertEqual(animals, self.shop.pets)

    def test_feed_pet_invalid_pet_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.shop02.feed_pet("food01", "lion")

        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_invalid_food_name(self):
        result = self.shop02.feed_pet("invalid food", "dog")
        self.assertEqual("You do not have invalid food", result)

    def test_feed_pet_insufficient_food(self):
        self.shop02.add_food("test food", 50)
        result = self.shop02.feed_pet("test food", "cat")

        self.assertEqual("Adding food...", result)
        self.assertEqual(1050, self.shop02.food["test food"])

    def test_feed_pet_valid_input(self):
        result = self.shop02.feed_pet("food02", "cat")
        self.assertEqual("cat was successfully fed", result)
        self.assertEqual(200, self.shop02.food["food02"])

    def test__repr__(self):
        expected_result = 'Shop Test02:\nPets: dog, cat, mouse'
        result = repr(self.shop02)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
