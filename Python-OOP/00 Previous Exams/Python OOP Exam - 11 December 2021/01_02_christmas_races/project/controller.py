from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:

    def __init__(self):
        self.cars: [Car] = []
        self.drivers: [Driver] = []
        self.races: [Race] = []

    @property
    def valid_cars(self):
        return {
            "MuscleCar": MuscleCar,
            "SportsCar": SportsCar,
        }

    @staticmethod
    def find_data(value, attribute, some_list):
        for obj in some_list:
            if getattr(obj, attribute) == value:
                return obj

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in self.valid_cars:
            car = self.find_data(model, "model", self.cars)
            if car:
                raise Exception(f"Car {car.model} is already created!")

            new_car = self.valid_cars[car_type](model, speed_limit)
            self.cars.append(new_car)

            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = self.find_data(driver_name, "name", self.drivers)
        if driver:
            raise Exception(f"Driver {driver.name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)

        return f"Driver {new_driver.name} is created."

    def create_race(self, race_name: str):
        race = self.find_data(race_name, "name", self.races)
        if race:
            raise Exception(f"Race {race.name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)

        return f"Race {new_race.name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.find_data(driver_name, "name", self.drivers)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        for i in range(len(self.cars) - 1, -1, -1):
            car = self.cars[i]
            if car.__class__.__name__ == car_type and not car.is_taken:
                if driver.car:
                    old_model = driver.car
                    old_model.is_taken = False
                    driver.car = car
                    car.is_taken = True
                    return f"Driver {driver.name} changed his car from {old_model.model} to {driver.car.model}."
                else:
                    driver.car = car
                    car.is_taken = True
                    return f"Driver {driver_name} chose the car {car.model}."
        else:
            raise Exception(f"Car {car_type} could not be found!")

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.find_data(race_name, "name", self.races)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        driver = self.find_data(driver_name, "name", self.drivers)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver.name} is already added in {race.name} race."

        race.drivers.append(driver)
        return f"Driver {driver.name} added in {race.name} race."

    def start_race(self, race_name: str):
        race = self.find_data(race_name, "name", self.races)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race.name} cannot start with less than 3 participants!")

        winners = []

        for n, driver in enumerate(sorted(race.drivers, key=lambda d: -d.car.speed_limit)):
            if n == 3:
                break
            driver.number_of_wins += 1
            winners.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return '\n'.join(winners)
