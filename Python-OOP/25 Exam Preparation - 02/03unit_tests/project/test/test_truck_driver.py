from project.truck_driver import TruckDriver
from unittest import main, TestCase


class TestTruckDriver(TestCase):

    def setUp(self) -> None:
        self.driver = TruckDriver("Ivan", 10.5)

    def test_initialisation_is_correct(self):
        self.assertEqual("Ivan", self.driver.name)
        self.assertEqual(10.5, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0.0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1

        self.assertEqual("Ivan went bankrupt.", str(ve.exception))

        self.driver.earned_money = 10
        self.assertEqual(10, self.driver.earned_money)

    def test_add_cargo_offer_existing_cargo_raises_exception(self):
        self.driver.available_cargos = {"Sofia": 50}

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Sofia", 50)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_for_valid_input(self):
        test_cargos = {"Kaspichan": 50, "Sofia": 400, "Burgas": 100}

        for location, distance in test_cargos.items():
            result = self.driver.add_cargo_offer(location, distance)
            expected_result = f"Cargo for {distance} to {location} was added as an offer."
            self.assertEqual(expected_result, result)

        self.assertEqual(test_cargos, self.driver.available_cargos)

    def test_drive_best_cargo_offer_for_non_existing_offer(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer_for_valid_input(self):
        self.driver.available_cargos = {"Kaspichan": 50, "Sofia": 400, "Burgas": 100}

        result = self.driver.drive_best_cargo_offer()

        self.assertEqual(4180, self.driver.earned_money)
        self.assertEqual(400, self.driver.miles)
        self.assertEqual("Ivan is driving 400 to Sofia.", result)

    def test_drive_best_cargo_offer_goes_bankrupt(self):
        self.driver.money_per_mile = 0.01
        self.driver.available_cargos = {"Porto": 100_000}

        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()

        self.assertEqual("Ivan went bankrupt.", str(ve.exception))

    def test_check_for_activities_proper_working(self):
        self.driver.earned_money = 300_000
        self.driver.check_for_activities(30_000)
        expected_result = 300_000 - (2400 + 1350 + 10_000 + 22_500)
        self.assertEqual(expected_result, self.driver.earned_money)

    def test_eat_proper_working(self):
        self.driver.earned_money = 40
        self.driver.eat(250)
        self.assertEqual(20, self.driver.earned_money)

        self.driver.eat(250)
        self.assertEqual(0, self.driver.earned_money)

    def test_sleep_proper_working(self):
        self.driver.earned_money = 90
        self.driver.sleep(1000)
        self.assertEqual(45, self.driver.earned_money)

        self.driver.sleep(1000)
        self.assertEqual(0, self.driver.earned_money)

    def test_pump_gas_proper_working(self):
        self.driver.earned_money = 1000
        self.driver.pump_gas(1500)
        self.assertEqual(500, self.driver.earned_money)
        self.driver.pump_gas(1500)

        self.assertEqual(0, self.driver.earned_money)

    def test_repair_truck_proper_working(self):
        self.driver.earned_money = 15_000
        self.driver.repair_truck(10_000)
        self.assertEqual(7500, self.driver.earned_money)
        self.driver.repair_truck(10_000)

        self.assertEqual(0, self.driver.earned_money)

    def test__repr__(self):
        self.assertEqual("Ivan has 0 miles behind his back.", str(self.driver))


if __name__ == '__main__':
    main()
