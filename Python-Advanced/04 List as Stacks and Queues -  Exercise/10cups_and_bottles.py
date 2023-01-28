from collections import deque


class CupsAndBottles:

    def __init__(self):
        self.cups = deque()
        self.bottles = []
        self.waste_water = 0
        self.message = ''
        self.main_meth()

    def main_meth(self):
        self.fill_cups_deque()
        self.fill_bottles_stack()
        self.start_to_fill_the_cups()
        self.prepare_result_message()

    def fill_cups_deque(self):
        self.cups = deque(int(n) for n in input().split())

    def fill_bottles_stack(self):
        self.bottles = [int(n) for n in input().split()]

    def start_to_fill_the_cups(self):
        while self.cups and self.bottles:
            cup = self.cups.popleft()
            while self.bottles:
                bottle = self.bottles.pop()
                if bottle >= cup:
                    self.waste_water += (bottle - cup)
                    break
                else:
                    cup -= bottle

    def prepare_result_message(self):
        if not self.cups:
            self.message = f'Bottles: {" ".join(str(n) for n in self.bottles)}'
        if not self.bottles:
            self.message = f'Cups: {" ".join(str(n) for n in self.cups)}'
        self.message += f'\nWasted litters of water: {self.waste_water}'

    def __repr__(self):
        return self.message


if __name__ == '__main__':
    print(CupsAndBottles())

#################################### TASK CONDITION ############################
"""
                     10. *Cups and Bottles
You will be given a sequence of integers – each indicating a cup's capacity 
(in litters). After that, you will be given another sequence of integers – 
each indicating a bottle's capacity (in litters). Your job is to try to fill 
up all the cups. You must start picking from the last received bottle and 
start filling from the first entered cup. You could pick exactly one bottle 
at a time. If the current bottle has N water, you give the first entered cup 
N water and reduce its integer value by N. When a cup's integer value reaches 
0 or less, it gets removed. It is possible that the current cup's value is 
greater than the current bottle's value. In that case, you pick bottles until 
you reduce the cup's integer value to 0 or less. If a bottle's value is greater 
or equal to the cup's current value, you fill up the cup, and the remaining 
water becomes wasted. You should keep track of the wasted litters of water and 
print them at the end of the program. If you have managed to fill up all the cups, 
print the remaining water bottles, from the last entered – to the first. Otherwise, 
you must print the remaining cups ordered by the entrance – from the first 
entered – to the last.
Input
•	On the first line of input, you will receive the integers representing
 the cups' capacity, separated by a single space.
•	On the second line of input, you will receive the integers representing
 the filled bottles, separated by a single space.
Output
•	On the first line:
o	If you filled all the cups, print the remaining bottles as specified: 
"Bottles: {bottle1} {bottle2} … {bottleN}" 
o	If you used all the bottles of water, print the remaining cups as specified:
"Cups: {cup1} {cup2} … {cupN}"
•	On the second line, print the wasted litters of water in the following format: 
"Wasted litters of water: {wasted_litters_of_water}."
Constraints
•	All the given numbers will be valid integers in the range [1, 1000].
•	It is safe to assume that there will be NO case in which the water is
 exactly as much as the cups' values so that in the end, there are no cups
  and no water in the bottles.
•	There will be NO case where a cup will be almost full at the end.

____________________________________________________________________________________________
Example_01

Input
4 2 10 5
3 15 15 11 6

Output
Bottles: 3
Wasted litters of water: 26	

Explanation
We take the first entered cup and the last entered bottle, as it is described in the condition.
6 – 4 = 2 – we have 2 more liters of water left.
11 – 2 = 9 – again, we have 9 more liters of water left, so the amount of wasted water becomes 11.
15 – 10 = 5 – wasted water becomes 16.
15 – 5 = 10 – wasted water becomes 26.
We've managed to fill up all of the cups, so we print the 
remaining bottles and the total amount of wasted water.

____________________________________________________________________________________________
Example_02

Input
1 5 28 1 4
3 18 1 9 30 4 5

Output
Cups: 4
Wasted litters of water: 35

____________________________________________________________________________________________
Example_03

Input	
10 20 30 40 50
20 11

Output
Cups: 30 40 50
Wasted litters of water: 1	

"""
