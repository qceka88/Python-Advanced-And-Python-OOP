from project.train.train import Train
from unittest import main, TestCase


class TestTrain(TestCase):

    def setUp(self) -> None:
        self.train = Train("Burgas", 5)
        self.train02 = Train("Yambol", 5)
        self.train02.passengers = ["test01", "test02", "test03", "test04", "test05"]

    def test_initialisation_is_correct(self):
        self.assertEqual("Burgas", self.train.name)
        self.assertEqual(5, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_class_attributes_are_correct(self):
        self.assertEqual("Train is full", Train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", Train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", Train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", Train.PASSENGER_ADD)
        self.assertEqual("Removed {}", Train.PASSENGER_REMOVED)
        self.assertEqual(0, Train.ZERO_CAPACITY)

    def test_add_for_full_train_with_passengers(self):
        with self.assertRaises(ValueError) as ve:
            self.train02.add("TEST")

        self.assertEqual(Train.TRAIN_FULL, str(ve.exception))

    def test_add_for_existing_passenger(self):
        passengers = ["test01", "test02", "test03", "test04"]
        [self.train.add(p) for p in passengers]

        with self.assertRaises(ValueError) as ve:
            self.train.add("test03")

        self.assertEqual("Passenger test03 Exists", str(ve.exception))

    def test_add_successfully_passenger(self):
        result = self.train.add("Test Passenger")

        self.assertEqual("Added passenger Test Passenger", result)

    def test_remove_for_removing_non_existing_passenger(self):
        with self.assertRaises(ValueError) as ve:
            self.train.remove("Non Existing")

        self.assertEqual(Train.PASSENGER_NOT_FOUND, str(ve.exception))

    def test_remove_for_removing_existing_passenger(self):
        result = self.train02.remove("test04")

        self.assertEqual("Removed test04", result)


if __name__ == '__main__':
    main()
