class Cup:

    def __init__(self, *data):
        self.size, self.quantity = data

    def fill(self, milliliters):
        if self.quantity + milliliters <= self.size:
            self.quantity += milliliters

    def status(self):
        return self.size - self.quantity


# Part below is part from automatic judge system from SoftUni
cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())


#################################### TASK CONDITION ############################
'''
                     4.	Cup
Create a class called Cup. Upon initialization it should receive 
size (number) and quantity (a number representing how much liquid is in it). 
The class should have two methods:
•	fill(milliliters) which will increase the amount of liquid in the cup 
with the given milliliters (if there is space in the cup, otherwise ignore). 
•	status() which will return the amount of free space left in the cup. 
Submit only the class in the judge system. Do not forget to test your code.
_______________________________________________
Example

Test Code	(no input data in this task)

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())

Output
50
10

'''
