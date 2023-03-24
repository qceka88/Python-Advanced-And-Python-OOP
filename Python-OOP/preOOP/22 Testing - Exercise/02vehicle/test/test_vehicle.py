from project.vehicle import Vehicle
from unittest import main, TestCase


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(10.5, 100.5)

    def test_initialisation_is_correct(self):
        self.assertEqual(10.5, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(100.5, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.fuel_consumption, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_method_raises_exception(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_method_is_decrease_fuel(self):
        self.vehicle.drive(2)
        self.assertEqual(8, self.vehicle.fuel)

    def test_refuel_method_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_method_is_refuel_proper(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(1)

        self.assertEqual(1, self.vehicle.fuel)

    def test__str__method(self):
        result = str(self.vehicle)
        expected_result = f"The vehicle has 100.5 " \
                          f"horse power with 10.5 fuel left and 1.25 fuel consumption"

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    main()
