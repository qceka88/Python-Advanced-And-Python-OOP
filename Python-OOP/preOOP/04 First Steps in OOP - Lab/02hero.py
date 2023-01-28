class Hero:

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f'{self.name} was defeated'

    def heal(self, health):
        self.health += health


# Part below is part from automatic judge system from SoftUni
hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))


#################################### TASK CONDITION ############################
'''
               2.	Hero
Create a class called Hero. Upon initialization it should receive
 a name (string) and health (number). Create two methods:
•	defend(damage) - reduce the given damage from the hero's health:
o	if the health become 0 or less, set it to 0 and return "{name} was defeated"

_______________________________________________
Example

Test Code	(no input data in this task)

hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))

Output
None
None
Peter was defeated

'''
