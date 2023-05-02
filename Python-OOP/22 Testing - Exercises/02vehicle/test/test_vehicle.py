import sys

from project.vehicle import Vehicle
from unittest import main, TestCase


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.test = Vehicle(50.5, 135.4)

    def test_initialisation_is_correct(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(50.5, self.test.fuel)
        self.assertEqual(50.5, self.test.capacity)
        self.assertEqual(135.4, self.test.horse_power)
        self.assertEqual(1.25, self.test.fuel_consumption)

    def test_drive_insufficient_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test.drive(sys.maxsize)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_valid_input(self):
        self.test.drive(10)
        self.test.drive(10)

        self.assertEqual(25.5, self.test.fuel)

    def test_refuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test.refuel(sys.maxsize)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_valid_input(self):
        self.test.fuel = 10

        self.test.refuel(5.5)
        self.test.refuel(5.0)

        self.assertEqual(20.5, self.test.fuel)

    def test__str__(self):
        expected_result = f"The vehicle has 135.4 " \
                          f"horse power with 50.5 fuel left and 1.25 fuel consumption"
        result = str(self.test)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
