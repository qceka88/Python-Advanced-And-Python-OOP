##################################### variant 01 #####################################
def feed_the_snake(row, col):
    global food, snake_pos
    snake_pos = [row, col]
    food += 1


def snake_take_burrow(row, col):
    global snake_pos, territory, burrows_pos
    territory[row][col] = '.'
    if burrows_pos[0] == [row, col]:
        snake_pos = burrows_pos[1]
    else:
        snake_pos = burrows_pos[0]


def move_the_snake(row, col):
    global snake_pos
    snake_pos = [row, col]


size = int(input())

actions = {'*': feed_the_snake,
           'B': snake_take_burrow,
           '-': move_the_snake}

territory = []
snake_pos = []
burrows_pos = []
moves = {"up": (-1, 0), "down": (1, 0),
         "left": (0, -1), "right": (0, 1)}

for row in range(size):
    line = list(input())
    if 'S' in line:
        snake_pos = [row, line.index('S')]
    for col in range(size):
        symbol = line[col]
        if symbol == 'B':
            burrows_pos.append([row, col])
    territory.append(line)

food = 0
while True:
    way = input()
    territory[snake_pos[0]][snake_pos[1]] = '.'
    snake_row = snake_pos[0] + moves[way][0]
    snake_col = snake_pos[1] + moves[way][1]

    if 0 <= snake_row < size and 0 <= snake_col < size:
        symbol = territory[snake_row][snake_col]
        actions[symbol](snake_row, snake_col)

    else:
        break
    territory[snake_pos[0]][snake_pos[1]] = 'S'
    if food == 10:
        break
print("Game over!" if food < 10 else "You won! You fed the snake.")
print(f'Food eaten: {food}')
print('\n'.join(''.join(row) for row in territory))

##################################### variant 02 #####################################

class Snake:

    def __init__(self, size):
        self.size = size
        self.territory = []
        self.snake_pos = []
        self.burrows_pos = []
        self.actions = {'*': self.feed_the_snake,
                        'B': self.snake_take_burrow,
                        '-': self.move_the_snake}
        self.moves = {"up": (-1, 0), "down": (1, 0),
                      "left": (0, -1), "right": (0, 1)}
        self.food = 0
        self.message = ''

    def create_snake_territory(self):
        for row in range(size):
            line = list(input())
            if 'S' in line:
                self.snake_pos = [row, line.index('S')]
            for col in range(size):
                symbol = line[col]
                if symbol == 'B':
                    self.burrows_pos.append([row, col])
            self.territory.append(line)

    def feed_the_snake(self, row, col):
        self.snake_pos = [row, col]
        self.food += 1

    def snake_take_burrow(self, row, col):
        self.territory[row][col] = '.'
        if self.burrows_pos[0] == [row, col]:
            self.snake_pos = self.burrows_pos[1]
        else:
            self.snake_pos = self.burrows_pos[0]

    def move_the_snake(self, row, col):
        self.snake_pos = [row, col]

    def move_snake_on_territory(self):
        while self.food < 10:
            way = input()
            self.territory[self.snake_pos[0]][self.snake_pos[1]] = '.'
            snake_row = self.snake_pos[0] + self.moves[way][0]
            snake_col = self.snake_pos[1] + self.moves[way][1]

            if 0 <= snake_row < size and 0 <= snake_col < size:
                symbol = self.territory[snake_row][snake_col]
                self.actions[symbol](snake_row, snake_col)
            else:
                break
            self.territory[self.snake_pos[0]][self.snake_pos[1]] = 'S'

    def prepare_result(self):
        self.message = "Game over!" if self.food < 10 else "You won! You fed the snake."
        self.message += f'\nFood eaten: {self.food}\n'
        self.message += '\n'.join(''.join(row) for row in self.territory)

    def __repr__(self):
        return self.message


size = int(input())

output = Snake(size)
output.create_snake_territory()
output.move_snake_on_territory()
output.prepare_result()
print(output)


#################################### TASK CONDITION ############################
'''

                                 03Snake

Everybody remembers the old snake game. Now it is time to create your own.

You will be given an integer n for the size of the snake territory with square shape. On the next n lines, 
you will receive the rows of the territory. The snake will be placed on a random position, marked with the 
letter 'S'. On random positions there will be food, marked with '*'. There might also be a lair on the 
territory. The lair has two burrows. They are marked with the letter - 'B'. All of the empty positions 
will be marked with '-'. Each turn, you will be given command for the snake’s movement. When the snake 
moves it leaves a trail marked with '.' Move commands will be: "up", "down", "left", "right".
If the snake moves to a food, it eats the food and increases the food quantity with one.
If it goes inside of a burrow, it goes out on the position of the other burrow and then both burrows
disappear. If the snake goes out of its territory, it loses, can't return back and the program ends. 
The snake needs at least 10 food quantity to win.
When the snake has gone outside of its territory or has eaten enough food, the game ends.
Input
•	On the first line, you are given the integer n – the size of the square matrix.
•	The next n lines holds the values for every row.
•	On each of the next lines you will get a move command.
Output
•	On the first line:
o	If the snake goes out of its territory, print: "Game over!"
o	If the snake eat enough food, print: "You won! You fed the snake."
•	On the second line print all food eaten: "Food eaten: {food quantity}"
•	In the end print the matrix.
Constraints
•	The size of the square matrix will be between [2…10].
•	There will always be 0 or 2 burrows, marked with - 'B'.
•	The snake position will be marked with 'S'.
•	The snake will always either go outside its territory or eat enough food.
•	There will be no case in which the snake will go through itself.

_______________________________________________
Example_01

Input
6
-----S
----B-
------
------
--B---
--*---
left
down
down
down
left

Output
Game over!
Food eaten: 1
----..
----.-
------
------
--.---
--.---

Explanation
  1) left     2) down     3) down     5) down
   ----S.      ----..      ----..      ----..
   ----B-      ----.-      ----.-      ----.-
   ------      ------      ------      ------
   ------      ------      ------      ------
   --B---      --S---      --.---      --.---
   --*---      --*---      --S---      --.---
3) eat the food: '*' (5, 2)
5) the snake goes out from its territory and the program ends

_______________________________________________
Example_02

Input
7
--***S-
--*----
--***--
---**--
---*---
---*---
---*---
left
left
left
down
down
right
right
down
left
down

Output
You won! You fed the snake.
Food eaten: 10
--....-
--.----
--...--
---..--
---S---
---*---
---*---	


'''
