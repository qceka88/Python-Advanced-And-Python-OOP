from project.hardware.hardware import Hardware
from math import floor


class PowerHardware(Hardware):

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name=name,
                         hardware_type="Power",
                         capacity=floor(capacity * 0.25),
                         memory=floor(memory * 1.75))
