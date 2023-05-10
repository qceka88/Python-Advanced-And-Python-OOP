from project.toy_store import ToyStore
from unittest import main, TestCase


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.store = ToyStore()

    def test_initialisation_is_correct(self):
        expected_shelf = {"A": None, "B": None,
                          "C": None, "D": None,
                          "E": None, "F": None,
                          "G": None,
                          }

        self.assertEqual(expected_shelf, self.store.toy_shelf)

    def test_add_toy_invalid_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("invalid", "Train")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_same_toy_on_shelf_raises_exception(self):
        self.store.add_toy("A", "Car")

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Car")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_for_taken_shelf_raises_exception(self):
        self.store.add_toy("D", "Car")

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("D", "Plane")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_for_valid_data(self):
        result01 = self.store.add_toy("A", "Plane")
        self.assertEqual("Toy:Plane placed successfully!", result01)

        result02 = self.store.add_toy("F", "Bike")
        self.assertEqual("Toy:Bike placed successfully!", result02)

        self.assertEqual("Plane", self.store.toy_shelf["A"])
        self.assertEqual("Bike", self.store.toy_shelf["F"])

    def test_remove_toy_for_invalid_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("K", "Truck")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_for_invalid_toy_raises_exception(self):
        self.store.toy_shelf["G"] = "Rocket"

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("G", "Ball")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_for_valid_input(self):
        self.store.add_toy("D", "Plane")
        result = self.store.remove_toy("D", "Plane")

        self.assertEqual(f"Remove toy:Plane successfully!", result)
        self.assertIsNone(self.store.toy_shelf["D"])


if __name__ == '__main__':
    main()
