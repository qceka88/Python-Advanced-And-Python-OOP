class Recursion:

    def __init__(self, number, power):
        self.power = power
        self.number = number
        self.result = 0

    def main_meth(self):
        self.result = self.recursive_power(self.number, self.power)
        return self.result

    def recursive_power(self, number, power):
        if power == 1:
            return self.number
        return number * self.recursive_power(number, power - 1)


def recursive_power(*args):
    output = Recursion(*args).main_meth()
    return output


print(recursive_power(2, 10))
print(recursive_power(10, 100))


#################################### TASK CONDITION ############################
'''
                   5.	Recursive Power
Create a recursive function called recursive_power() which should receive a 
number and a power. Using recursion, return the result of number ** power. 
Submit only the function in the judge system.

_______________________________________________
Example_01

Test Code	(no input data in this task)
print(recursive_power(2, 10))	

Output
1024

_______________________________________________
Example_02

Test Code	(no input data in this task)
print(recursive_power(10, 100))	

Output
10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

'''
