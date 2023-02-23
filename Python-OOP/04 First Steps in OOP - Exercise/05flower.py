class Flower:

    def __init__(self, *args):
        self.name, self.water_requirements = args
        self.is_happy = False

    def water(self, quantity):
        if self.water_requirements <= quantity:
            self.is_happy = True

    def status(self):
        condition = "" if self.is_happy else "not "
        message = f"{self.name} is {condition}happy"
        return message


# Part below is part from automatic judge system from SoftUni
flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())




#################################### TASK CONDITION ############################
'''
                    5.	Flower
Create a class called Flower. Upon initialization, the class should receive name (string)
and water_requirements (number). The flower should also have an instance attribute 
called is_happy (False by default). Add two methods to the class:
-	water(quantity) - it will water the flower. Each time check if the quantity is greater 
than or equal to the required. If it is - the flower becomes happy (set is_happy to True). 
-	status() - it should return "{name} is happy" if the flower is happy,
otherwise it should return "{name} is not happy". 
Submit only the class in the judge system.
_______________________________________________
Example

Test Code	(no input data in this task)

flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())

Output
Lilly is not happy
Lilly is not happy
Lilly is happy

'''
