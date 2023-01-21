from collections import deque


class SnakeMoves:

    def __init__(self):
        self.output_message = ''
        self.snake = deque()
        self.rows = 0
        self.cols = 0
        self.matrix = []
        self.main_meth()

    def main_meth(self):
        self.define_rows_and_cols_of_matrix()
        self.define_string_representing_snake()
        self.fill_matrix_with_elements()
        self.prepare_output_message()

    def define_rows_and_cols_of_matrix(self):
        self.rows, self.cols = [int(x) for x in input().split()]

    def define_string_representing_snake(self):
        self.snake = deque(input())

    def fill_matrix_with_elements(self):
        for row in range(1, self.rows + 1):
            current_row = self.create_snake_rows(row)
            self.matrix.append(current_row)

    def create_snake_rows(self, row):
        snake_row = deque()
        for col in range(self.cols):
            symbol = self.snake[0]
            if row % 2 == 0:
                snake_row.appendleft(symbol)
            else:
                snake_row.append(symbol)
            self.snake.rotate(-1)
        return snake_row

    def prepare_output_message(self):
        self.output_message = '\n'.join(''.join(row) for row in self.matrix)

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(SnakeMoves())


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
