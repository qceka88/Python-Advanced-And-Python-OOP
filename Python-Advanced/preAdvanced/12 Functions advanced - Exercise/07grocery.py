##################################### variant 02 #####################################
def grocery_store(**kwargs):
    sorted_products = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    return '\n'.join(f'{product}: {quantity}' for product, quantity in sorted_products.items())


# Part below is part from automatic judge system from SoftUni
print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))


##################################### variant 02 #####################################
class Grocery:

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.sorted_products = {}

    def func_executor(self):
        for name, quantity in sorted(self.kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
            self.sorted_products[name] = quantity

    def return_to_func(self):
        return '\n'.join(f'{product}: {quantity}' for product, quantity in self.sorted_products.items())


def grocery_store(**kwargs):
    output = Grocery(**kwargs)
    output.func_executor()
    return output.return_to_func()


# Part below is part from automatic judge system from SoftUni
print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

#################################### TASK CONDITION ############################
'''
                      7.	Grocery
Create a function called grocery_store() that receives a different number 
of key-value pairs. The key will be the product's name and the value - its quantity. 
You should return a sorted receipt for all products. They should be sorted 
by their quantity in descending order. If there are two or more products with 
the same quantity, sort them by their name's length in descending order. If there 
are two or more products with the same name's length, sort them by their name in 
ascending order (alphabetically). In the end, return a string in the following format:
"{product_name1}: {product_quantity1}
{product_name2}: {product_quantity2}
…
{product_nameN}: {product_quantityN}"

_______________________________________________
Example_01

Test Code	(no input data in this task)
print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

Output
pasta: 12
eggs: 12
bread: 5

_______________________________________________
Example_02

Test Code	(no input data in this task)
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))	

Output
eggs: 20
bread: 2
pasta: 2
carrot: 1



'''
