from project.controller import Controller
from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish

c = Controller()

aquariums = {"SaltwaterAquarium": "Salt", "FreshwaterAquarium": "Fresh", "PepsiAquarium": "Lemon"}
[print(c.add_aquarium(t, n)) for t, n in aquariums.items()]

base_decorations_list = ["Plant", "Ornament", "Ornament", "Plant", "Snail",
                         "Plant", "Ornament", "", "Pepsi", "Ornament", "Plant"]
[print(c.add_decoration(decor)) for decor in base_decorations_list]

decorations_list02 = ["Plant", "Ornament", "Ornament", "Plant", "Snail"]
decorations_list03 = ["Plant", "Ornament", "", "Pepsi", "Ornament", "Plant"]
[print(c.insert_decoration("Salt", d)) for d in decorations_list02]
[print(c.insert_decoration("Fresh", d)) for d in decorations_list03]
# [print(c.insert_decoration("Lemon", d)) for d in decorations_list02]

fish_fresh_list = [
    ("FreshwaterFish", "Nemo", "GoldFish", 5.5),
    ("FreshwaterFish", "Ariel", "Mermaid", 250.5),
    ("FreshwaterFish", "Manuel", "Whale", 45),
    ("FreshwaterFish", "Jeffry", "Octopus", 50.5),
]
[print(c.add_fish("Fresh", t, n, s, p)) for t, n, s, p in fish_fresh_list]

fish_salt_list = [
    ("SaltwaterFish", "NemoSalt", "GoldFish", 6.5),
    ("SaltwaterFish", "ArielSalt", "Mermaid", 280.5),
    ("SaltwaterFish", "Armando", "Shark", 44),
    ("SaltwaterFish", "Samuel", "Octopus", 56.5),
]
[print(c.add_fish("Salt", t, n, s, p)) for t, n, s, p in fish_salt_list]
fish_mixed_list = [
    ("SaltwaterFish", "NemoSalt", "GoldFish", 6.5),
    ("FreshwaterFish", "Manuel", "Whale", 45),
    ("SaltwaterFish", "ArielSalt", "Mermaid", 280.5),
    ("FreshwaterFish", "Jeffry", "Octopus", 50.5),
]
[print(c.add_fish("Fresh", t, n, s, p)) for t, n, s, p in fish_mixed_list]

print(c.feed_fish("Salt"))
print(c.feed_fish("Fresh"))

print(c.calculate_value("Salt"))
print(c.calculate_value("Fresh"))

print(c.report())
