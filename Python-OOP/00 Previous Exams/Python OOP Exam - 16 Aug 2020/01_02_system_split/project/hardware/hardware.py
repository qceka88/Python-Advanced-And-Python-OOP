from project.software.software import Software


class Hardware:

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components: [Software] = []

    def install(self, software: Software):
        if self.capacity < sum(
                s.capacity_consumption for s in self.software_components) + software.capacity_consumption or \
                self.memory < sum(s.memory_consumption for s in self.software_components) + software.memory_consumption:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)

    def uninstall(self, software: Software):
        # TODO: to check is need for existing software from the software_components list
        self.software_components.remove(software)
