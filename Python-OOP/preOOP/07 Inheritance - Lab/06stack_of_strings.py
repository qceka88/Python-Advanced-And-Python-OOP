class Stack:

    def __init__(self):
        self.data = []

    def push(self, element):
        return self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return False if self.data else True

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"



#################################### TASK CONDITION ############################
'''
                 6.	Stack of Strings
Create a class Stack that can store only strings and has the following functionality:
•	Instance attribute: data: list
•	Method: push(element) – adds an element at the end of the stack
•	Method: pop() – removes and returns the last element in the stack
•	Method: top() - returns a reference to the topmost element of the stack
•	Method: is_empty() - returns boolean True/False
•	Override the string method to return the stack data in the format: 
"[{element(N)}, {element(N-1)} ... {element(0)}]"


'''