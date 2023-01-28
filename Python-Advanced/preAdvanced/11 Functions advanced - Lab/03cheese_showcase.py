##################################### variant 01 #####################################
def sorting_cheeses(**kwargs):
    some_sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for brand, quantity in some_sorted_cheeses:
        result.append(brand)
        result.append('\n'.join([str(x) for x in sorted(quantity, reverse=True)]))
    return '\n'.join(result)


##################################### variant 02 #####################################

class Sorting:

    def __init__(self, some_dict):
        self.some_dict = some_dict

    def sorting(self):
        result = []
        sorted_some_dict = sorted(self.some_dict.items(), key=lambda x: (-len(x[1]), x[0]))
        result = []
        for brand, quantity in sorted_some_dict:
            result.append(brand)
            result.append('\n'.join([str(x) for x in sorted(quantity, reverse=True)]))
        return '\n'.join(result)


def sorting_cheeses(**kwargs):
    output = Sorting(kwargs).sorting()
    return output

#################################### TASK CONDITION ############################
'''
             3.	Cheese Showcase
White a function called sorting_cheeses that receives keywords arguments:
•	The key represents the name of the cheese
•	The value is a list of quantities (integers) of the pieces of the given cheese
The function should return the cheeses and their pieces' quantities 
sorted by the number of pieces of a cheese kind in descending order. 
If two or more cheeses have the same number of pieces, sort them by their 
names in ascending order (alphabetically). For each kind of cheese, return 
their pieces quantities in descending order.

_______________________________________________
Example_01

Test Code	(no input data in this task)
print(
    sorting_cheeses(
        Parmesan=[102, 120, 135], 
        Camembert=[100, 100, 105, 500, 430], 
        Mozzarella=[50, 125],
    )
)

Output
Camembert
500
430
105
100
100
Parmesan
135
120
102
Mozzarella
125


_______________________________________________
Example_02

Test Code	(no input data in this task)
print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

Output
Brie
150
125
Feta
515
150
Parmigiano
215
165

'''
