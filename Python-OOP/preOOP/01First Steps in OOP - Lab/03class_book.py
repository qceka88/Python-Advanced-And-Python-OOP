class Book:

    def __init__(self, *args):
        self.name = args[0]
        self.author = args[1]
        self.pages = int(args[2])

    def name(self):
        return self.name()

    def author(self):
        return self.author()

    def pages(self):
        return self.pages


# Part below is part from automatic judge system from SoftUni
book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)


#################################### TASK CONDITION ############################
'''
3.	Class Book
Create a class called Book. It should have an __init__() method that should receive:
•	name: string
•	author: string
•	pages: int
Submit only the class in the judge system. 

_______________________________________________
Example_01

Test Code	(no input data in this task)
book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)

Output
My Book
Me
200

'''