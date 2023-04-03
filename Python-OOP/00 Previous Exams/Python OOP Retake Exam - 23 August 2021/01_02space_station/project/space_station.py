from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.unsuccessful_missions = 0

    @property
    def valid_astronauts(self):
        return {
            "Biologist": Biologist,
            "Geodesist": Geodesist,
            "Meteorologist": Meteorologist,
        }

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        try:
            astro = self.valid_astronauts[astronaut_type](name)
            self.astronaut_repository.add(astro)
            return f"Successfully added {astronaut_type}: {astro.name}."

        except KeyError:
            raise Exception("Astronaut type is not valid!")

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet_new = Planet(name)
        planet_new.items.extend(items.split(', '))
        self.planet_repository.planets.append(planet_new)

        return f"Successfully added Planet: {planet_new.name}."

    def retire_astronaut(self, name: str):
        astro = self.astronaut_repository.find_by_name(name)
        if not astro:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astro)

        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        oxygen_amount = 10
        [a.increase_oxygen(oxygen_amount) for a in self.astronaut_repository.astronauts]

    def find_crew_members_for_mission(self):
        astronauts = []
        for member in sorted(self.astronaut_repository.astronauts, key=lambda a: -a.oxygen):
            if member.oxygen > 30:
                astronauts.append(member)
                if len(astronauts) == 5: break

        return astronauts

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        crew = self.find_crew_members_for_mission()

        if not crew:
            raise Exception("You need at least one astronaut to explore the planet!")

        for member in crew:
            while planet.items:
                if member.oxygen - member.breathe_amount() < 0:
                    break

                current_item = planet.items.pop()
                member.backpack.append(current_item)
                member.breathe()

            if not planet.items:
                astronauts = len([m for m in crew if m.backpack])
                message = f"Planet: {planet_name} was explored. {astronauts} astronauts participated in collecting items."
                self.successful_missions += 1
                return message

        else:
            self.unsuccessful_missions += 1
            return "Mission is not completed."

    def report(self):
        message = [f"{self.successful_missions} successful missions!",
                   f"{self.unsuccessful_missions} missions were not completed!",
                   "Astronauts' info:"]
        for astronaut in self.astronaut_repository.astronauts:
            back_pack = f"Backpack items: {', '.join(astronaut.backpack) if astronaut.backpack else 'none'}"
            message.extend([f"Name: {astronaut.name}", f"Oxygen: {astronaut.oxygen}", back_pack])

        return "\n".join(message)

#
# workers_invalid = (("Geodesist", "Gosho"),
#                    ("Meteorologist", "Stavri"),
#                    ("Geodesist", "Unufri"))
#
# single_worker = ("Geodesist", "Gosho")
#
# workers = (("Biologist", "Gosho"),
#            ("Meteorologist", "Stavri"),
#            ("Geodesist", "Unufri"),
#            ("Geodesist", "Pensiq"),
#            ("Biologist", "Silvestar"),
#            ("Meteorologist", "Tosho"),
#            ("Meteorologist", "BaiHui"),)
#
# planetata1 = "Payner"
# items1 = 'disk, silikon, mikrofon, otverka, vibrator, slushalki, Milko Kalaidjiev, kamak, nojica, hartiq'
# # planetata2 = "Mars"
# # items2 = "kamani, izvanzemno, led, marsohodi, spatnici"
#
# station = SpaceStation()
#
# for a in workers_invalid:
#     print(station.add_astronaut(*a))
# # print(station.add_astronaut(*single_worker))
# print(station.add_planet(planetata1, items1))
#
# # print(station.retire_astronaut("Pensiq"))
# # station.recharge_oxygen()
# print(station.send_on_mission("Payner"))
# # [print(f"{a.name} - {a.oxygen}") for a in station.astronaut_repository.astronauts]
# print(station.report())
