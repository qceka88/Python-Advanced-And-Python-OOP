##################################### variant 01 #####################################

row_of_names = int(input())

odd_set, even_set = set(), set()

for row in range(1, row_of_names + 1):
    name = input()
    value = (sum(ord(i) for i in name)) // row
    if value % 2 == 0:
        even_set.add(value)
    else:
        odd_set.add(value)


if sum(odd_set) == sum(even_set):
    result = odd_set.union(even_set)
elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)
else:
    result = odd_set.symmetric_difference(even_set)

print(*result, sep=', ')

##################################### variant 02 #####################################

class Battle:

    def __init__(self, some_rows):
        self.some_rows = some_rows
        self.odd_set = set()
        self.even_set = set()
        self.result = set()

    def extract_data(self):
        for row in range(1, self.some_rows + 1):
            name = input()
            value = (sum(ord(i) for i in name)) // row
            if value % 2 == 0:
                self.even_set.add(value)
            else:
                self.odd_set.add(value)

    def battle_of_names(self):
        if sum(self.odd_set) == sum(self.even_set):
            self.result = self.odd_set.union(self.even_set)
        elif sum(self.odd_set) > sum(self.even_set):
            self.result = self.odd_set.difference(self.even_set)
        else:
            self.result = self.odd_set.symmetric_difference(self.even_set)

    def __repr__(self):
        return ', '.join(str(num) for num in self.result)


row_of_names = int(input())
output = Battle(row_of_names)
output.extract_data()
output.battle_of_names()
print(output)


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
