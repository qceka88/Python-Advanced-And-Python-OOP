##################################### variant 01 #####################################
from collections import deque

initial_food = int(input())
orders = deque(map(int, input().split()))
print(max(orders))

for current_order in range(len(orders)):
    order = orders.popleft()

    if initial_food - order >= 0:
        initial_food -= order
    else:
        orders.appendleft(order)

if orders:
    print(f'Orders left: {" ".join(str(data) for data in orders)}')
else:
    print('Orders complete')

##################################### variant 02 #####################################
from collections import deque


class FastFood:

    def __init__(self, some_food, some_orders):
        self.some_food = some_food
        self.some_orders = some_orders
        self.log = ''

    def actions(self):
        self.log += f'{max(self.some_orders)}\n'
        for current_order in range(len(self.some_orders)):
            order = self.some_orders.popleft()

            if self.some_food - order >= 0:
                self.some_food -= order
            else:
                self.some_orders.appendleft(order)

    def __repr__(self):
        if orders:
            self.log += f'Orders left: {" ".join(str(data) for data in self.some_orders)}'
        else:
            self.log += 'Orders complete'
        return self.log


initial_food = int(input())
orders = deque(map(int, input().split()))

output = FastFood(initial_food, orders)
output.actions()
print(output)
#################################### TASK CONDITION ############################
"""
                          3. Fast Food
You have a fast-food restaurant, and the food you are offering is previously prepared.
Write a program that checks if you have enough food to serve lunch to all your customers. 
You also want to know who the client with the biggest order for that day is. 
First, you will be given the quantity of the food you have for the day (an integer number). 
Next, you will be given a sequence of integers (separated by a single space), 
each representing the quantity of food in each order. Keep the orders in a queue.
Find the biggest order and print it. Next, you will begin servicing your clients from 
the first one that came. Before each order, check if you have enough food left to complete it:
•	If you have, remove the order from the queue and reduce the quantity of food in the restaurant. 
•	Otherwise, stop serving.
Input
•	On the first line, you will be given the quantity of your food - an integer in the range [0, 1000]
•	On the second line, you will receive a sequence of integers, representing each order, separated by a single space
Output
•	On the first line, print the quantity of the biggest order
•	On the second line:
o	If you succeeded in servicing all your clients, print: "Orders complete".  
o	Otherwise, print: "Orders left: {order1} {order2} .... {orderN}".
Constraints
•	The input will always be valid

____________________________________________________________________________________________
Example_01

Input
348
20 54 30 16 7 9

Output
54
Orders complete

____________________________________________________________________________________________
Example_02

Input
499
57 45 62 70 33 90 88 76 100 50	

Output
100
Orders left: 76 100 50


"""