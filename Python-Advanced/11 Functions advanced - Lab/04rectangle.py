class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def main_meth(self):
        try:
            return self.result_message(self.perimeter(), self.area())
        except TypeError:
            return self.error_message()

    def result_message(self, perimeter, area):
        return f'Rectangle area: {area}\nRectangle perimeter: {perimeter}'

    def error_message(self):
        return 'Enter valid values!'

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width


def rectangle(*args):
    output = Rectangle(*args).main_meth()
    return output

# This part below is part from automatic test code from Judge system in SoftUni
print(rectangle(2, 10))
print(rectangle('2', 10))


#################################### TASK CONDITION ############################
'''
                           4.	Rectangle
Create a function called rectangle(). It must have two parameters - length and width. 
First, you need to check if the given arguments are integers:
•	If one/ both of them is/ are NOT an integer/s, return the string "Enter valid values!"
Create two inner functions:
•	area() - returns the area of the rectangle with the given length and width
•	perimeter() - returns the perimeter of the rectangle with the given length and width
In the end, the rectangle function should return a string containing the 
area and the perimeter of a rectangle in the following format:
"Rectangle area: {ract_area}
Rectangle perimeter: {rect_perim}"

_______________________________________________
Example_01

Test Code	(no input data in this task)
print(rectangle(2, 10))	

Output
Rectangle area: 20
Rectangle perimeter: 24

_______________________________________________
Example_02

Test Code	(no input data in this task)
print(rectangle('2', 10))	

Output
"Enter valid values!"


'''