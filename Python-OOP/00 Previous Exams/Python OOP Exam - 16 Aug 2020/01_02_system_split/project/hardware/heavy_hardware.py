from project.hardware.hardware import Hardware
from math import floor


class HeavyHardware(Hardware):

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name=name,
                         hardware_type="Heavy",
                         capacity=capacity * 2,
                         memory=floor(memory * 0.75))
