class Shop:

    def __init__(self, *data):
        self.name, self.items = data

    def get_items_count(self):
        return len(self.items)


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
