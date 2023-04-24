from project.software.software import Software
from math import floor


class LightSoftware(Software):

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name,
                         software_type="Light",
                         capacity_consumption=floor(capacity_consumption * 1.5),
                         memory_consumption=floor(memory_consumption * 0.5))
