from project.shopping_cart import ShoppingCart
from unittest import main, TestCase


class TestShoppingCart(TestCase):

    def setUp(self):
        self.cart = ShoppingCart("Name", 1000)

    def test_initialisation_is_correct(self):
        self.assertEqual("Name", self.cart.shop_name)
        self.assertEqual(1000, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_name_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "shop"
        with self.assertRaises(ValueError) as ve1:
            self.cart.shop_name = "shop1"

        expected_result = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected_result, str(ve.exception))
        self.assertEqual(expected_result, str(ve1.exception))

    def test_add_to_cart_for_expensive_product_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("Python", 500.5)

        self.assertEqual(f"Product Python cost too much!", str(ve.exception))

    def test_add_to_cart_valid_input(self):
        result = self.cart.add_to_cart("PythonBasic", 50)

        self.assertEqual("PythonBasic product was successfully added to the cart!", result)
        self.assertEqual(50, self.cart.products["PythonBasic"])

    def test_remove_from_cart_invalid_product_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("Python")

        self.assertEqual("No product with name Python in the cart!", str(ve.exception))

    def test_remove_from_cart_for_valid_data(self):
        self.cart.products = {"Python": 50, "C#": 60, "Java": 40}
        result = self.cart.remove_from_cart("C#")

        self.assertEqual(f"Product C# was successfully removed from the cart!", result)
        self.assertEqual({"Python": 50, "Java": 40}, self.cart.products)

    def test__add__(self):
        self.cart.products = {"Python": 50}
        cart_02 = ShoppingCart("NameTwo", 200)
        cart_02.products = {"C#": 60}
        cart03 = self.cart + cart_02

        self.assertEqual("NameNameTwo", cart03.shop_name)
        self.assertEqual(1200, cart03.budget)
        self.assertEqual({"Python": 50, "C#": 60}, cart03.products)

    def test_buy_product_for_expensive_products_raises_value_error(self):
        self.cart.budget = 1
        self.cart.products = {"Python": 50, "C#": 60}

        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()

        self.assertEqual("Not enough money to buy the products! Over budget with 109.00lv!", str(ve.exception))

    def test_buy_product_for_successfully_bought_products(self):
        self.cart.budget = 1500
        self.cart.products = {"Python": 50, "C#": 60}
        result = self.cart.buy_products()

        self.assertEqual(f'Products were successfully bought! Total cost: 110.00lv.', result)


if __name__ == '__main__':
    main()
