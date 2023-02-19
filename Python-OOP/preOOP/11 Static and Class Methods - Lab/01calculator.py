from functools import reduce


class Calculator:

    @staticmethod
    def add(*numbers):
        return sum(numbers)

    @staticmethod
    def multiply(*numbers):
        result = reduce(lambda a, b: a * b, numbers)
        return result

    @staticmethod
    def divide(*numbers):
        result = reduce(lambda a, b: a / b, numbers)
        return result

    @staticmethod
    def subtract(*numbers):
        result = reduce(lambda a, b: a - b, numbers)
        return result


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
