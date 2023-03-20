import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        ...


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return (self.base * self.height) / 2


class Circle(Shape):
    PI = math.pi

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return Circle.PI * (self.radius ** 2)


class Trapezoid(Shape):

    def __init__(self, base_a, base_b, height):
        self.base_a = base_a
        self.base_b = base_b
        self.height = height

    def calculate_area(self):
        return (self.base_a + self.base_b) / 2 * self.height


class Rhombus(Shape):

    def __init__(self, diagonal_a, diagonal_b):
        self.diagonal_a = diagonal_a
        self.diagonal_b = diagonal_b

    def calculate_area(self):
        return (self.diagonal_a * self.diagonal_b) / 2


class AreaCalculator:

    def __init__(self, shapes_list):
        self.shapes = shapes_list

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise TypeError("`shapes` should be of type `list`.")

        self.__shapes = value

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()

        return total


# it hass few more shapes than TASK CONDITION

shapes = [Rectangle(1, 6), Triangle(2, 3), Circle(5), Trapezoid(5, 10, 3), Rhombus(5, 10)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)

#################################### TASK CONDITION ############################
'''
                    4.	Shapes
You are provided with code containing class Rectangle and class AreaCalculator. 
Refactor the code using the Open/Closed Principle so that the code is open for 
extension (adding more shapes) but closed for modification.

 '''


# Code to fix
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height


class AreaCalculator:

    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.width * shape.height

        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

'''

_______________________________________________
Example

Test Code	(no input data in this task)


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)


Output

The total area is:  9.0




'''
