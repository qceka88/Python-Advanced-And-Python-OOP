##################################### variant 01 #####################################
def rectangle(length, width):
    def area():
        area = length * width
        return f"Rectangle area: {area}"

    def perimeter():
        perimeter = (length + width) * 2
        return f"Rectangle perimeter: {perimeter}"

    try:
        return area() + "\n" + perimeter()
    except TypeError:
        return "Enter valid values!"


print(rectangle(2, 10))
print(rectangle('2', 10))


##################################### variant 02 #####################################

class Rectangle:

    def __init__(self, some_tuple):
        self.length, self.width = some_tuple
        self.message = ''

    def rectangle(self):
        try:
            def area():
                area = self.length * self.width
                return f"Rectangle area: {area}"

            def perimeter():
                perimeter = (self.length + self.width) * 2
                return f"Rectangle perimeter: {perimeter}"

            return area() + '\n' + perimeter()
        except TypeError:
            return "Enter valid values!"

    def __repr__(self):
        return self.message


def rectangle(*args):
    output = Rectangle(args).rectangle()
    return output


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