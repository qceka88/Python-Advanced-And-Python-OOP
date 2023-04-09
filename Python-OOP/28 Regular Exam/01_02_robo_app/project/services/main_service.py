from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, MainService.CAPACITY)

    def details(self):
        robot_names = " ".join(r.name for r in self.robots) if self.robots else "none"
        message = f"{self.name} Main Service:\nRobots: {robot_names}"

        return message
