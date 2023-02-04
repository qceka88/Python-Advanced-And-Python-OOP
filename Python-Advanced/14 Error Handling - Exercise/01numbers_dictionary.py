class FillDict:

    def __init__(self):
        self.dict = {}

    def take_elements_to_dict(self):
        line = input()
        while line != "Search":
            try:
                number_as_string = line
                number = int(input())
                self.dict[number_as_string] = number
            except ValueError:
                print(f'Value must be an integer!')
            line = input()


class SearchNumbers:

    def __init__(self, nums_dict):
        self.nums_dict = nums_dict

    def search_for_number(self):
        line = input()
        while line != "Remove":
            try:
                searched = line
                print(self.nums_dict[searched])
            except KeyError:
                print(f'Number does not exist in dictionary')
            line = input()


class RemoveNumbers:

    def __init__(self, some_dict):
        self.some_dict = some_dict

    def check_for_number_removing(self):
        line = input()
        while line != "End":
            try:
                searched = line
                del self.some_dict[searched]
            except KeyError:
                print(f'Number  does not exist in dictionary')
            line = input()


class ClassPrint:

    def __init__(self, data):
        self.data = data

    def printing_method(self):
        print(self.data)


numbers_dictionary = FillDict()
numbers_dictionary.take_elements_to_dict()
some_search_object = SearchNumbers(numbers_dictionary.dict)
some_search_object.search_for_number()
some_remove_object = RemoveNumbers(numbers_dictionary.dict)
some_printing_object = ClassPrint(some_remove_object.some_dict).printing_method()




#################################### TASK CONDITION ############################
'''
             1.	Numbers Dictionary
You are provided with the following code:


 '''
numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    number = int(input())
    numbers_dictionary[number_as_string] = number

line = input()

while line != "Remove":
    searched = line
    print(numbers_dictionary[searched])

line = input()

while line != "End":
    searched = line
    del numbers_dictionary[searched]

print(numbers_dictionary)



'''
•	On the first several lines, until you receive the command "Search",
 you will receive on separate lines the number as a text and the number as an integer
•	When you receive "Search" on the next several lines until you receive the command "Remove",
 you will be given the searched number as a text, and you need to print it on the console
•	When you receive "Remove" on the next several lines until you receive "End", 
you will be given the searched number as a text, and you need to remove it from the dictionary
•	In the end, you need to print what is left from the dictionary
There is some missing code in the solution, and some errors may occur.
Complete the code, so the following errors are handled:
•	Passing non-integer type to the variable number
•	Searching for a non-existent number
•	Removing a non-existent number
Print appropriate messages when an error has occurred. The messages should be:
•	"The variable number must be an integer"
•	"Number does not exist in dictionary" - for non-existing keys

____________________________________________________________________________________________
Example_01

Input
one
1
two
2
Search
one
Remove
two
End

Output
1
{'one': 1}

____________________________________________________________________________________________
Example_02

Input
one
two
Search
Remove
End

Output
The variable number must be an integer
{}

____________________________________________________________________________________________
Example_03

Input
one
1
Search
one
Remove
two
End

Output
1
Number does not exist in dictionary
{'one': 1}

'''