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

##################################### variant 01 #####################################

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
