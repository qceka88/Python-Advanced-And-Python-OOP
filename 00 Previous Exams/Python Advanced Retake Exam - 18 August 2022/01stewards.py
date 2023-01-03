##################################### variant 01 #####################################
from collections import deque

seats = input().split(', ')
first_row = deque(map(int, input().split(', ')))
second_row = deque(map(int, input().split(', ')))
taken_seats = []
rotations = 0
while len(taken_seats) < 3 and rotations < 10:
    first_number, second_number = first_row.popleft(), second_row.pop()
    rotations += 1
    letter = chr(first_number + second_number)
    first_combination, second_combination = str(first_number) + letter, str(second_number) + letter
    if first_combination in seats or second_combination in seats:
        if first_combination in seats:
            taken_seats.append(first_combination)
            seats.remove(first_combination)
        if second_combination in seats:
            taken_seats.append(second_combination)
            seats.remove(second_combination)
    else:
        first_row.append(first_number)
        second_row.appendleft(second_number)

print(f'Seat matches: {", ".join(taken_seats)}')
print(f'Rotations count: {rotations}')
##################################### variant 02 #####################################
from collections import deque


class Stewards:

    def __init__(self, seats, first_nums, second_nums):
        self.seats = seats
        self.first_nums = first_nums
        self.second_nums = second_nums
        self.taken_seats = []
        self.rotations = 0

    def find_seats_for_passenger(self):
        while len(self.taken_seats) < 3 and self.rotations < 10:
            first_number, second_number = self.first_nums.popleft(), self.second_nums.pop()
            self.rotations += 1
            letter = chr(first_number + second_number)
            first_combination, second_combination = str(first_number) + letter, str(second_number) + letter
            if first_combination in self.seats or second_combination in self.seats:
                if first_combination in self.seats:
                    self.taken_seats.append(first_combination)
                    self.seats.remove(first_combination)
                if second_combination in self.seats:
                    self.taken_seats.append(second_combination)
                    self.seats.remove(second_combination)
            else:
                self.first_nums.append(first_number)
                self.second_nums.appendleft(second_number)

    def __repr__(self):
        message = f'Seat matches: {", ".join(self.taken_seats)}\nRotations count: {self.rotations}'
        return message


list_of_seats = input().split(', ')
deque_of_first_row = deque(map(int, input().split(', ')))
deque_of_second_row = deque(map(int, input().split(', ')))

output = Stewards(list_of_seats, deque_of_first_row, deque_of_second_row)
output.find_seats_for_passenger()
print(output)

#################################### TASK CONDITION ############################
'''

                               01.	 Stewards
"It's only when you are flying above that you realize how incredible the Earth really is."
As you know, stewards are needed for every single flight. Today you will be 
that one steward, and you will be assisting the passengers in finding their seats.
You will be given a sequence of 6 seats - every seat is a mix of a number and
a letter in the format "{number}{letter}". You will also be given two more sequences of numbers only.
First, you have to take the first number of the first sequence and the last 
number of the second sequence. Next, take the sum of those two numbers and find its ASCII character.
•	Compare each of the two taken numbers and the found character with the seats. If you f
ind a match, the passenger is seated, and the seat is considered taken. Remove both 
numbers from their sequences.
•	If there is no equality, the two numbers should be returned at the end of their 
sequences (first becomes last, last becomes first).
•	If you match an already taken seat, you should just remove both numbers from their sequences.
Each time you take numbers from the sequences and try to match them, you make one 
rotation. You should keep track of all rotations made.
The program should end under the following circumstances:
•	You have found 3 (three) seat matches 
•	You have made a total of 10 rotations
Input
•	On the first line, you will be given a sequence of seats -
 strings separated by comma and space ", "
•	On the second and the third line, you will be given two more sequences
 - integers separated by a comma and a space ", "
Output
When the program ends, print the following on two different lines:
o	Seat matches: {matches separated by comma and space}
o	Rotations count: {total rotations made}
Constraints
•	All integers will be in the range [1, 100]
•	All letters will be in the range [A-Z]
•	You will never run out of numbers in your sequences before the program ends
•	You will never have more than one match at a time

_______________________________________________
Example_01

Input
17K, 20B, 3C, 15D, 31Z, 28F
20, 35, 15, 3, 2, 10
1, 15, 64, 53, 45, 46	

Output
Seat matches: 20B, 15D, 3C
Rotations count: 4

Explanation
1) Take the first number from the first sequence (20) and the last number 
from the second sequence (46). Then, sum the two numbers (66) - its ASCII 
character is "B". Check both combinations "20B" and "46B" with the seats. 
The seat "20B" matches the first combination, so remove both numbers (20 and 46) 
from the sequences and take the seat - it's no longer available for matching.
2) Take the next numbers - 35 and 45. Their sum matches the character "P". 
There are no matches. Return both numbers to the opposite side of the sequences. 
The sequences look the following way: "15, 3, 2, 10, 35" and "45, 1, 15, 64, 53"
3) Take the following numbers - 15 and 53. Their sum matches the character "D". 
The seat "15D" is matched. Remove numbers 15 and 53 from their sequences.
4) Take the following numbers - 3 and 64. Their sum matches "C". 
The seat "3C" is matched. Remove the numbers 3 and 64 from their sequences.
Three seats are matched - print the needed information and end the program.

_______________________________________________
Example_02

Input
25A, 16B, 44T, 49D, 27M, 44F
25, 3, 31, 49, 26, 13
10, 15, 44, 40

Output
Seat matches: 25A, 44F
Rotations count: 10

_______________________________________________
Example_03

Input
15C, 25C, 36C, 43P, 40E, 38G
15, 25, 80, 40, 15, 99, 52
15, 42, 29

Output
Seat matches: 25C, 40E, 15C
Rotations count: 7

'''
