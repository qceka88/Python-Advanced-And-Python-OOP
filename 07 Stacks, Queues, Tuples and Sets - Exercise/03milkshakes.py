##################################### variant 01 #####################################

from collections import deque

chocolate_que = deque(map(int, input().split(', ')))
milk_que = deque(map(int, input().split(', ')))

milkshakes = 0

while milkshakes < 5 and milk_que and chocolate_que:

    chocolate_portion = chocolate_que.pop()
    milk_portion = milk_que.popleft()

    if chocolate_portion <= 0 or milk_portion <= 0:
        if chocolate_portion > 0:
            chocolate_que.append(chocolate_portion)
        if milk_portion > 0:
            milk_que.appendleft(milk_portion)
    elif chocolate_portion == milk_portion:
        milkshakes += 1
    else:
        milk_que.append(milk_portion)
        chocolate_que.append(chocolate_portion - 5)

print('Great! You made all the chocolate milkshakes needed!' if milkshakes == 5 else "Not enough milkshakes.")
print(f"Chocolate: {', '.join(map(str, chocolate_que)) if chocolate_que else 'empty'}")
print(f"Milk: {', '.join(map(str, milk_que)) if milk_que else 'empty'}")

##################################### variant 02 #####################################

from collections import deque


class Main:
    def __init__(self, choco_stack, milk_deque):
        self.choco_stack = choco_stack
        self.milk_deque = milk_deque
        self.shakes = 0
        self.message = []

    def milk_shaking(self):
        while self.shakes < 5 and self.milk_deque and self.choco_stack:

            chocolate_portion = self.choco_stack.pop()
            milk_portion = self.milk_deque.popleft()

            if chocolate_portion <= 0 or milk_portion <= 0:
                if chocolate_portion > 0:
                    self.choco_stack.append(chocolate_portion)
                if milk_portion > 0:
                    self.milk_deque.appendleft(milk_portion)
            elif chocolate_portion == milk_portion:
                self.shakes += 1
            else:
                self.milk_deque.append(milk_portion)
                self.choco_stack.append(chocolate_portion - 5)

    def result(self):
        self.message.append(
            'Great! You made all the chocolate milkshakes needed!' if self.shakes == 5 else "Not enough milkshakes.")
        self.message.append(f"Chocolate: {', '.join(map(str, self.choco_stack)) if self.choco_stack else 'empty'}")
        self.message.append(f"Milk: {', '.join(map(str, self.milk_deque)) if self.milk_deque else 'empty'}")

    def __repr__(self):
        return '\n'.join(self.message)


chocolates = list(map(int, input().split(', ')))
milks = deque(map(int, input().split(', ')))

output = Main(chocolates, milks)
output.milk_shaking()
output.result()
print(output)

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
