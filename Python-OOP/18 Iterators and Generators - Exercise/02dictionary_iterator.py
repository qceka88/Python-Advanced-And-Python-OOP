class dictionary_iter:

    def __init__(self, some_dict):
        self.list_from_dict = list(some_dict.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1

        if self.index == len(self.list_from_dict):
            raise StopIteration

        return self.list_from_dict[self.index]


# Part below is part from automatic judge system from SoftUni
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

#################################### TASK CONDITION ############################
'''
                  2.	Dictionary Iterator
Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object. 
Implement the iterator to return each key-value pair of the dictionary as a tuple 
of two elements (the key and the value).
Note: Submit only the class in the judge system


_______________________________________________
Example_01

Test Code	(no input data in this task)


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)



Output

(1, '1')
(2, '2')


_______________________________________________
Example_02

Test Code	(no input data in this task)


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)


Output

("name", "Peter")
("age", 24)

'''
