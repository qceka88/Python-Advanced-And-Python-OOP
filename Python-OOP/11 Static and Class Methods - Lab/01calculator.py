from functools import reduce


# ####################### variant01 ####################

class Calculator:

    @staticmethod
    def add(*numbers):
        return sum(numbers)

    @staticmethod
    def multiply(*numbers):
        return reduce(lambda a, b: a * b, numbers)

    @staticmethod
    def divide(*numbers):
        return reduce(lambda a, b: a / b, numbers)

    @staticmethod
    def subtract(*numbers):
        return reduce(lambda a, b: a - b, numbers)


####################### variant02 ####################

class Calculator:

    @staticmethod
    def return_result(operator, *numbers):  # Basically, this is useless method. It`s just for practice.
        return reduce(lambda a, b: eval(str(a) + operator + str(b)), numbers)

    @staticmethod
    def add(*numbers):
        return Calculator.return_result("+", *numbers)

    @staticmethod
    def multiply(*numbers):
        return Calculator.return_result("*", *numbers)

    @staticmethod
    def divide(*numbers):
        return Calculator.return_result("/", *numbers)

    @staticmethod
    def subtract(*numbers):
        return Calculator.return_result("-", *numbers)


# Part below is part from automatic judge system from SoftUni
print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))


#################################### TASK CONDITION ############################
'''
                     1.	Calculator
Create a class called Calculator that has the following static methods:
•	add(*args) - sums all the arguments passed to the function and returns the result
•	multiply(*args) - multiplies all the numbers and returns the result
•	divide(*args) - divides all the numbers (starting from the first one) and returns the result
•	subtract(*args) - subtracts all the numbers (starting from the first one) and returns the result

_______________________________________________
Example

Test Code    (no input data in this task)

print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))


Output
19
30
50.0
70

'''
