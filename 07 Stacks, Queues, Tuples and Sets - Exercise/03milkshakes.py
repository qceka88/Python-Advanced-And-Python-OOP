from collections import deque


class Milkshakes:

    def __init__(self):
        self.result_message = ''
        self.chocolate_row = deque()
        self.milk_cups_row = deque()
        self.milkshakes = 0
        self.main_meth()

    def main_meth(self):
        self.fill_chocolates()
        self.fill_cups_of_milks()
        self.start_creating_milkshakes()
        self.prepare_result()

    def fill_chocolates(self):
        self.chocolate_row = deque(int(x) for x in input().split(', '))

    def fill_cups_of_milks(self):
        self.milk_cups_row = deque(int(x) for x in input().split(', '))

    def start_creating_milkshakes(self):
        while self.chocolate_row and self.milk_cups_row and self.milkshakes != 5:
            current_chocolate = self.chocolate_row.pop()
            current_milk = self.milk_cups_row.popleft()
            if current_chocolate <= 0 or current_milk <= 0:
                if current_chocolate > 0:
                    self.chocolate_row.append(current_chocolate)
                if current_milk > 0:
                    self.milk_cups_row.appendleft(current_milk)
            else:
                if current_milk == current_chocolate:
                    self.milkshakes += 1
                else:
                    self.chocolate_row.append(current_chocolate - 5)
                    self.milk_cups_row.append(current_milk)

    def prepare_result(self):
        if self.milkshakes == 5:
            self.result_message = 'Great! You made all the chocolate milkshakes needed!\n'
        else:
            self.result_message = 'Not enough milkshakes.\n'
        choco = "empty" if not self.chocolate_row else ", ".join(str(x) for x in self.chocolate_row)
        milk = "empty" if not self.milk_cups_row else ", ".join(str(x) for x in self.milk_cups_row)
        self.result_message += f'Chocolate: {choco}\n'
        self.result_message += f'Milk: {milk}'

    def __repr__(self):
        return self.result_message


if __name__ == '__main__':
    print(Milkshakes())


#################################### TASK CONDITION ############################
"""
                                3.	Milkshakes
You are learning how to make milkshakes. First, you will be given two sequences 
of integers representing chocolates and cups of milk. You have to start from 
the last chocolate and try to match it with the first cup of milk. If their 
values are equal, you should make a milkshake and remove both ingredients. 
Otherwise, you should move the cup of milk at the end of the sequence and 
decrease the value of the chocolate by 5 without moving it from its position.
If any of the values are equal to or below 0, you should remove them from the 
records right before mixing them with the other ingredient. When you successfully 
prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk 
left, you need to stop making chocolate milkshakes.
Input
•	On the first line of input, you will receive the integers
 representing the chocolate, separated by  ", ". 
•	On the second line of input, you will receive the integers
 representing the cups of milk, separated by ", ".
Output
•	On the first line, print:
o	If you successfully made 5 milkshakes: "Great! You made all
 the chocolate milkshakes needed!"
o	Otherwise: "Not enough milkshakes."
•	On the second line - print:
o	If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
o	Otherwise: "Chocolate: empty"
•	On the third line - print:
o	If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
o	Otherwise: "Milk: empty"
Constraints
•	All given numbers will be valid integers in the range [-100 … 100].
The values in each sequence should be sorted in ascending order.

____________________________________________________________________________________________
Example_01

Input
20, 24, -5, 17, 22, 60, 26
26, 60, 22, 17, 24, 10, 55	

Output
Great! You made all the chocolate milkshakes needed!
Chocolate: 20
Milk: 10, 55


Explanation
1) 26 == 26 -> You made chocolate milkshake. Remove both ingredients.
2) 60 == 60 -> You made chocolate milkshake. Remove both ingredients.
3) 22 == 22 -> You made chocolate milkshake. Remove both ingredients.
4) 17 == 17 -> You made chocolate milkshake. Remove both ingredients.
5) -5 is invalid, so it is removed before mixing.
6) 24 == 24 -> You made chocolate milkshake. Remove both ingredients. 
You made enough chocolate milkshakes. The program ends. 
The values in each sequence should be sorted in ascending order.

____________________________________________________________________________________________
Example_02

Input
-10, -2, -30, 10
-5

Output
Not enough milkshakes.
Chocolate: -10, -2, -30, 10
Milk: empty
The values in each sequence should be sorted in ascending order.

____________________________________________________________________________________________
Example_03

Input
2, 3, 3, 7, 2
2, 7, 3, 3, 2, 14, 6

Output
Great! You made all the chocolate milkshakes needed!
Chocolate: empty
Milk: 14, 6

"""
