class BattleNames:

    def __init__(self):
        self.output_message = ''
        self.numbers_of_names = int(input())
        self.odd_set = set()
        self.even_set = set()
        self.even_odd = {True: self.even_set,
                         False: self.odd_set}
        self.main_meth()

    def main_meth(self):
        self.receive_names()
        self.prepare_output_message()

    def receive_names(self):
        for number in range(1, self.numbers_of_names + 1):
            name = input()
            value_of_name = self.calculate_ascii_value_of_name(name, number)
            boolean = self.is_even(value_of_name)
            self.even_odd[boolean].add(value_of_name)

    def calculate_ascii_value_of_name(self, some_name, some_number):
        sum_of_letters = sum(ord(i) for i in some_name)
        final_value = self.calculate_final_value_by_row(sum_of_letters, some_number)
        return final_value

    def calculate_final_value_by_row(self, some_value, some_number):
        return some_value // some_number

    def is_even(self, number_to_check):
        return True if number_to_check % 2 == 0 else False

    def prepare_output_message(self):
        if sum(self.odd_set) == sum(self.even_set):
            self.output_message = ', '.join(map(str, self.odd_set.union(self.even_set)))
        elif sum(self.odd_set) > sum(self.even_set):
            self.output_message = ', '.join(map(str, self.odd_set.difference(self.even_set)))
        else:
            self.output_message = ', '.join(map(str, self.odd_set.symmetric_difference(self.even_set)))

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(BattleNames())

#################################### TASK CONDITION ############################
"""
                        6.	Battle of Names
You will receive a number N. On the following N lines, you will be receiving 
names. You should sum the ASCII values of each letter in the name and integer 
divide it by the number of the current row (starting from 1). Save the result 
to a set of either odd or even numbers, depending on if the resulting number 
is odd or even. After that, sum the values of each set.
•	If the sums of the two sets are equal, print the union of the values, 
separated by ", ". 
•	If the sum of the odd numbers is bigger than the sum of the even numbers,
 print the different values, separated by ", ".
•	If the sum of the even numbers is bigger than the sum of the odd numbers,
 print the symmetric-different values, separated by ", ".
NOTE: On every operation, the starting set should be the odd set

____________________________________________________________________________________________
Example_01

Input
4
Pesho
Stefan
Stamat
Gosho	

Output
304, 128, 206, 511	

Explanation
First name: Pesho. The sum of the ASCII values is: 
80 + 101 + 115 + 104 + 111 = 511. Integer divide the sum to the current row (1): 511 / 1 = 511.
Second name: Stefan. The sum of the ASCII values is: 
83 + 116 + 101 + 102 + 97 + 110 = 609. Integer divide the sum to the current row (2): 609 / 2 = 304.
Third name: Stamat. The sum of the ASCII values is: 
83 + 116 + 97 + 109 + 97 + 116 = 618. Integer divide the sum to the current row (3): 618 / 3 = 206.
Fourth name: Gosho. The sum of the ASCII values is: 
71 + 111 + 115 + 104 + 111 = 512. Integer divide the sum to the current row (4): 512 / 4 = 128.
The odd set: 511
The even set: 304, 206, 128
The sum of the even numbers is larger, so we print the symmetric-different values.

____________________________________________________________________________________________
Example_02

Input
6
Preslav
Gosho
Ivan
Stamat
Pesho
Stefan	

Output
733, 101	

"""
