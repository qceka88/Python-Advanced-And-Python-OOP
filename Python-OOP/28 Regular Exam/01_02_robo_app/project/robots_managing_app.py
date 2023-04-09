from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    def __init__(self):
        self.robots: [BaseRobot] = []
        self.services: [BaseService] = []

    @property
    def valid_services(self):
        return {
            "MainService": MainService,
            "SecondaryService": SecondaryService,
        }

    @property
    def valid_robots(self):
        return {
            "MaleRobot": MaleRobot,
            "FemaleRobot": FemaleRobot,
        }

    @staticmethod
    def find_data(value, attribute, some_list):
        for obj in some_list:
            if getattr(obj, attribute) == value:
                return obj

    def add_service(self, service_type: str, name: str):
        try:
            service = self.valid_services[service_type](name)

        except KeyError:
            raise Exception("Invalid service type!")

        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        try:
            robot = self.valid_robots[robot_type](name, kind, price)

        except KeyError:
            raise Exception("Invalid robot type!")

        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.find_data(robot_name, "name", self.robots)
        service = self.find_data(service_name, "name", self.services)

        if robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ == "MainService" or \
                robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ == "SecondaryService":
            if len(service.robots) == service.capacity:
                raise Exception("Not enough capacity for this robot!")

            service.robots.append(robot)
            self.robots.remove(robot)
            return f"Successfully added {robot_name} to {service_name}."

        else:
            return "Unsuitable service."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.find_data(service_name, "name", self.services)
        robot = self.find_data(robot_name, "name", service.robots)

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.find_data(service_name, "name", self.services)
        [r.eating() for r in service.robots]

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.find_data(service_name, "name", self.services)
        total_price = sum([r.price for r in service.robots])

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        message = [s.details() for s in self.services]
        return '\n'.join(message)

