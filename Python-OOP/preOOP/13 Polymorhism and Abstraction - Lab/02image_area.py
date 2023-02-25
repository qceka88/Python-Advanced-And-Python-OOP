class ImageArea:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.get_area() > other

    def __ge__(self, other):
        return self.get_area() >= other

    def __lt__(self, other):
        return self.get_area() < other

    def __le__(self, other):
        return self.get_area() <= other

    def __eq__(self, other):
        return self.get_area() == other

    def __ne__(self, other):
        return self.get_area() != other


# Part below is part from automatic judge system from SoftUni
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 != a2)
print(a1 >= a3)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 <= a2)
print(a1 < a3)

#################################### TASK CONDITION ############################
'''
                          2.	ImageArea
Create a class called ImageArea which will store the width and the height of an image. 
Create a method called get_area() which will return the area of the image. 
We have also to implement all the magic methods for comparison of two 
image areas (>, >=, <, <=, ==, !=), which will compare their areas.

_______________________________________________
Example_01

Test Code	(no input data in this task)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)

Output
True
True

_______________________________________________
Example_02

Test Code	(no input data in this task)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 != a2)
print(a1 >= a3)

Output
False
False

_______________________________________________
Example_03

Test Code	(no input data in this task)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 <= a2)
print(a1 < a3)

Output
True
True

'''