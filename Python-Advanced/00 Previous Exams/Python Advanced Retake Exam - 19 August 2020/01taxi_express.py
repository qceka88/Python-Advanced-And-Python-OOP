##################################### variant 01 #####################################
from collections import deque

customers = deque(int(num) for num in input().split(', '))
taxis = [int(num) for num in input().split(', ')]
total_time = 0

while customers and taxis:
    current_customer = customers.popleft()
    while taxis:
        current_taxi = taxis.pop()
        if current_taxi >= current_customer:
            total_time += current_customer
            break

    if len(taxis) < 1 and current_taxi < current_customer:
        customers.appendleft(current_customer)

if customers:
    print(f'Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(map(str, customers))}')
else:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')


##################################### variant 02 #####################################

from collections import deque


class TaxiExpress:

    def __init__(self, customer_times, taxi_cabs):
        self.customer_times = customer_times
        self.taxi_cabs = taxi_cabs
        self.total_time = 0

    def taxi_company_in_action(self):
        while self.customer_times and self.taxi_cabs:
            current_customer = self.customer_times.popleft()
            while self.taxi_cabs:
                current_taxi = self.taxi_cabs.pop()
                if current_taxi >= current_customer:
                    self.total_time += current_customer
                    break

            if len(self.taxi_cabs) < 1 and current_taxi < current_customer:
                self.customer_times.appendleft(current_customer)

    def __repr__(self):
        if self.customer_times:
            message = f'Not all customers were driven to their destinations'
            message += f'\nCustomers left: {", ".join(map(str, self.customer_times))}'
        else:
            message = 'All customers were driven to their destinations'
            message += f'\nTotal time: {self.total_time} minutes'
        return message


customers_deque = deque(int(num) for num in input().split(', '))
taxis_stack = [int(num) for num in input().split(', ')]

output = TaxiExpress(customers_deque, taxis_stack)
output.taxi_company_in_action()
print(output)


#################################### TASK CONDITION ############################
'''


                              01. Taxi Express
 
You have created your own taxi company called "Taxi Express". You want to analyze how well your taxi drivers 
are doing by calculating how much time they need to tend the customers. You will receive a list of the 
cutomers (numbers seperated by comma and space ", ") on the first line and list of your taxis 
(numbers seperated by comma and space ", "). Each number from the customer list represents how much time it
takes to drive the customer to his/her destination. Each number from the taxis list represents how much time 
they can drive, before they need to refill their tanks. Keep track of the total time passed to drive all the 
customers to their destinations (values of all customers). Each time you tend customers you should put the 
first customer in the last taxi until there are no customers left.
•	If the taxi can drive the customer to his/her destination, he does and you must add the time passed 
to drive the customer to his/her destination (the value of the current customer) to the total time. 
Remove both the customer and the taxi.
•	If the taxi cannot drive the customer to his/her destination, leave the customer at the 
beginning of the queue and remove the taxi. 
At the end if you have successfully driven all the customers to their destinations, print 
All customers were driven to their destinations
Total time: {total_time} minutes
Otherwise, if you ran out of taxis and there are still some customers left print
Not all customers were driven to their destinations
Customers left: {left_customers joined by ", "}
Input
•	On the first line you are given the customers – numbers seperated by comma and space ", "
•	On the second line you are given the taxis – numbers seperated by comma and space ", "
Output
•	Print the output as described above
Constraints
•	You will always have at least one customer and at least one taxi

_______________________________________________
Example_01

Input
4, 6, 8, 5, 1
1, 9, 15, 10, 6	

Output
All customers were driven to their destinations
Total time: 24 minutes

_______________________________________________
Example_02

Input
10, 5, 8, 9
2, 4, 5, 8

Output
Not all customers were driven to their destinations
Customers left: 10, 5, 8, 9

_______________________________________________
Example_03

Input
2, 8, 4, 3, 11, 7
10, 15, 4, 6, 3, 10, 2, 1


Output
All customers were driven to their destinations
Total time: 35 minutes



'''
