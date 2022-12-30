##################################### variant 01 #####################################
def even_odd_filter(**kwargs):
    result = {}

    for key, value in kwargs.items():
        parity = 0 if key == 'even' else 1
        numbers = [num for num in value if num % 2 == parity]
        result[key] = numbers
    sorted_result = {key: value for key, value in sorted(result.items(), key=lambda x: -len(x[1]))}
    return sorted_result


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
##################################### variant 02 #####################################
class Main:

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.result = {}

    def filter(self):
        for key, value in self.kwargs.items():
            parity = 0 if key == 'even' else 1
            numbers = [num for num in value if num % 2 == parity]
            self.result[key] = numbers

    def return_data(self):
        return {key: value for key, value in sorted(self.result.items(), key=lambda x: -len(x[1]))}


def even_odd_filter(**kwargs):
    result = Main(**kwargs)
    result.filter()
    return result.return_data()


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))


#################################### TASK CONDITION ############################
'''
                    4.	Numbers Filter
Create a function called even_odd_filter() that can receive a different 
number of named arguments. The keys will be "even" and/or "odd", and the 
values will be a list of numbers. When the key is "odd", you should extract 
only the odd numbers from its list. When the key is "even", you should extract 
only the even numbers from its list. The function should return a dictionary 
sorted by the length of the lists in descending order. There will be no case 
of lists with the same length. Submit only your function in the judge system.

_______________________________________________
Example_01

Test Code	(no input data in this task)t
print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))	

Output
{'even': [4, 10, 2, 2], 'odd': [1, 3, 5]}

_______________________________________________
Example_02

Test Code	(no input data in this task)
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

Output
{'odd': [5]}

'''
