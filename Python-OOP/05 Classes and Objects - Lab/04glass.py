class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, milliliters):
        if self.capacity >= self.content + milliliters:
            self.content += milliliters
            return f"Glass filled with {milliliters} ml"

        return f"Cannot add {milliliters} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        space_left = self.capacity - self.content
        return f"{space_left} ml left"


# Part below is part from automatic judge system from SoftUni
glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())


#################################### TASK CONDITION ############################
'''
                  4.	Glass
Create a class called Glass. Upon initialization it will not receive any parameters,
you must create however an instance attribute called content which should be equal to 0.
You should also create a class attribute called capacity which should be 250 ml.
Create 3 instance methods:
-	fill(ml) - fill the glass with the given milliliters if there is enough space 
in it and return "Glass filled with {ml} ml", otherwise return "Cannot add {ml} ml"
-	empty() - empty the glass and return "Glass is now empty" 
-	info() - returns info about the glass in the format "{space_left} ml left"
_______________________________________________
Example

Test Code	(no input data in this task)

glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())

Output
Glass filled with 100 ml
Cannot add 200 ml
Glass is now empty
Glass filled with 200 ml
50 ml left

'''
