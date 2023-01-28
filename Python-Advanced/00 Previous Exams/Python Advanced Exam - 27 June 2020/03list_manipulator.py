##################################### variant 01 #####################################
def list_manipulator(some_list, command, side, *args):
    if command == 'remove':
        quantity = args[0] if args else 1
        if side == 'end':
            some_list = some_list[:-quantity]
        elif side == 'beginning':
            some_list = some_list[quantity:]
    elif command == 'add':
        some_list = some_list + list(args) if side == 'end' else list(args) + some_list
    return some_list


# Part below is part from automatic judge system from SoftUni
print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
##################################### variant 02 #####################################

class ListManipulator:

    def __init__(self, some_list, command, side, *args):
        self.some_list = some_list
        self.command = command
        self.side = side
        self.args = args
        self.actions = {'remove': self.remove_numbers,
                        'add': self.add_numbers}

    def end_of_list_remove(self, quantity):
        self.some_list = self.some_list[:-quantity]

    def beginning_of_list_remove(self, quantity):
        self.some_list = self.some_list[quantity:]

    def remove_numbers(self):
        side_of_list = {'end': self.end_of_list_remove,
                        'beginning': self.beginning_of_list_remove}
        quantity = self.args[0] if self.args else 1
        side_of_list[self.side](quantity)

    def end_of_list_add(self):
        self.some_list = self.some_list + list(self.args)

    def beginning_of_list_add(self):
        self.some_list = list(self.args) + self.some_list

    def add_numbers(self):
        side_of_list = {'end': self.end_of_list_add,
                        'beginning': self.beginning_of_list_add}
        side_of_list[self.side]()

    def manipulating_the_list(self):
        self.actions[self.command]()
        return self.some_list


def list_manipulator(*args):
    output = ListManipulator(*args)
    return output.manipulating_the_list()


# Part below is part from automatic judge system from SoftUni
print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))

#################################### TASK CONDITION ############################
'''
                      03 List Manipulator

Write a function called list_manipulator which receives a list of numbers as first parameter and different 
amount of other parameters. The second parameter might be "add" or "remove". The third parameter might be 
"beginning" or "end". There might or might not be any other parameters (numbers):
•	In case of "add" and "beginning", add the given numbers to the beginning of the 
given list of numbers and return the new list
•	In case of "add" and "end", add the given numbers to the end of the given list of numbers and return the new list
•	In case of "remove" and "beginning"
o	If there is another parameter (number), remove that amount of numbers from the beginning of the list of numbers.
o	If there are no other parameters, remove only the first element of the list.
o	Finaly, return the new list
•	In case of "remove" and "end"
o	If there is another parameter (number), remove that amount of numbers from the end of the list of numbers.
o	Otherwise if there are no other parameters, remove only the last element of the list.
o	Finaly, return the new list
For more clarifications, see the examples below.
Input
•	There will be no input
•	Parameters will be passed to your function
Output
•	The function should return the new list of numbers

_______________________________________________
Example_01

Test Code	(no input data in this task)                                  Output  
print(list_manipulator([1,2,3], "remove", "end"))                         [1, 2]        
print(list_manipulator([1,2,3], "remove", "beginning"))                   [2, 3]           
print(list_manipulator([1,2,3], "add", "beginning", 20))                  [20, 1, 2, 3]              
print(list_manipulator([1,2,3], "add", "end", 30))                        [1, 2, 3, 30]                   
print(list_manipulator([1,2,3], "remove", "end", 2))                      [1]            
print(list_manipulator([1,2,3], "remove", "beginning", 2))                [3]            
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))          [20, 30, 40, 1, 2, 3]           
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))                [1, 2, 3, 30, 40, 50]       	

'''
