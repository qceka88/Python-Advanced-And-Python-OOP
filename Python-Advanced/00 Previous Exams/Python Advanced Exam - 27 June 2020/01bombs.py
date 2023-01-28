##################################### variant 01 #####################################
from collections import deque

bomb_effects = deque(int(n) for n in input().split(','))
bomb_casing = [int(n) for n in input().split(',')]

bombs_names = {40: 'Datura Bombs',
               60: 'Cherry Bombs',
               120: 'Smoke Decoy Bombs'}
created_bombs = {'Datura Bombs': 0,
                 'Cherry Bombs': 0,
                 'Smoke Decoy Bombs': 0}

enough_bombs = False
while True:
    effect = bomb_effects.popleft()
    casing = bomb_casing.pop()
    value = effect + casing

    if value not in bombs_names:
        if value >= 45:
            while value not in bombs_names:
                effect -= 5
                value = effect + casing
                if value < min(bombs_names.keys()):
                    break
    if value in bombs_names:
        created_bombs[bombs_names[value]] += 1

    enough_bombs = created_bombs['Datura Bombs'] >= 3 \
                   and created_bombs['Cherry Bombs'] >= 3 \
                   and created_bombs['Smoke Decoy Bombs'] >= 3

    if enough_bombs or not bomb_effects or not bomb_casing:
        break

if enough_bombs:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
left_bombs_effects = 'empty' if not bomb_effects else ', '.join(map(str, bomb_effects))
print(f'Bomb Effects: {left_bombs_effects}')
left_bombs_casing = 'empty' if not bomb_casing else ', '.join(map(str, bomb_casing))
print(f'Bomb Casings: {left_bombs_casing}')
print('\n'.join(f'{name}: {count}' for name, count in sorted(created_bombs.items())))

##################################### variant 02 #####################################

from collections import deque


class Bombs:

    def __init__(self, effects, casings):
        self.effects = effects
        self.casings = casings
        self.bombs_names = {40: 'Datura Bombs',
                            60: 'Cherry Bombs',
                            120: 'Smoke Decoy Bombs'}
        self.created_bombs = {'Datura Bombs': 0,
                              'Cherry Bombs': 0,
                              'Smoke Decoy Bombs': 0}
        self.enough_bombs = False
        self.message = ''

    def decreasing_effect_value(self, effect_value, casing_value):
        combination = effect_value + casing_value
        while combination not in self.bombs_names:
            effect_value -= 5
            combination = effect_value + casing_value
            if combination < min(self.bombs_names.keys()):
                break
        return combination

    def check_combinations(self):
        while True:
            current_effect = self.effects.popleft()
            current_casing = self.casings.pop()
            value = current_effect + current_casing

            if value not in self.bombs_names and value >= min(self.bombs_names.keys()) + 5:
                value = self.decreasing_effect_value(current_effect, current_casing)

            if value in self.bombs_names:
                self.created_bombs[self.bombs_names[value]] += 1
            else:
                continue

            self.enough_bombs = self.created_bombs['Datura Bombs'] >= 3 \
                                and self.created_bombs['Cherry Bombs'] >= 3 \
                                and self.created_bombs['Smoke Decoy Bombs'] >= 3

            if self.enough_bombs or not self.effects or not self.casings:
                break

    def prepare_result(self):
        if self.enough_bombs:
            self.message = "Bene! You have successfully filled the bomb pouch!"
        else:
            self.message = "You don't have enough materials to fill the bomb pouch."
        left_bombs_effects = 'empty' if not self.effects else ', '.join(map(str, self.effects))
        self.message += f'\nBomb Effects: {left_bombs_effects}'
        left_bombs_casing = 'empty' if not self.casings else ', '.join(map(str, self.casings))
        self.message += f'\nBomb Casings: {left_bombs_casing}'
        self.message += '\n' + '\n'.join(f'{name}: {count}' for name, count in sorted(self.created_bombs.items()))

    def __repr__(self):
        return self.message


bomb_effects = deque(int(n) for n in input().split(','))
bomb_casings = [int(n) for n in input().split(',')]

output = Bombs(bomb_effects, bomb_casings)
output.check_combinations()
output.prepare_result()
print(output)


#################################### TASK CONDITION ############################
'''
                       01Bombs

Ezio is still learning how to make bombs. With their help, he will save civilization. 
We should help Ezio to make his perfect bombs.

You will be given two sequences of integers, representing bomb effects and bomb casings.
You need to start from the first bomb effect and try to mix it with the last bomb casing. If the sum of
their values is equal to any of the materials in the table below – create the bomb corresponding to the 
value and remove both bomb materials. Otherwise, just decrease the value of the bomb casing by 5.You need to
stop combining when you have no more bomb effects or bomb casings, or you successfully filled the bombs pouch.
Bombs:
•	Datura Bombs: 40
•	Cherry Bombs: 60
•	Smoke Decoy Bombs: 120
To fill the bomb pouch, Ezio needs three of each of the bomb types.
Input
•	On the first line, you will receive the integers representing the bomb effects, separated by ", ".
•	On the second line, you will receive the integers representing the bomb casings, separated by ", ".
Output
•	On the first line, print:
o	if Ezio succeeded to fulfill the bomb pouch: "Bene! You have successfully filled the bomb pouch!"
o	if Ezio didn't succeed to fulfill the bomb pouch: "You don't have enough materials to fill the bomb pouch."
•	On the second line, print all bomb effects left:
o	If there are no bomb effects: "Bomb Effects: empty"
o	If there are effects: "Bomb Effects: {bombEffect1}, {bombEffect2}, (…)"
•	On the third line, print all bomb casings left:
o	If there are no bomb casings: "Bomb Casings: empty"
o	If there are casings: "Bomb Casings: {bombCasing1}, {bombCasing2}, (…)"
•	Then, you need to print all bombs and the count you have of them, ordered alphabetically:
o	"Cherry Bombs: {count}"
o	"Datura Bombs: {count}"
o	"Smoke Decoy Bombs: {count}"
Constraints
•	All of the given numbers will be valid integers in the range [0, 120].
•	There will be no cases with negative material.

_______________________________________________
Example_01

Input
5, 25, 25, 115
5, 15, 25, 35

Output
You don't have enough materials to fill the bomb pouch.
Bomb Effects: empty
Bomb Casings: empty
Cherry Bombs: 0
Datura Bombs: 3
Smoke Decoy Bombs: 1

Example
1) 5 + 35 = 40 -> Datura Bomb. Remove both.
2) 25 + 25 = 50 -> can't create bomb. Bomb casing should be decreased with 5 -> 20
3) 25 + 20 = 45 -> can't create bomb. Bomb casing should be decreased with 5 -> 15
4) 25 + 15 = 40 -> Datura Bomb. Remove both
…

_______________________________________________
Example_02

Input
30, 40, 5, 55, 50, 100, 110, 35, 40, 35, 100, 80
20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 10

Output
Bene! You have successfully filled the bomb pouch!
Bomb Effects: 100, 80
Bomb Casings: 20
Cherry Bombs: 3
Datura Bombs: 4
Smoke Decoy Bombs: 3

Output
After creating a bomb with bomb effect 35 and bomb casing 25, have created 3 Cherry bombs, 
4 Datura bombs, and 3 Smoke Decoy bombs. From all of the bomb types we have 3 bombs,
so the program ends.


'''
