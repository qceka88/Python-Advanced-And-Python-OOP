from project.factory.paint_factory import PaintFactory
from unittest import main, TestCase


class TestPaintFactory(TestCase):

    def setUp(self) -> None:
        self.factory = PaintFactory("Name", 15)
        self.factory02 = PaintFactory("Name02", 15)
        self.factory02.ingredients = {"white": 2,
                                      "yellow": 2,
                                      "blue": 2,
                                      }

    def test_initialisation_is_correct(self):
        self.assertEqual("Name", self.factory.name)
        self.assertEqual(15, self.factory.capacity)
        self.assertEqual({}, self.factory.ingredients)
        valid_ingredients = ["white", "yellow", "blue", "green", "red"]
        self.assertEqual(valid_ingredients, self.factory.valid_ingredients)

    def test_add_ingredient_not_allowed_ingredient_raises_type_error(self):
        with self.assertRaises(TypeError) as ty:
            self.factory.add_ingredient("test", 5)

        self.assertEqual("Ingredient of type test not allowed in PaintFactory", str(ty.exception))

    def test_add_ingredient_insufficient_capacity_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.factory.add_ingredient('red', 20)

        self.assertEqual("Not enough space in factory", str(ve.exception))

    def test_add_ingredient_valid_type(self):
        ingredients = {"white": 1, "yellow": 1, "blue": 1, "green": 1, "red": 1}

        for product, quantity in ingredients.items():
            self.factory.add_ingredient(product, quantity)

        self.assertEqual(ingredients, self.factory.ingredients)

        for product, quantity in ingredients.items():
            self.factory.add_ingredient(product, quantity)

        expected = {"white": 2, "yellow": 2, "blue": 2, "green": 2, "red": 2}
        self.assertEqual(expected, self.factory.ingredients)

    def test_remove_non_existing_ingredient(self):
        with self.assertRaises(KeyError) as ke:
            self.factory02.remove_ingredient("red", 1)

        self.assertEqual("'No such ingredient in the factory'", str(ke.exception))

    def test_remove_ingredient_with_insufficient_quantity(self):
        with self.assertRaises(ValueError) as ve:
            self.factory02.remove_ingredient("white", 5)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(ve.exception))

    def test_remove_ingredient_valid_input(self):
        self.factory02.remove_ingredient("white", 1)
        self.factory02.remove_ingredient("yellow", 1)

        expected_result = {"white": 1, "yellow": 1, "blue": 2}
        self.assertEqual(expected_result, self.factory02.ingredients)

    def test_products(self):
        expected_result = {"white": 2, "yellow": 2, "blue": 2}
        self.assertEqual(expected_result, self.factory02.products)
        self.assertEqual({}, self.factory.products)

    def test_can_add(self):
        positive = self.factory02.can_add(3)
        negative = self.factory02.can_add(25)

        self.assertTrue(positive)
        self.assertFalse(negative)

    def test__repr__(self):
        expected_result = "Factory name: Name02 with capacity 15.\n" \
                          "white: 2\nyellow: 2\nblue: 2\n"
        result = self.factory02.__repr__()
        self.assertEqual(expected_result, result)

        expected_result02 = "Factory name: Name with capacity 15.\n"
        result02 = self.factory.__repr__()
        self.assertEqual(expected_result02, result02)


if __name__ == '__main__':
    main()
