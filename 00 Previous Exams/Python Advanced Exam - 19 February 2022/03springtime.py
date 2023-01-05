##################################### variant 01 #####################################
from collections import defaultdict


def start_spring(**kwargs):
    output = defaultdict(list)
    for item_name, item_type in kwargs.items():
        output[item_type].append(item_name)

    sorted_output = dict(sorted(output.items(), key=lambda x: (-len(x[1]), x[0], (x[1].sort()))))

    return '\n'.join(
        f'{key}:\n' + "\n".join(f'-{name}' for name in value) for key, value in sorted_output.items())


# Part below is part from automatic judge system from SoftUni
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird", }
print(start_spring(**example_objects))

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

##################################### variant 02 #####################################

from collections import defaultdict


class StartSpring:

    def __init__(self, **kwargs):
        self.items = kwargs
        self.data = defaultdict(list)
        self.sorted_data = {}
        self.message = ''

    def process_initial_data(self):
        for item_name, item_type in self.items.items():
            self.data[item_type].append(item_name)

    def sort_data(self):
        self.sorted_data = dict(sorted(self.data.items(), key=lambda x: (-len(x[1]), x[0], (x[1].sort()))))

    def prepare_output_message(self):
        self.message = '\n'.join(f'{key}:\n' + "\n".join(f'-{name}' for name in value)
                                 for key, value in self.sorted_data.items())

    def __repr__(self):
        return self.message


def start_spring(**kwargs):
    output = StartSpring(**kwargs)
    output.process_initial_data()
    output.sort_data()
    output.prepare_output_message()
    return f'{output}'


# Part below is part from automatic judge system from SoftUni
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird", }
print(start_spring(**example_objects))

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

#################################### TASK CONDITION ############################
'''
                              03. Springtime
Spring is the season of new beginnings. Fresh buds bloom, animals awaken and the 
earth seems to come to life again. Farmers and gardeners plant their seeds and 
temperatures slowly rise. Write a function called start_spring which will receive 
a different number of keyword arguments. Each keyword holds a key with a name of 
the spring object (string), and each value holds its type (string). For example, 
dahlia="flower", shrikes="bird", dogwood="tree". The function should sort the 
given spring objects in collections by their type:
•	The collections sorted by their number of elements in descending order. 
If two or more collections have the same number of elements in them, return 
them in ascending order (alphabetically) by the type's name. 
•	Each collection's elements should be sorted in ascending order 
(alphabetically) by the object's name.
Note: Submit only the function in the judge system
Input
•	There will be no input. Just parameters passed to your function.
Output
•	Return the result, sorted as described above in the format:
o	"{type_one}:
-{spring_object_of_this_type_one}
-{spring_object_of_this_type_two}
…
-{spring_object_of_this_type_N}
{type_two}:
…
{type_N}:
…
-{last_spring_object_of_typeN}"

_______________________________________________
Example_01

Test Code	(no input data in this task)
example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))	

Output
flower:
-Dahlia
-Tulip
-Water Lilly
bird:
-Swallows
-Swifts
tree:
-Callery Pear

_______________________________________________
Example_02

Test Code	(no input data in this task)
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

Output
bird:
-Shrikes
-Swallow
-Swallows
-Thrushes
-Warblers
-Woodpeckers

_______________________________________________
Example_03

Test Code	(no input data in this task)
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

output
bird:
-Shrikes
-Swallow
-Thrushes
tree:
-Cherries
-Magnolia
-Pear
insect:
-Butterfly


'''
