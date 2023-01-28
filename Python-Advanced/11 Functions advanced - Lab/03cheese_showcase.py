class Cheeses:

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.sorted_data = None
        self.result = ''

    def main_meth(self):
        self.sort_data()
        self.return_output_result()
        return self.result

    def sort_data(self):
        self.sorted_data = sorted(self.kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    def return_output_result(self):
        self.result = '\n'.join(
            name + '\n' + '\n'.join(str(i) for i in sorted(qty)[::-1]) for name, qty in self.sorted_data)


def sorting_cheeses(**kwargs):
    output = Cheeses(**kwargs).main_meth()
    return output

# This part below is part from automatic test code from Judge system in SoftUni
print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)


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

