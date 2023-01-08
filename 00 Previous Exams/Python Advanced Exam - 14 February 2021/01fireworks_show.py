##################################### variant 01 #####################################

from collections import deque

fireworks_effects = deque(int(num) for num in input().split(', '))
explosive_power = list(map(int, input().split(', ')))
created_fireworks = {'Palm Fireworks': 0,
                     'Willow Fireworks': 0,
                     'Crossette Fireworks': 0}
is_success = False
while explosive_power and fireworks_effects and not is_success:
    power = explosive_power.pop()
    if power > 0:
        while fireworks_effects:
            effect = fireworks_effects.popleft()
            if effect > 0:
                product = power + effect

                if product % 3 == 0 and product % 5 != 0:
                    created_fireworks['Palm Fireworks'] += 1
                elif product % 5 == 0 and product % 3 != 0:
                    created_fireworks['Willow Fireworks'] += 1
                elif product % 3 == 0 and product % 5 == 0:
                    created_fireworks['Crossette Fireworks'] += 1
                else:
                    fireworks_effects.append(effect - 1)
                    explosive_power.append(power)
                if created_fireworks['Palm Fireworks'] >= 3 and created_fireworks['Willow Fireworks'] >= 3 and \
                        created_fireworks['Crossette Fireworks'] >= 3:
                    is_success = True
            else:
                explosive_power.append(power)
            break

if is_success:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if fireworks_effects:
    print(f"Firework Effects left: {', '.join(map(str, fireworks_effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")
print('\n'.join(f'{key}: {value}' for key, value in created_fireworks.items()))

##################################### variant 02 #####################################


from collections import deque


class FireworkShow:

    def __init__(self, effects, powers):
        self.effects = effects
        self.powers = powers
        self.created_fireworks = {'Palm Fireworks': 0,
                                  'Willow Fireworks': 0,
                                  'Crossette Fireworks': 0}
        self.is_success = False
        self.message = ''

    def produce_fireworks(self):
        while self.effects and self.powers and not self.is_success:
            power = self.powers.pop()
            if power > 0:
                while self.effects:
                    effect = self.effects.popleft()
                    if effect > 0:
                        product = power + effect

                        if product % 3 == 0 and product % 5 != 0:
                            self.created_fireworks['Palm Fireworks'] += 1
                        elif product % 5 == 0 and product % 3 != 0:
                            self.created_fireworks['Willow Fireworks'] += 1
                        elif product % 3 == 0 and product % 5 == 0:
                            self.created_fireworks['Crossette Fireworks'] += 1
                        else:
                            self.effects.append(effect - 1)
                            self.powers.append(power)
                        if self.created_fireworks['Palm Fireworks'] >= 3 and self.created_fireworks[
                            'Willow Fireworks'] >= 3 and \
                                self.created_fireworks['Crossette Fireworks'] >= 3:
                            self.is_success = True
                    else:
                        self.powers.append(power)
                    break

    def prepare_result(self):
        if self.is_success:
            self.message = "Congrats! You made the perfect firework show!"
        else:
            self.message = "Sorry. You can't make the perfect firework show."
        if self.effects:
            self.message += f"\nFirework Effects left: {', '.join(map(str, self.effects))}"
        if explosive_power:
            self.message += f"\nExplosive Power left: {', '.join(map(str, explosive_power))}"
        self.message += '\n' + '\n'.join(f'{key}: {value}' for key, value in self.created_fireworks.items())

    def __repr__(self):
        return f'{self.message}'


fireworks_effects = deque(int(num) for num in input().split(', '))
explosive_power = list(map(int, input().split(', ')))
output = FireworkShow(fireworks_effects, explosive_power)
output.produce_fireworks()
output.prepare_result()
print(output)


#################################### TASK CONDITION ############################
'''
                        Problem 1
Maria wants to make a firework show for the wedding of her best friend. 
We should help her to make the perfect firework show.

First, you will be given a sequence of integers representing firework effects. 
Afterwards you will be given another sequence of integers representing explosive power.
You need to start from the first firework effect and try to mix it with the last 
explosive power. If the sum of their values is:
•	divisible by 3, but it is not divisible by 5 – create Palm firework and remove both materials
•	divisible by 5, but it is not divisible by 3 – create Willow firework and remove both materials
•	divisible by both 3 and 5 – create Crossette firework and remove both materials
Otherwise, decrease the value of the firework effect by 1 and move it at the end of the sequence. 
Then, try to mix the same explosive power with the next firework effect. 
If any value is equal to or below 0, you should remove it from the sequence before trying to mix it with the other. 
When you have successfully prepared enough fireworks for the show or you have no more firework 
punches or explosive power, you need to stop mixing. 
To make the perfect firework show, Maria needs 3 of each of the firework types.
Input
•	On the first line, you will receive the integers representing the firework effects, separated by ", ".
•	On the second line, you will receive the integers representing the explosive power, separated by ", ".
Output
•	On the first line, print:
o	if Maria successfully prepared the firework show: "Congrats! You made the perfect firework show!"
o	if Maria failed to prepare it: "Sorry. You can't make the perfect firework show."
•	On the second line, print all firework effects left if there are any: 
o	"Firework Effects left: {effect1}, {effect2}, (…)"
•	On the third line, print all explosive fillings left if there are any: 
o	" Explosive Power left: {filling1}, {filling2}, (…)"
•	Then, you need to print all fireworks and the amount you have of them:
o	"Palm Fireworks: {count}"
o	"Willow Fireworks: {count}"
o	"Crossette Fireworks: {count}"
Constraints
•	All the given numbers will be integers in the range [-100, 100].
•	There will be no cases with empty sequences.

_______________________________________________
Example_01

Input
5, 6, 4, 16, 11, 5, 30, 2, 3, 27
1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22

Output
Congrats! You made the perfect firework show!
Palm Fireworks: 4
Willow Fireworks: 3
Crossette Fireworks: 3

Explanation
1) 5 + 22 = 27 is devisible by 3 -> Palm Firework. Remove both.
2) 6 + 7 = 13 -> can't create firework. Firework effect should be decreased with 1 -> 5 and moved at the end 
3) 4 + 7= 11 -> can't create firework. Firework effect should be decreased with 1 -> 3 and moved at the end
3) 16 + 7 = 23 -> can't create firework. Firework effect should be decreased with 1 -> 15 and moved at the end
4) 11 + 7 = 18 is devisible by 3 -> Palm Firework. Remove both.
5) 5 + 5 = 10 is devisible by 5 -> Willow Firework. Remove both.
6) 30 + 3 = 33 is devisible by 3 -> Palm Firework. Remove both.
7) 2 + 19 = 21 is devisible by 3 -> Palm Firework. Remove both. 
8) 3 + 32 = 35 is devisible by 5 -> Willow Firework. Remove both.
9) (-7) is negative, so we remove it before mixing.
10) 27 + 3 = 30 is devisible by 5 and 3 -> Crossette Firework. Remove both.
11) 5 + 5 = 10 is devisible by 5 -> Willow Firework. Remove both.
12) 3 + 13 = 16 -> can't create firework. Firework effect should be decreased with 1 -> 2 and moved at the end
13) 15 + 13 = 28 -> can't create firework. Firework effect should be decreased with 1 -> 14 and moved at the end
14) 2 + 13 = 15 is devisible by 5 and 3 -> Crossette Firework. Remove both.
15) 1 + 14 = 15 is devisible by 5 and 3 -> Crossette Firework. Remove both.
We have enough fireworks to make a firework show. 

_______________________________________________
Example_02

Input
-15, -8, 0, -16, 0, -22
10, 5

Output
Sorry. You can't make the perfect firework show.
Explosive Power left: 10, 5
Palm Fireworks: 0
Willow Fireworks: 0
Crossette Fireworks: 0

Explanation
After removing all the invalid integers, the firework effects's sequence is empty and the program ends.


'''