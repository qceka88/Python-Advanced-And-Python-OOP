from project.truck_driver import TruckDriver
from unittest import main, TestCase


class TruckDriverTest(TestCase):

    def setUp(self):
        self.driver = TruckDriver("Name", 10.5)

    def test_initialisation_is_correct(self):
        self.assertEqual("Name", self.driver.name)
        self.assertEqual(10.5, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0.0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1

        self.assertEqual("Name went bankrupt.", str(ve.exception))
        self.driver.earned_money = 10
        self.assertEqual(10, self.driver.earned_money)

    def test_add_cargo_method_adding_and_raises_exception(self):
        self.driver.available_cargos = {"Varna": 100}

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Varna", 100)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_method_adding_new_location(self):
        result = self.driver.add_cargo_offer("Varna", 100)
        self.assertEqual("Cargo for 100 to Varna was added as an offer.", result)

        self.assertEqual({"Varna": 100}, self.driver.available_cargos)

    def test_driver_best_cargo_offer_return_no_offers(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_driver_best_cargo_offer_method_proper_work(self):
        self.driver.available_cargos = {"Burgas": 50, "Varna": 100, "Sofia": 80}

        result = self.driver.drive_best_cargo_offer()

        self.assertEqual(100, self.driver.miles)
        self.assertEqual(1050, self.driver.earned_money)
        self.assertEqual("Name is driving 100 to Varna.", result)

    def test_driver_best_cargo_offer_method_expensive_location(self):
        self.driver.money_per_mile = 0.01
        self.driver.available_cargos = {"Moon": 1_000_000}

        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()

        self.assertEqual("Name went bankrupt.", str(ve.exception))

    def test_check_for_activities_method(self):
        self.driver.earned_money = 100_000
        self.driver.check_for_activities(15_000)
        self.assertEqual(85625, self.driver.earned_money)

    def test_eat_method(self):
        self.driver.earned_money = 40
        self.driver.eat(250)

        self.assertEqual(20, self.driver.earned_money)

    def test_sleep_method(self):
        self.driver.earned_money = 90
        self.driver.sleep(1000)

        self.assertEqual(45, self.driver.earned_money)

    def test_pump_gas_method(self):
        self.driver.earned_money = 1000
        self.driver.pump_gas(1500)

        self.assertEqual(500, self.driver.earned_money)

    def test_repair_truck_method(self):
        self.driver.earned_money = 15_000
        self.driver.repair_truck(10_000)

        self.assertEqual(7500, self.driver.earned_money)

    def test__repr__method(self):
        self.assertEqual("Name has 0 miles behind his back.", repr(self.driver))


if __name__ == '__main__':
    main()
