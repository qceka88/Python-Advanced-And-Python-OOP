##################################### variant 01 #####################################
from collections import deque

rows, cols = tuple(map(int, input().split()))
snake = deque(input())
matrix = []

for row in range(rows):
    result = deque()
    for col in range(cols):
        letter = snake.popleft()
        if row % 2 == 0:
            result.append(letter)
        else:
            result.appendleft(letter)
        snake.append(letter)
    matrix.append(result)

for row in matrix:
    print(*row, sep='')

##################################### variant 02 #####################################
from collections import deque


class Main:

    def __init__(self, rows, cols, snake):
        self.rows = rows
        self.cols = cols
        self.snake = deque(snake)
        self.matrix = []
        self.log = []

    def snake_method(self):
        for row in range(self.rows):
            result = deque()
            for col in range(self.cols):
                letter = self.snake.popleft()
                if row % 2 == 0:
                    result.append(letter)
                else:
                    result.appendleft(letter)
                self.snake.append(letter)
            self.matrix.append(result)

    def __repr__(self):
        result = ''
        for row in self.matrix:
            result += ''.join(row) + '\n'
        return result


rows_number, cols_number = list(map(int, input().split()))
text = input()
output = Main(rows_number, cols_number, text)
output.snake_method()
print(output)

#################################### TASK CONDITION ############################
"""
                        7.	Snake Moves
You are tasked to visualize a snake's zigzag path in a rectangular matrix with 
a size N x M.  A string represents the snake. It starts moving from the top-left 
corner to the right. When the snake reaches the end of the row, it slithers its 
way down to the next row and turns left. The moves are repeated to the very end. 
The first cell is filled with the first symbol of the snake. The second cell is 
filled with the second symbol, etc. The snake's path is as long as it takes to 
fill the matrix completely - if you reach the end of the string representing the 
snake, start again at the first symbol. In the end, you should print the snake's path.
Input
The input data consists of exactly two lines:
•	On the first line, you will receive the dimensions N x M of the 
field in format: "{rows} {columns}". 
•	On the second line, you will receive the string representing the snake
Output
•	You should print the snake's zigzag path of size N x M (rows x columns)
Constraints
•	The dimensions N and M of the matrix will be integers in the range [1 … 12]
•	The snake will be a string with length in the range [1 … 20] and 
will not contain any whitespace characters

____________________________________________________________________________________________
Example_01

Input
5 6
SoftUni	

Output
SoftUn
UtfoSi
niSoft
foSinU
tUniSo

____________________________________________________________________________________________
Example_02

Input
1 4
Python	

Output
Pyth

"""
