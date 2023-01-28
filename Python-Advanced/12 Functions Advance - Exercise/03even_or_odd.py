class EvenOdd:

    def __init__(self, *args):
        self.result = []
        self.numbers = args[:-1]
        self.command = args[-1]
        self.actions = {
            'even': self.even_numbers,
            'odd': self.odd_numbers
        }


    def main_meth(self):
        self.filter_numbers_as_per_command()
        return self.result

    def filter_numbers_as_per_command(self):
        self.actions[self.command]()

    def even_numbers(self):
        self.result = filter(lambda x: (x % 2 == 0), self.numbers)

    def odd_numbers(self):
        self.result = filter(lambda x: (x % 2 != 0), self.numbers)


def even_odd(*args):
    output = EvenOdd(*args).main_meth()
    return list(output)


# Part below is part from automatic judge system from SoftUni
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
print(even_odd(1, 2, 3, 4, 5, 6, "even"))


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
