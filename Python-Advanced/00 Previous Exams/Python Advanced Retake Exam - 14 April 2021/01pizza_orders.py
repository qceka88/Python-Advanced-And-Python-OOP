##################################### variant 01 #####################################

from collections import deque

pizza_orders = deque(int(num) for num in input().split(', '))
workers = [int(num) for num in input().split(', ')]

total_pizza = 0

while pizza_orders and workers:
    current_orders = pizza_orders.popleft()
    if 0 < current_orders <= 10:
        while workers:
            current_employee = workers.pop()
            if current_orders <= current_employee:
                total_pizza += current_orders
                current_orders = 0
                break
            elif current_orders > current_employee:
                current_orders -= current_employee
                total_pizza += current_employee
    if not workers and current_orders > 0:
        pizza_orders.appendleft(current_orders)
if not pizza_orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizza}')
    if workers:
        print(f'Employees: {", ".join(map(str, workers))}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(map(str, pizza_orders))}')

##################################### variant 02 #####################################

from collections import deque


class PizzaOrders:

    def __init__(self, orders, workers):
        self.orders = orders
        self.workers = workers
        self.total_pizza = 0
        self.log = ''

    def pizza_making(self):
        while self.orders and self.workers:
            current_orders = self.orders.popleft()
            if 0 < current_orders <= 10:
                while self.workers:
                    current_employee = self.workers.pop()
                    if current_orders <= current_employee:
                        self.total_pizza += current_orders
                        current_orders = 0
                        break
                    elif current_orders > current_employee:
                        current_orders -= current_employee
                        self.total_pizza += current_employee
            if not self.workers and current_orders > 0:
                self.orders.appendleft(current_orders)

    def prepare_result(self):
        if not self.orders:
            self.log += 'All orders are successfully completed!'
            self.log += f'\nTotal pizzas made: {self.total_pizza}'
            if self.workers:
                self.log += f'\nEmployees: {", ".join(map(str, self.workers))}'
        else:
            self.log += 'Not all orders are completed.\n'
            self.log += f'Orders left: {", ".join(map(str, self.orders))}'

    def __repr__(self):
        return f'{self.log}'


pizza_orders = deque(int(num) for num in input().split(', '))
workers_stack = [int(num) for num in input().split(', ')]

output = PizzaOrders(pizza_orders, workers_stack)
output.pizza_making()
output.prepare_result()
print(output)

#################################### TASK CONDITION ############################
'''

                                       Problem 1

On the first line, you will receive a sequence of pizza orders. Each order contains a different number of 
pizzas, separated by comma and space ", ". On the second line, you will receive a sequence of employees 
with pizza-making capacities (how much pizzas an employee could make), separated by comma and space ", ".
Your task is to check if all pizza orders are completed. 
To do that, you should take the first order and the last employee and see:
•	If the number of pizzas in the order is less than or equal to the employee's pizza making capacity, 
the order is completed. Remove both the order and the employee.
•	If the number of pizzas in the order is greater than the employee's pizza making capacity, the remaining 
pizzas from the order are going to be made by the next employees until the order is completed. 
o	If there are no more employees to finish the order, consider it not completed.
•	The restaurant does not take orders for more than 10 pizzas at once.
•	If an order is invalid (less than or equal to 0), you need to remove it before it is taken by an employee. 
You should keep track of the total pizzas that are being made.
Input
•	On the first line you will be given a sequence of pizza orders each represented as a
 number – integers separated by comma and space ", "
•	On the second line you will be given a sequence of employees with pizza-making 
capacities – integers separated by comma and space ", "
Output
•	If all orders are successfully completed, print:
All orders are successfully completed!
Total pizzas made: {total count}
Employees: {left employees joined by ", "}
•	Otherwise, if you ran out of employees and there are still some orders left print:
Not all orders are completed.
Orders left: {left orders joined by ", "}
Constraints
•	You will always have at least one order and at least one employee
•	All integers will be in range [-100, 100]

_______________________________________________
Example_01

Input
11, 6, 8, 1
3, 1, 9, 10, 5, 9, 1

Output
All orders are successfully completed!
Total pizzas made: 15
Employees: 3, 1

Explanation
1) The restaurant do not take the first order for 11 pizzas.
2) The first employee (1) takes an order for 6 pizzas but could only make 1. 5 pizzas left.
3) The next employee (9) continues the same order for 5 pizzas. The order is completed. Remove both.
4) The next employee (5) takes an order for 8 pizzas but could only make 5. 3 pizzas left.
5) The next employee (10) continues the same order for 3 pizzas. The order is completed. Remove both.
6) The next employee (9) takes an order for 1 pizza. The order is completed. Remove both.
7) All orders are completed. 

_______________________________________________
Example_02

Input
10, 9, 8, 7, 5
5, 10, 9, 8, 7

Output
Not all orders are completed.
Orders left: 2, 5

Explanation
1) The last employee (7) takes an order for 10 pizzas but could only make 7. 3 pizzas left.
2) The next employee (8) continues the same order for 3 pizzas. The order is completed. Remove both.
3) The next employee (9) takes an order for 9 pizzas. The order is completed. Remove both.
4) The next employee (10) takes an order for 8 pizzas. The order is completed. Remove both.
5) The next employee (5) takes an order for 7 pizzas but could only make 5. 2 pizzas left.
6) Orders are not completed. 

_______________________________________________
Example_01

Input
12, -3, 14, 3, 2, 0
10, 15, 4, 6, 3, 1, 22, 1

Output
All orders are successfully completed!
Total pizzas made: 5
Employees: 10, 15, 4, 6



'''
