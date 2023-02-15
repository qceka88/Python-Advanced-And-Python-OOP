from collections import deque


class CustomersRamen:

    def __init__(self):
        self.ramen_bowls = deque()
        self.customers = deque()

    def main_method(self):
        self.__fill_ramen_supplies()
        self.__fill_customers_list()

    def __fill_ramen_supplies(self):
        [self.ramen_bowls.append(int(bowl)) for bowl in input().split(', ')]

    def __fill_customers_list(self):
        [self.customers.append(int(customer)) for customer in input().split(', ')]


class ServingMeals:

    def __init__(self, data):
        self.restaurant = data

    def restaurant_in_action(self):
        def __feed_customers_with_ramen():
            if bowl > customer:
                self.restaurant.ramen_bowls.append(bowl - customer)
            elif customer > bowl:
                self.restaurant.customers.appendleft(customer - bowl)

        while self.restaurant.ramen_bowls and self.restaurant.customers:
            bowl = self.restaurant.ramen_bowls.pop()
            customer = self.restaurant.customers.popleft()

            __feed_customers_with_ramen()


class PrepareResult:

    def __init__(self, data):
        self.result = []
        self.data = data

    def check_restaurant_data(self):
        if not self.data.customers:
            self.result.append("Great job! You served all the customers.")
            if self.data.ramen_bowls:
                left_ramen = ', '.join(str(r) for r in self.data.ramen_bowls)
                self.result.append(f"Bowls of ramen left: {left_ramen}")
        else:
            self.result.append("Out of ramen! You didn't manage to serve all customers.")
            left_customers = ', '.join(str(c) for c in self.data.customers)
            self.result.append(f"Customers left: {left_customers}")

    def __str__(self):
        return '\n'.join(self.result)


if __name__ == '__main__':
    restaurant = CustomersRamen()
    restaurant.main_method()
    serving = ServingMeals(restaurant)
    serving.restaurant_in_action()
    result = PrepareResult(restaurant)
    result.check_restaurant_data()
    print(result)


#################################### TASK CONDITION ############################
'''

                    01.	 Ramen Shop
You will be given two sequences of integers representing bowls of ramen and customers. 
Your task is to find out if you can serve all the customers. Start by taking the last bowl 
of ramen and the first customer. Try to serve every customer with ramen until we have no 
more ramen or customers left:
•	Each time the value of the ramen is equal to the value of the customer, remove them both 
and continue with the next bowl of ramen and the next customer.
•	Each time the value of the ramen is bigger than the value of the customer, decrease the 
value of that ramen with the value of that customer and remove the customer. Then try to match 
the same bowl of ramen (which has been decreased) with the next customer.
•	Each time the customer's value is bigger than the value of the ramen bowl, decrease the 
value of the customer with the value of the ramen bowl and remove the bowl. Then try to match 
the same customer (which has been decreased) with the next bowl of ramen.
Look at the examples provided for a better understanding of the problem.
Input
•	On the first line, you will receive integers representing the bowls of ramen, 
separated by a single space and a comma ", ".
•	On the second line, you will receive integers representing the customers, 
separated by a single space and a comma ", ".
Output
•	If all customers are served, print: "Great job! You served all the customers."
o	Print all of the left ramen bowls (if any) separated by comma and space in the format:
"Bowls of ramen left: {bowls of ramen left}"
•	Otherwise, print: "Out of ramen! You didn't manage to serve all customers."
o	Print all customers left separated by comma and space in the format "Customers left: {customers left}"

_______________________________________________
Example_01

Input
14, 25, 37, 43, 19
58, 23, 37	

Output
Great job! You served all the customers
Bowls of ramen left: 14, 6


Explanation
Start by taking the last bowl 19 and the first customer 58. The customer value is higher, 
so we remove the bowl and decrease the value of the customer by 19. Now the two lists should look like this:
Bowls = [14, 25, 37, 43]
Customers = [39, 23, 37]
Next, we take the following bowl (43) and continue with the same customer who is 39 now. 
The value of the bowl with ramen is higher than the customer's value, so we remove the customer 
and decrease the value of the ramen bowl. Now the two lists should look like this:
Bowls = [14, 25, 37, 4]
Customers = [23, 37]
We take the last bowl of ramen, which is 4 now, and compare it with the next customer (23). 
The value of the customer is higher, so we decrease his value by 4 and remove the last bowl. 
Now the two lists should look like this:
Bowls = [14, 25, 37]
Customers = [19, 37]
Then we continue with the ball 37 and customer 19. The bowl is higher. We remove the customer 
and decrease the bowl value with the value of the customer 19. Now the two lists should look like this:
Bowls = [14, 25,   18]
Customers  = [37]
Then we continue with bowl 18 and customer 37. The customer value is higher. We remove the bowl
 and decrease the customer value with the value of bowl 18. Now the two lists should look like this:
Bowls = [14, 25]
Customers = [19]
Then we continue with the ball 25 and customer 19. The bowl is higher. We remove the customer and 
decrease the bowl value with the value of the customer 19. Now the two lists should look like this:
Bowls = [14, 6]
Customers = []
We see that we served all of the customers and print the appropriate string for that case. 
After that, we print the leftover bowls of ramen.

_______________________________________________
Example_02

Input
30, 13, 45
70, 25, 55, 15

Output
Out of ramen! You didn't manage to serve all customers.
Customers left: 7, 55, 15

_______________________________________________
Example_03

Input
30, 25
20, 35

Output
Great job! You served all the customers.


'''
