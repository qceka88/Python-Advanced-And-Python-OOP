def shop_from_grocery_list(budget, needed_products, *shop):

    def prepare_result():
        log = []
        if len(needed_products) == 0:
            log.append(f"Shopping is successful. Remaining budget: {budget:.2f}.")
        else:
            remaining_products = ', '.join(needed_products)
            log.append(f"You did not buy all the products. Missing products: {remaining_products}.")
        return log

    for product, price in shop:
        if product in needed_products:
            if budget - float(price) >= 0:
                budget -= float(price)
                needed_products.remove(product)
            else:
                break

    result = prepare_result()

    return '\n'.join(result)

# Part below is part from automatic judge system from SoftUni
print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))

#################################### TASK CONDITION ############################
"""
                                   3.  Grocery List

John has to shop for products on a list made by his wife. 
You need to help him by writing a program to make his task easier.
Write a function called shop_from_grocery_list that receives information about a budget, a grocery list, 
products, and their prices, and returns the result after the shopping. The function will receive a 
different number of arguments. The arguments will be passed as follows:
•	The first argument will be the budget - an integer in the range [0, 200];
•	The second argument will be the grocery list - a list with one, many,
 or no strings representing the products needed to be bought;
•	The following arguments will be the tuples with two elements - the first 
one is the product name (string), and the second one is its price (float);
After receiving the information and calling the function, the program should 
start tracking the shopping process:
•	Take the product name from each tuple successively and if you have enough 
money, buy it, and proceed to the next one.
•	If a product has already been purchased, ignore it, and proceed to the next one.
•	If you receive a product that is not on the grocery list, ignore it, and proceed to the next one.
•	If the budget you have is less than the price of the product, STOP shopping!
 In the end:
•	If you manage to buy all the products from the grocery list, return the message:
 "Shopping is successful. Remaining budget: {budget_left}."
o	The remaining budget should be formatted to the second decimal place.
•	Otherwise, return the message: "You did not buy all the products. 
Missing products: {"product1", "product2", …, "product N"}."
Note: Submit only the function in the judge system
Input
•	There will be no input from the console, just parameters passed to your function.
Output
•	Return one of the strings shown above depending on the result. 
Constraints
•	The first argument will always be an integer.
•	The second argument will always be a list.
•	Each tuple given will always contain the product name with its price.

_______________________________________________
Example_01

Test Code	(no input data in this task)
print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

Output
Shopping is successful. Remaining budget: 84.20.

_______________________________________________
Example_02

Test Code	(no input data in this task)
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

Output
You did not buy all the products. Missing products: chips.

_______________________________________________
Example_03

Test Code	(no input data in this task)
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))

Output
You did not buy all the products. Missing products: chips, meat.

"""
