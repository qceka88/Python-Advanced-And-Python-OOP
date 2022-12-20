##################################### variant 01 #####################################
first, second = tuple(map(int, input().split()))

first_set = set()
second_set = set()

for num in range(first):
    first_set.add(input())

for num in range(second):
    second_set.add(input())

result = first_set.intersection(second_set)

print(*result, sep='\n')


##################################### variant 02 #####################################
class Main:

    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.first_set = set()
        self.second_set = set()
        self.result = set()

    def fill_first_set(self):
        for num in range(self.first):
            self.first_set.add(input())

    def fill_second_set(self):
        for num in range(self.second):
            self.second_set.add(input())

    def compare(self):
        self.result = self.first_set.intersection(self.second_set)

    def __repr__(self):
        return '\n'.join(str(element) for element in self.result)


first_number, second_number = tuple(map(int, input().split()))
output = Main(first_number, second_number)
output.fill_first_set()
output.fill_second_set()
output.compare()
print(output)

#################################### TASK CONDITION ############################

"""

                     2.	Sets of Elements
Write a program that prints a set of elements. On the first line, 
you will receive two numbers - n and m, separated by a single 
space - representing the lengths of two separate sets. On the 
next n + m lines, you will receive n numbers, which are the numbers 
in the first set, and m numbers, which are in the second set. 
Find all the unique elements that appear in both and print them on 
separate lines (the order does not matter).
For example:
Set with length n = 4: {1, 3, 5, 7}
Set with length m = 3: {3, 4, 5}
Set that contains all the elements that repeat in both sets -> {3, 5}

____________________________________________________________________________________________
Example_01

Input
4 3
1
3
5
7
3
4
5	

Output
3
5

____________________________________________________________________________________________
Example_02

Input
2 2
1
3
1
5	

Output
1

"""
