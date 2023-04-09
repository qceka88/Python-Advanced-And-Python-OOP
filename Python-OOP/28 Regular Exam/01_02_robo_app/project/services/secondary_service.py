from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, SecondaryService.CAPACITY)

    def details(self):
        robot_names = " ".join(r.name for r in self.robots) if self.robots else "none"
        message = f"{self.name} Secondary Service:\nRobots: {robot_names}"

        return message
