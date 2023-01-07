##################################### variant 01 #####################################
def shopping_list(budget, **kwargs):
    shopping_basket = {}
    if budget >= 100:
        for product_type, data in kwargs.items():
            if len(shopping_basket) == 5:
                break
            total_price = data[0] * data[1]
            if budget - total_price >= 0:
                budget -= total_price
                shopping_basket[product_type] = total_price

        return "\n".join(f"You bought {name} for {price:.2f} leva." for name, price in shopping_basket.items())

    else:
        return "You do not have enough budget."


# Part below is part from automatic judge system from SoftUni
print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
##################################### variant 02 #####################################
class Shopping:

    def __init__(self, budget, **kwargs):
        self.budget = budget
        self.input_products = kwargs
        self.shopping_basket = {}
        self.message = ''

    def go_to_shopping(self):
        if self.budget >= 100:
            for product_type, data in self.input_products.items():
                if len(self.shopping_basket) == 5:
                    break
                total_price = data[0] * data[1]
                if self.budget - total_price >= 0:
                    self.budget -= total_price
                    self.shopping_basket[product_type] = total_price

            self.message = "\n".join(
                f"You bought {name} for {price:.2f} leva." for name, price in self.shopping_basket.items())

        else:
            self.message = "You do not have enough budget."

    def __repr__(self):
        return f'{self.message}'


def shopping_list(budget, **kwargs):
    output = Shopping(budget, **kwargs)
    output.go_to_shopping()
    return f'{output}'


# Part below is part from automatic judge system from SoftUni
print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))



#################################### TASK CONDITION ############################
'''
                         Problem 3 - Shopping List

Write a function called shopping_list which will receive an integer number representing the 
budget in leva and a different number of keywords. Each key represents the product (string),
and each value will be a tuple with the product's price (integer or float number) at the first 
position and quantity (integer) at the second position. Your job is to return which products you 
bought with the given budget. You only buy a product if you can buy all of its quantity.
You could only start shopping if you have at least 100 leva budget. Otherwise, you should stop 
the program and return "You do not have enough budget.".
Also, you are carrying a basket that cannot hold more than 5 types of products. You should stop buying products:
•	if you reach the allowed amount of types of products (no matter their quantity)
•	if you did not reach the allowed amount, but you do not have more products on the shopping list
You should always buy products successively!
For each product (all its quantity) you succeeded to buy, return a string on a new line in the following format:
"You bought {product_name} for {total_price} leva."
Note: Submit only the function in the judge system
Input
•	There will be no input, and just parameters passed to your function
Output
•	The function should return strings on separate lines containing the bought 
products and their price in the format described above.

_______________________________________________
Example_01

Test Code	(no input data in this task)
print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

Output                    
You bought skirts for 60.00 leva.
You bought coffee for 15.00 leva.

_______________________________________________
Example_02

Test Code	(no input data in this task)
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

Output
You do not have enough budget.

_______________________________________________
Example_03

Test Code	(no input data in this task)
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

Output                    
You bought cola for 2.40 leva.
You bought candies for 3.75 leva.
You bought bread for 1.80 leva.
You bought pie for 52.50 leva.
You bought tomatoes for 4.20 leva.

'''

