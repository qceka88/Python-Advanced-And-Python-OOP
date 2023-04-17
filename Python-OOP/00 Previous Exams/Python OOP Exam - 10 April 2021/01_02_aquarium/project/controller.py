from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: [BaseAquarium] = []

    @property
    def valid_aquarium(self):
        return {
            "FreshwaterAquarium": FreshwaterAquarium,
            "SaltwaterAquarium": SaltwaterAquarium,
        }

    @property
    def valid_decoration(self):
        return {
            "Ornament": Ornament,
            "Plant": Plant,
        }

    @property
    def valid_fish(self):
        return {
            "FreshwaterFish": FreshwaterFish,
            "SaltwaterFish": SaltwaterFish,

        }

    @staticmethod
    def find_data(value, attribute, some_list):
        for obj in some_list:
            if getattr(obj, attribute) == value:
                return obj

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        try:
            aquarium = self.valid_aquarium[aquarium_type](aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."

        except KeyError:
            return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        try:
            decoration = self.valid_decoration[decoration_type]()
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."

        except KeyError:
            return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.find_data(aquarium_name, "name", self.aquariums)
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if aquarium and decoration != "None":
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

        return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        try:
            fish = self.valid_fish[fish_type](fish_name, fish_species, price)
        except KeyError:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.find_data(aquarium_name, "name", self.aquariums)

        f = fish.__class__.__name__.replace("Fish", "")
        a = aquarium.__class__.__name__.replace("Aquarium", "")

        if f != a:
            return "Water not suitable."
        else:
            return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.find_data(aquarium_name, "name", self.aquariums)
        aquarium.feed()

        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.find_data(aquarium_name, "name", self.aquariums)
        fish_price = sum(f.price for f in aquarium.fish)
        decoration_price = sum(d.price for d in aquarium.decorations)

        total = fish_price + decoration_price
        return f"The value of Aquarium {aquarium_name} is {total:.2f}."

    def report(self):
        message = [str(a) for a in self.aquariums]
        return '\n'.join(message)
