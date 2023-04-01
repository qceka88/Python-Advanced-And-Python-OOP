from project.plantation import Plantation
from unittest import main, TestCase


class TestPlantation(TestCase):

    def setUp(self):
        self.plantation = Plantation(3)

    def test_initialisation_is_correct(self):
        self.assertEqual(3, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_setter(self):
        with self.assertRaises(ValueError) as ve:
            plantation = Plantation(-1)

        self.assertEqual("Size must be positive number!", str(ve.exception))

        self.plantation.size = 5
        self.assertEqual(5, self.plantation.size)

    def test_hire_worker_for_existing_worker_raises_value_error(self):
        self.plantation.workers = ["Worker01", "Worker02"]

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Worker02")

        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_for_valid_input(self):
        self.plantation.workers = ["Worker01", "Worker02"]

        result = self.plantation.hire_worker("Worker03")

        self.assertEqual("Worker03 successfully hired.", result)
        self.assertEqual("Worker03", self.plantation.workers[2])
        self.assertEqual(3, len(self.plantation.workers))

    def test__len__(self):
        self.assertEqual(0, len(self.plantation))
        self.plantation.plants = {"Worker01": ["plant01", 'plant02'], "Worker02": ["plant01"]}
        self.assertEqual(3, len(self.plantation))

    def test_planting_with_invalid_worker_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Worker01", "plant01")

        self.assertEqual("Worker with name Worker01 is not hired!", str(ve.exception))

    def test_planting_for_exceeded_size_raises_value_error(self):
        self.plantation.workers = ["Worker01", "Worker02"]
        self.plantation.plants = {"Worker01": ["plant01", 'plant02'], "Worker02": ["plant01"]}

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Worker01", "plant03")

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_for_experienced_worker_valid_input(self):
        self.plantation.workers = ["Worker01", "Worker02"]
        self.plantation.plants = {"Worker01": ["plant01"], "Worker02": ["plant01"]}

        result = self.plantation.planting("Worker01", "plant02")
        self.assertEqual("Worker01 planted plant02.", result)
        self.assertEqual("plant02", self.plantation.plants["Worker01"][1])

    def test_planting_for_inexperienced_worker_valid_input(self):
        self.plantation.workers = ["Worker01"]

        result = self.plantation.planting("Worker01", "plant01")
        self.assertEqual("Worker01 planted it's first plant01.", result)
        self.assertEqual("plant01", self.plantation.plants["Worker01"][0])

    def test__str__(self):
        self.plantation.workers = ["Worker01", "Worker02"]
        self.plantation.plants = {"Worker01": ["plant01", 'plant02'], "Worker02": ["plant01"]}

        result = str(self.plantation)
        expected_result = "Plantation size: 3\nWorker01, Worker02\nWorker01 planted: plant01, plant02\nWorker02 planted: plant01"

        self.assertEqual(expected_result, result)

    def test__repr__(self):
        self.plantation.workers = ["Worker01", "Worker02"]

        result = repr(self.plantation)
        expected_result = "Size: 3\nWorkers: Worker01, Worker02"

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
