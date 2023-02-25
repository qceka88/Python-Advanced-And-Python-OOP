from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def calculate_area(self):
        return pi * (self.__radius ** 2)

    def calculate_perimeter(self):
        return pi * (self.__radius * 2)


class Rectangle:

    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return (self.__width + self.__height) * 2


# Part below is part from automatic judge system from SoftUni
circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

#################################### TASK CONDITION ############################
'''
                  4.	Shapes
Create an abstract class Shape with abstract methods calculate_area and calculate_perimeter. 
Create classes Circle (receives radius upon initialization) and 
Rectangle (receives height and width upon initialization) that implement those 
methods (returning the result). The fields of Circle and Rectangle should be private.
Submit all the classes and your imports in the judge system

_______________________________________________
Example_01

Test Code	(no input data in this task)

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

Output
78.53981633974483
31.41592653589793

_______________________________________________
Example_01

Test Code	(no input data in this task)

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

Output
200
60

'''
