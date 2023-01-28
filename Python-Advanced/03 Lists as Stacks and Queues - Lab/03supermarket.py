from collections import deque


class Supermarket:

    def __init__(self):
        self.customers = deque()

    def customer_enter_in_shop(self):
        while True:
            current_customer = input()
            if current_customer == 'End':
                break
            elif current_customer == 'Paid':
                while self.customers:
                    print(self.customers.popleft())
            else:
                self.customers.append(current_customer)

    def __repr__(self):
        return f'{len(self.customers)} people remaining.'


output = Supermarket()
output.customer_enter_in_shop()
print(output)


#################################### TASK CONDITION ############################
"""

                              3.	Supermarket
Tom is working at the supermarket, and he needs your help to keep track 
of his clients. Write a program that reads lines of input consisting of a 
customer's name and adds it to the end of a queue until "End" is received.
If, in the meantime, you receive the command "Paid", you should print each 
customer in the order they are served (from the first to the last one) and 
empty the queue. When you receive "End", you should print the count of the
remaining people in the queue in the format: "{count} people remaining.".

____________________________________________________________________________________________
Example_01

Input
George
Peter
William
Paid
Michael
Oscar
Olivia
Linda
End	

Output
George
Peter
William
4 people remaining.

____________________________________________________________________________________________
Example_02

Input
Anna
Emma
Alexander
End	

Output
3 people remaining.


"""

