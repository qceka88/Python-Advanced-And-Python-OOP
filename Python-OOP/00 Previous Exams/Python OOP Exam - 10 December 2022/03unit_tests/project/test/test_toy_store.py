from project.toy_store import ToyStore
from unittest import main, TestCase


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.store = ToyStore()

    def test_initialisations_is_correct(self):
        test_shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None}

        for i in range(len(self.store.toy_shelf)):
            r_key = list(test_shelf)[i]
            e_key = list(self.store.toy_shelf)[i]

            self.assertEqual(r_key, e_key)
            r_val, e_val = self.store.toy_shelf[r_key], self.store.toy_shelf[e_key]
            self.assertEqual(r_val, e_val)

    def test_add_toy_searching_invalid_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("Python", "Snake")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_try_to_add_existing_toy_raises_exception(self):
        self.store.toy_shelf["A"] = "Snake"
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Snake")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_try_take_used_taken_shelf_raises_exception(self):
        self.store.toy_shelf["A"] = "Python"
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Snake")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_for_valid_input_data(self):
        result = self.store.add_toy("A", "PythonToy")

        self.assertEqual("Toy:PythonToy placed successfully!", result)
        self.assertEqual("PythonToy", self.store.toy_shelf["A"])

    def test_remove_toy_searching_invalid_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("Python", "Snake")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_for_invalid_toy_name_raises_exception(self):
        self.store.toy_shelf["A"] = "Python"
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "JavScript")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_for_valid_input_data(self):
        self.store.toy_shelf["A"] = "Python"
        result = self.store.remove_toy("A", "Python")

        self.assertEqual("Remove toy:Python successfully!", result)
        self.assertEqual(None, self.store.toy_shelf["A"])


if __name__ == '__main__':
    main()
