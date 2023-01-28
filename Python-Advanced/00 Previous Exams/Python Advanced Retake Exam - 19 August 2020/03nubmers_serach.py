##################################### variant 01 #####################################

def numbers_searching(*args):
    duplicates = []
    for number in sorted(args):
        if number not in duplicates:
            count_duplicates = args.count(number)
            if count_duplicates > 1:
                duplicates.append(number)
    full_row = [num for num in range(min(args), max(args) + 1)]
    missing_number = set(full_row) - set(args)
    return [*missing_number, duplicates]


# Part below is part from automatic judge system from SoftUni
print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))


##################################### variant 02 #####################################

class SearchNumbers:

    def __init__(self, *args):
        self.args = args
        self.duplicates = []
        self.missing_number = 0

    def find_missing_number(self):
        numbers_row = set(self.args)
        start, end = min(numbers_row), max(numbers_row)
        full_numbers_row = [i for i in range(start, end)]
        self.missing_number = set(full_numbers_row) - numbers_row

    def find_duplicated_numbers(self):
        for number in sorted(set(self.args)):
            if number not in self.duplicates:
                if self.args.count(number) > 1:
                    self.duplicates.append(number)

    def return_to_main(self):
        return [*self.missing_number, self.duplicates]


def numbers_searching(*args):
    output = SearchNumbers(*args)
    output.find_missing_number()
    output.find_duplicated_numbers()
    return output.return_to_main()


# Part below is part from automatic judge system from SoftUni
print(numbers_searching(1, 2, 4, 2, 5, 4))

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

#################################### TASK CONDITION ############################
'''  
                                  03 Numbers search
 
Write a function called numbers_searching which receives a different amount of parameters. All parameters 
will be integer numbers forming a sequence of consecutive numbers. Your task is to find an unknown amount 
of duplicates from the given sequence and a missing value, such that all the duplicate values and the missing 
value are between the smallest and the biggest received number.  The function should return a list with the last 
missing number as a first argument and a sorted list, containing the duplicates found, in ascending order.
For example: if we have the following numbers: 1, 2, 4, 2, 5, 4 will return 3 as missing number and 2, 4 as 
duplicate numbers in the following format: [3, [2, 4]]
Input
•	There will be no input
•	Parameters will be passed to your function
Output
•	The function should return a list in the following format: 
[missing number, [duplicate_numbers separated with comma and space]]
Constraints
•	The missing number will always be between the smallest and the biggest received number

_______________________________________________
Example_01

Test Code	(no input data in this task)
print(numbers_searching(1, 2, 4, 2, 5, 4))

Output
[3, [2, 4]]

_______________________________________________
Example_02

Test Code	(no input data in this task)
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

Output
[6, [5, 7, 9]]

_______________________________________________
Example_03

Test Code	(no input data in this task)
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

Output
[46, [44, 45, 47, 48, 50]]

'''
