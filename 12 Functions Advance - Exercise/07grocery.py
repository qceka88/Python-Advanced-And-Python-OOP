class GroceryStore:

    def __init__(self, **products):
        self.products = products
        self.sorted_products = {}
        self.result = []

    def main_meth(self):
        self.sort_data_in_sorted_products_dict()
        return self.result_message()

    def sort_data_in_sorted_products_dict(self):
        for product, quantity in sorted(self.products.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
            self.result.append(f"{product}: {quantity}")

    def result_message(self):
        message = '\n'.join(self.result)
        return message


def grocery_store(**kwargs):
    output = GroceryStore(**kwargs).main_meth()
    return output

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