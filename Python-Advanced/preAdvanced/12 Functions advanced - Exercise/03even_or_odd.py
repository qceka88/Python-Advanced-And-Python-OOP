##################################### variant 01 #####################################
def even_odd(*args):
    command = args[-1]
    parity = 0 if command == 'even' else 1
    result = []
    for i in range(len(args) - 1):
        num = args[i]
        if num % 2 == parity:
            result.append(num)
    return result

#Part below is part from automatic judge system from SoftUni
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))


##################################### variant 02 #####################################
class Main:

    def __init__(self, *args):
        self.args = args
        self.result = []

    def return_to_main(self):
        command = self.args[-1]
        parity = 0 if command == 'even' else 1

        for i in range(len(self.args) - 1):
            num = self.args[i]
            if num % 2 == parity:
                self.result.append(num)
        return self.result


def even_odd(*args):
    result = Main(*args).return_to_main()
    return result

#Part below is part from automatic judge system from SoftUni
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

#################################### TASK CONDITION ############################
'''
                  3.	Even or Odd
Create a function called even_odd() that can receive a different quantity of 
numbers and a command at the end. The command can be "even" or "odd". 
Filter the numbers depending on the command and return them in a list. 
Submit only the function in the judge system.
Submit only your function in the judge system.

_______________________________________________
Example_01

Test Code	(no input data in this task)
print(even_odd(1, 2, 3, 4, 5, 6, "even"))	

Output
[2, 4, 6]

_______________________________________________
Example_02

Test Code	(no input data in this task)
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))	

Output
[1, 3, 5, 7, 9]


'''
