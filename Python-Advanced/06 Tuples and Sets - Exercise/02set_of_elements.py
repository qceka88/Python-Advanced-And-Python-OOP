class SetOfElements:

    def __init__(self):
        self.output_message = ""
        self.rows_01, self.rows_02 = list(map(int, input().split()))
        self.first_set = set()
        self.second_set = set()
        self.occurrences = {}
        self.main_meth()

    def main_meth(self):
        self.add_numbers_to_first_set()
        self.add_number_to_second_set()
        self.find_occurrences()
        self.prepare_result()

    def add_numbers_to_first_set(self):
        for _ in range(self.rows_01):
            self.first_set.add(int(input()))

    def add_number_to_second_set(self):
        for _ in range(self.rows_02):
            self.second_set.add(int(input()))

    def find_occurrences(self):
        self.occurrences = self.first_set & self.second_set
        # self.occurrences = self.first_set.difference(self.second_set)

    def prepare_result(self):
        self.output_message = '\n'.join(str(n) for n in self.occurrences)

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(SetOfElements())


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
