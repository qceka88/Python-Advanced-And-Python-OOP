class Shop:
    def __init__(self, name: str, items: list):
        self.name = name
        self.items = items

    def get_items_count(self):
        number_of_items = len(self.items)
        return number_of_items

# Part below is part from automatic judge system from SoftUni
shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())

#################################### TASK CONDITION ############################
'''
                 1.	Shop
Create a class called Shop. Upon initialization it should receive a name (string) and items (list). 
Create a method called get_items_count() which should return the number of items in the store.

_______________________________________________
Example

Test Code	(no input data in this task)

shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())

Output
3

'''
