##################################### variant 01 #####################################
def recursive_power(number, power):
    if power == 0:
        return 1
    return number * recursive_power(number, power - 1)


print(recursive_power(2, 10))
print(recursive_power(10, 100))
##################################### variant 02 #####################################
class Recursion:

    def __init__(self, some_tuple):
        self.number, self.power = some_tuple

    def recursive_power(self):
        if self.power == 0:
            return 1
        return self.number * recursive_power(self.number, self.power - 1)


def recursive_power(*args):
    output = Recursion(args).recursive_power()
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
