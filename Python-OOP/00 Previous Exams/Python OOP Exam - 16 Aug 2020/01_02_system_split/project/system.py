from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware: [Hardware] = []
    _software: [Software] = []

    @staticmethod
    def find_data(some_name, some_list):
        for some_object in some_list:
            if some_object.name == some_name:
                return some_object

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int,
                                  memory_consumption: int):

        hardware = System.find_data(hardware_name, System._hardware)
        if not hardware:
            return "Hardware does not exist"

        new_express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_express_software)
        System._software.append(new_express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int,
                                memory_consumption: int):
        hardware = System.find_data(hardware_name, System._hardware)
        if not hardware:
            return "Hardware does not exist"

        new_light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_light_software)
        System._software.append(new_light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.find_data(hardware_name, System._hardware)
        software = System.find_data(software_name, System._software)

        if not all([hardware, software]):
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        return f"""System Analysis
Hardware Components: {len(System._hardware)}
Software Components: {len(System._software)}
Total Operational Memory: {sum(s.memory_consumption for s in System._software)} / {sum(h.memory for h in System._hardware)}
Total Capacity Taken: {sum(s.capacity_consumption for s in System._software)} / {sum(h.capacity for h in System._hardware)}"""

    @staticmethod
    def system_split():
        message = []
        for component in System._hardware:
            names = ", ".join(
                s.name for s in component.software_components) if component.software_components else "None"
            message.append(f"""Hardware Component - {component.name}
Express Software Components: {len([c for c in component.software_components if c.software_type == "Express"])}
Light Software Components: {len([c for c in component.software_components if c.software_type == "Light"])}
Memory Usage: {sum(c.memory_consumption for c in component.software_components)} / {component.memory}
Capacity Usage: {sum(s.capacity_consumption for s in component.software_components)} / {component.capacity}
Type: {component.hardware_type}
Software Components: {names}""")

        return '\n'.join(message)
