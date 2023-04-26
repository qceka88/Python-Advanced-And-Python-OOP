from functools import reduce

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    def __init__(self):
        self.horses: [Appaloosa, Thoroughbred] = []
        self.jockeys: [Jockey] = []
        self.horse_races: [HorseRace] = []

    @property
    def valid_breeds(self):
        return {
            "Appaloosa": Appaloosa,
            "Thoroughbred": Thoroughbred,
        }

    @staticmethod
    def find_data(some_value, attribute, some_list):
        for some_object in some_list:
            if getattr(some_object, attribute) == some_value:
                return some_object

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type in self.valid_breeds:
            if self.find_data(horse_name, "name", self.horses):
                raise Exception(f"Horse {horse_name} has been already added!")

            new_horse = self.valid_breeds[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)

            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.find_data(jockey_name, "name", self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)

        return f"Jockey {new_jockey.name} is added."

    def create_horse_race(self, race_type: str):
        if self.find_data(race_type, "race_type", self.horse_races):
            raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.find_data(jockey_name, "name", self.jockeys)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        for i in range(len(self.horses) - 1, -1, -1):
            horse = self.horses[i]
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                if jockey.horse:
                    return f"Jockey {jockey.name} already has a horse."
                else:
                    horse.is_taken = True
                    jockey.horse = horse
                    return f"Jockey {jockey.name} will ride the horse {horse.name}."
        else:
            raise Exception(f"Horse breed {horse_type} could not be found!")

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.find_data(race_type, "race_type", self.horse_races)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.find_data(jockey_name, "name", self.jockeys)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey.name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey.name} has been already added to the {race.race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey.name} added to the {race.race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.find_data(race_type, "race_type", self.horse_races)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        # TODO: check with different method to find winner
        jockey = reduce(lambda a, b: a if a.horse.speed > b.horse.speed else b, race.jockeys)

        return f"The winner of the {race.race_type} race, with a speed of {jockey.horse.speed}km/h is {jockey.name}! " \
               f"Winner's horse: {jockey.horse.name}."
