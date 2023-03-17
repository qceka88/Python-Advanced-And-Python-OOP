class reverse_iter:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.data[self.index]
        else:
            raise StopIteration

# Part below is part from automatic judge system from SoftUni
reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)


#################################### TASK CONDITION ############################
'''
                              2.	Reverse Iter
Create a class called reverse_iter which should receive an iterable upon initialization. 
Implement the __iter__ and __next__ methods, so the iterator returns the items 
of the iterable in reversed order.

Note: Submit only the class in the judge system

_______________________________________________
Example

Test Code	(no input data in this task)

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)



Output

4
3
2
1


'''
