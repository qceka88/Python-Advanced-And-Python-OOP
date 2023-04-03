from project.astronaut.astronaut import Astronaut


class AstronautRepository:

    def __init__(self):
        self.astronauts: [Astronaut] = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for astro in self.astronauts:
            if astro.name == name:
                return astro
