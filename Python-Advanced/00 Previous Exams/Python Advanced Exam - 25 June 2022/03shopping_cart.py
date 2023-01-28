##################################### variant 01 #####################################

def shopping_cart(*args):
    products = {'Soup': [], 'Pizza': [], 'Dessert': []}
    car_product = False

    def fill_the_products():
        if product not in products[meal]:
            products[meal].append(product)

    for info in args:
        if info == 'Stop':
            break
        meal, product = info[0], info[1]
        if meal == 'Soup' and len(products[meal]) < 3:
            fill_the_products()
        elif meal == 'Pizza' and len(products[meal]) < 4:
            fill_the_products()
        elif meal == 'Dessert' and len(products[meal]) < 2:
            fill_the_products()
        car_product = True

    if not car_product:
        return "No products in the cart!"
    else:
        message = []
        for meal, products in sorted(products.items(), key=lambda x: (-len(x[1]), x[0])):
            message.append(f'{meal}:')
            if products:
                message.append('\n'.join(f' - {product}' for product in sorted(products)))

        return '\n'.join(message)


# Part below is part from automatic judge system from SoftUni
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))


##################################### variant 02 #####################################

class ShoppingCart:

    def __init__(self, *args):
        self.data = args
        self.products = {'Soup': [], 'Pizza': [], 'Dessert': []}
        self.car_product = False

    def shopping_cart(self):

        def fill_the_products():
            if product not in self.products[meal]:
                self.products[meal].append(product)

        for info in self.data:
            if info == 'Stop':
                break
            meal, product = info[0], info[1]
            if meal == 'Soup' and len(self.products[meal]) < 3:
                fill_the_products()
            elif meal == 'Pizza' and len(self.products[meal]) < 4:
                fill_the_products()
            elif meal == 'Dessert' and len(self.products[meal]) < 2:
                fill_the_products()
            self.car_product = True

    def __repr__(self):
        if not self.car_product:
            return "No products in the cart!"
        else:
            message = []
            for meal, products in sorted(self.products.items(), key=lambda x: (-len(x[1]), x[0])):
                message.append(f'{meal}:')
                if products:
                    message.append('\n'.join(f' - {product}' for product in sorted(products)))
            return '\n'.join(message)


def shopping_cart(*args):
    output = ShoppingCart(*args)
    output.shopping_cart()
    return f'{output}'


# Part below is part from automatic judge system from SoftUni
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

#################################### TASK CONDITION ############################
'''
                             3. Shopping Cart
Peter has decided to invite some guests. He should go shopping, but he will need 
help because  there are too many things he needs to remember. Would you assist him?
Write a function called shopping_cart that adds products to a shopping cart for 
the following three types of meals:  "Soup", "Pizza", and "Dessert". 
Every meal has a limit of products that can be added to it:
•	Soup: 3
•	Pizza: 4
•	Dessert: 2
Once you reach the limit of a meal, you should stop adding products to that meal.
The function will receive a different number of arguments. The arguments will be 
passed as tuples with two elements - the first one is the type of meal, and the 
second is the product for the meal. You need to take each argument and make a 
dictionary with the meal's name as a key and the products as a value of the 
corresponding key.
There are some additional requirements:
•	If you receive the same product for the same meal more than once,
 you must not add it again.
•	If you run into the word "Stop" (not tuple) as an argument,
 you must immediately stop adding products to the cart - just sort 
 and return the desired result as described below.
In the end, sort the meals by the number of bought products in descending order. 
If there are meals with an equal number of products, sort them (the meals) 
by their name in ascending order (alphabetically). For each meal sort its 
products in ascending order (alphabetically).
Return an output as described below.
Note: Submit only the function in the judge system
Input
•	There will be no input, just parameters passed to your function
Output
•	Return a string for each of the 3 types of a meal of the sorted result in the format:
o	"{meal_type}:"
" - {first_product_added}"
" - {second_product_added}"
 …
" - {Nth_product_added}"
o	If there are no products given for a meal, return just its name in the format shown above.
•	If there are NO products in the cart (at all), return the message: "No products in the cart!"
Constrains
•	Each tuple given will always contain the type of meal in the first position and a product in the second.
•	There will be no other meals passed than "Soup", "Pizza", and "Dessert".

_______________________________________________
Example_01

Test Code	(no input data in this task)
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

Output
Pizza:
 - cheese
 - flour
 - ham
 - mushrooms
Dessert:
 - milk
Soup:
 - carrots
 
_______________________________________________
Example_02

Test Code	(no input data in this task)
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

Output
Dessert:
 - milk
Pizza:
 - ham
Soup:

_______________________________________________
Example_03

Test Code	(no input data in this task)
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

Output
No products in the cart!

'''
