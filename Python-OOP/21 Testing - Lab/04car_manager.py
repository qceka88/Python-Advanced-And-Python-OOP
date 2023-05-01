from unittest import main, TestCase


class TestCar(TestCase):

    def setUp(self) -> None:
        self.car = Car("Skoda", "Octavia", 10, 55)

    def test_initialisation_is_correct(self):
        self.assertEqual("Skoda", self.car.make)
        self.assertEqual("Octavia", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(55, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            test = Car("", "Octavia", 10, 55)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            test = Car("Skoda", "", 10, 55)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_setter_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            test = Car("Skoda", "Octavia", 0, 55)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            test = Car("Skoda", "Octavia", 10, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_setter_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_for_negative_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_for_valid_input(self):
        self.car.refuel(5)
        self.car.refuel(5)
        self.assertEqual(10, self.car.fuel_amount)

        self.car.refuel(100)
        self.assertEqual(55, self.car.fuel_amount)

    def test_drive_insufficient_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(500)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_for_valid_data(self):
        self.car.refuel(50)
        self.car.drive(100)
        self.assertEqual(40, self.car.fuel_amount)
        self.car.drive(100)
        self.assertEqual(30, self.car.fuel_amount)


if __name__ == "__main__":
    main()


#################################### TASK CONDITION ############################
'''
                           4.	Car Manager
You are provided with a simple project containing only one class - Car. 
The provided class is simple - its main point is to represent some of the 
functionality of a Car. Each car contains information about its make, model, 
fuel consumption, fuel amount, and fuel capacity. Also, each Car can add some 
fuel to its tank by refueling and can travel distance by driving. In order to be driven, 
our Car needs to have enough fuel. Everything in the provided skeleton is working perfectly 
fine, and you mustn't change it.
Your job now is to write unit tests on the provided project and its functionality. 

You should test every part of the code inside the Car class:
•	You should test the constructor
•	You should test all the methods and validations inside the class
Constraints
•	Everything in the provided skeleton is working perfectly fine
•	You must not change anything in the project structure
•	Any part of validation should be tested
•	There is no limit on the tests you can write but keep 
your attention on the main functionality
Note: You are not allowed to change the structure of the provided code

"Brum…Brum…Brum-suuuututututu…"

 '''


# Code to test
class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed

