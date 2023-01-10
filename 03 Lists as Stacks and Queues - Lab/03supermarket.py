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
