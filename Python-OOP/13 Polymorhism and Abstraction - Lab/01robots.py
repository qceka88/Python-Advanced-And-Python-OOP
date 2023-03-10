import abc


class Robot:
    def __init__(self, name):
        self.name = name

    @staticmethod
    @abc.abstractmethod
    def sensors_amount():
        return 1


class MedicalRobot(Robot):

    @staticmethod
    def sensors_amount():
        return 6


class ChefRobot(Robot):

    @staticmethod
    def sensors_amount():
        return 4


class WarRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 12


def number_of_robot_sensors(robot):
    if isinstance(robot, Robot):
        print(robot.sensors_amount())


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')

number_of_robot_sensors(basic_robot)
number_of_robot_sensors(da_vinci)
number_of_robot_sensors(moley)
number_of_robot_sensors(griffin)



#################################### TASK CONDITION ############################
'''
   1.	Robots
Refactor the provided code, so we do not need to do any type-checking. 
The classes should implement the method to return the number of sensors for each type of robot.


Below is code to refactor
'''

class Robot:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        return 1


class MedicalRobot(Robot):
    @staticmethod
    def medical_robot_sensors_amount():
        return 6


class ChefRobot(Robot):
    @staticmethod
    def chef_robot_sensors_amount():
        return 4


class WarRobot(Robot):
    @staticmethod
    def war_robot_sensors_amount():
        return 12


def number_of_robot_sensors(robot):
    if isinstance(robot, Robot):
        print(robot.sensors_amount())
    if isinstance(robot, MedicalRobot):
        print(robot.medical_robot_sensors_amount())
    elif isinstance(robot, ChefRobot):
        print(robot.chef_robot_sensors_amount())
    elif isinstance(robot, WarRobot):
        print(robot.war_robot_sensors_amount())


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')

number_of_robot_sensors(basic_robot)
number_of_robot_sensors(da_vinci)
number_of_robot_sensors(moley)
number_of_robot_sensors(griffin)
