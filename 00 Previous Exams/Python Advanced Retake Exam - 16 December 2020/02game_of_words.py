##################################### variant 01 #####################################
initial_string = input()
size = int(input())
moves = {'up': (-1, 0), 'down': (1, 0),
         'left': (0, -1), 'right': (0, 1)}

matrix = []
my_pos = []

for row in range(size):
    input_line = list(input())
    if 'P' in input_line:
        my_pos = [row, input_line.index('P')]
        input_line[my_pos[1]] = '-'
    matrix.append(input_line)

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input()
    row = my_pos[0] + moves[command][0]
    col = my_pos[1] + moves[command][1]
    if 0 <= row < size and 0 <= col < size:
        symbol = matrix[row][col]
        if symbol != '-':
            initial_string += symbol
            matrix[row][col] = '-'
        my_pos = [row, col]
    else:
        initial_string = initial_string[:len(initial_string) - 1]

matrix[my_pos[0]][my_pos[1]] = 'P'

print(initial_string)
print('\n'.join(''.join(row) for row in matrix))

##################################### variant 02 #####################################

class WordsGame:

    def __init__(self, string, size):
        self.string = string
        self.size = size
        self.matrix = []
        self.my_pos = []
        self.moves = {'up': (-1, 0), 'down': (1, 0),
                      'left': (0, -1), 'right': (0, 1)}

    def create_game_field(self):
        for row in range(self.size):
            input_line = list(input())
            if 'P' in input_line:
                self.my_pos = [row, input_line.index('P')]
                input_line[self.my_pos[1]] = '-'
            self.matrix.append(input_line)

    def play_the_game(self, number):
        for _ in range(number):
            command = input()
            row = self.my_pos[0] + self.moves[command][0]
            col = self.my_pos[1] + self.moves[command][1]
            if 0 <= row < self.size and 0 <= col < self.size:
                symbol = self.matrix[row][col]
                if symbol != '-':
                    self.string += symbol
                    self.matrix[row][col] = '-'
                self.my_pos = [row, col]
            else:
                self.string = self.string[:len(self.string) - 1]
        self.matrix[self.my_pos[0]][self.my_pos[1]] = 'P'

    def __repr__(self):
        message = self.string
        message += '\n' + '\n'.join(''.join(row) for row in self.matrix)
        return message

initial_string = input()
size_of_matrix = int(input())

output = WordsGame(initial_string, size_of_matrix)
output.create_game_field()
output.play_the_game(int(input()))
print(output)

#################################### TASK CONDITION ############################
'''

                           Problem 2

You will be given a string. Then, you will be given an integer N for the size of the field with square 
shape. On the next N lines, you will receive the rows of the field. The player will be placed on a random 
position, marked with "P". On random positions there will be letters. All of the empty positions will be 
marked with "-". Each turn you will be given commands for the player’s movement. If he moves to a letter, 
he consumes it, concatеnates it to the initial string and the letter disappears from the field. If he tries 
to move outside of the field, he is punished - he loses the last letter in the string, if there are any, 
and the player’s position is not changed.
At the end print all letters and the field.
Input
•	On the first line, you are given the initial string
•	On the second line, you are given the integer N - the size of the square matrix
•	The next N lines holds the values for every row
•	On the next line you receive a number M
•	On the next M lines you will get a move command
Output
•	On the first line the final state of the string
•	In the end print the matrix
Constraints
•	The size of the square matrix will be between [2…10]
•	The player position will be marked with "P"
•	The letters on the field will be any letter except for "P"
•	Move commands will be: "up", "down", "left", "right" 

_______________________________________________
Example_01

Input
Hello
4
P---
Mark
-l-y
--e-
4
down
right
right
right

Output
HelloMark
----
---P
-l-y
--e-

Explanation
The initial string we receive is "Hello". Then we receive 4x4 field and the player is on index [0;0].
Then, we start receiving commands. First the player moves to [1;0], where he consumes 'M', and then 
all letters on the right. Оur string is "HelloMark" and the player is on index [1;3].

_______________________________________________
Example_02

Input
Initial
5
-----
t-r--
--Pa-
--S--
z--t-
4
up
left
left
left

Output
Initialr
-----
P----
---a-
--S--
z--t-

Explanation
The initial string we receive is "Initial". Then we receive 5x5 field and the player is on index [2;2].
The player consumes 'r' and 't', but also tries to go out of the matrix once, 
so he loses the last character of his string – 't'. 


'''
