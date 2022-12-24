##################################### variant 01 #####################################
def check_range(r, c, m):  # r- Row, c - Col, m - Matrix
    damaged_cells = []
    for row in range(r - 1, r + 2):
        if 0 <= row < len(m):
            for col in range(c - 1, c + 2):
                if 0 <= col < len(m[row]):
                    damaged_cells.append([row, col])
    return damaged_cells


size = int(input())
matrix = [[int(x) for x in input().split()] for row in range(size)]
bombs = [list(map(int, coordinates.split(','))) for coordinates in input().split()]

for bomb in bombs:
    x, y = bomb
    power = matrix[x][y]
    if matrix[x][y] > 0:
        matrix[x][y] = 0
        collateral_damage = check_range(x, y, matrix)
        for act in collateral_damage:
            row_i, col_i = act
            if matrix[row_i][col_i] > 0:
                matrix[row_i][col_i] -= power
alive_cells = [i for row in matrix for i in row if i > 0]
print(f'Alive cells: {len(alive_cells)}')
print(f'Sum: {sum(alive_cells)}')

for i in matrix:
    print(*i)


##################################### variant 02 #####################################
class CheckRange:

    def __init__(self, row, col, matrix):
        self.row = row
        self.col = col
        self.matrix = matrix
        self.damaged_cells = []

    def damaging(self):
        for row in range(self.row - 1, self.row + 2):
            if 0 <= row < len(self.matrix):
                for col in range(self.col - 1, self.col + 2):
                    if 0 <= col < len(self.matrix[row]):
                        self.damaged_cells.append([row, col])
        return self.damaged_cells


class Main:

    def __init__(self, size):
        self.size = size
        self.matrix = []
        self.bombs_locations = []
        self.log = []

    def the_matrix(self):
        self.matrix = [[int(x) for x in input().split()] for row in range(self.size)]

    def targets(self):
        self.bombs_locations = [list(map(int, coordinates.split(','))) for coordinates in input().split()]

    def bombing(self):
        for bomb in self.bombs_locations:
            x, y = bomb
            power = self.matrix[x][y]
            if self.matrix[x][y] > 0:
                self.matrix[x][y] = 0
                collateral_object = CheckRange(x, y, self.matrix).damaging()
                for act in collateral_object:
                    row_i, col_i = act
                    if self.matrix[row_i][col_i] > 0:
                        self.matrix[row_i][col_i] -= power

    def resulting(self):
        alive_cells = [i for row in self.matrix for i in row if i > 0]
        self.log.append(f'Alive cells: {len(alive_cells)}')
        self.log.append(f'Sum: {sum(alive_cells)}')
        for row in self.matrix:
            self.log.append(' '.join(map(str, row)))

    def __repr__(self):
        return '\n'.join(self.log)


some_size = int(input())
output = Main(some_size)
output.the_matrix()
output.targets()
output.bombing()
output.resulting()
print(output)


#################################### TASK CONDITION ############################
"""
                           8.	*Bombs
You will be given a square matrix of integers, each integer separated by a 
single space, and each row will be on a new line. On the last line of input, 
you will receive indexes - coordinates of several cells separated by a single 
space, in the following format: "{row1},{column1} {row2},{column2} … {row3},{column3}".
On those cells, there are bombs. You must detonate every bomb in the order 
they were given. When a bomb explodes, it deals damage equal to its integer 
value to all the cells around it (in every direction and in all diagonals). 
One bomb can't explode more than once, and after it does, its value becomes 0. 
When a cell's value reaches 0 or below, it dies. Dead cells can't explode.
You must print the count of all alive cells and their sum. Afterward, print 
the matrix with all its cells (including the dead ones).
Input
•	On the first line, you are given the integer N - the size of the square matrix.
•	The following N lines hold each column's values - N numbers separated by a space.
•	On the last line, you will receive the coordinates of the cells with the bombs 
in the format described above.
Output
•	On the first line, you need to print the count of all alive cells in the format: 
"Alive cells: {alive_cells}"
•	On the second line, you need to print the sum of all alive cells in the format: 
"Sum: {sum_of_cells}"
•	In the end, print the matrix. A space must separate the cells.
Constraints
•	The size of the matrix will be between [0…1000].
•	The bomb coordinates will always be in the matrix.
•	The bomb's values will always be greater than 0.
•	The integers of the matrix will be in the range [1…10000]. 

____________________________________________________________________________________________
Example_01

Input
4
8 3 2 5
6 4 7 9
9 9 3 6
6 8 1 2
1,2 2,1 2,0	

Output
Alive cells: 3
Sum: 12
8 -4 -5 -2
-3 -3 0 2
0 0 -4 -1
-3 -1 -1 2	

Explanation
1) The bomb with value 7 will explode and reduce the values of the cells around it. 
2) The bomb with coordinates 2,1 and value 9 will explode and reduce its neighbor cells. 
3) The bomb with coordinates 2,0 and value 9 will explode. 
After that, you have to print the count of the alive cells - 3, and their sum - 12. 
Print the matrix after the explosions.

____________________________________________________________________________________________
Example_02

Input
3
7 8 4
3 1 5
6 4 9
0,2 1,0 2,2	

Output
Alive cells: 3
Sum: 8
4 1 0
0 -3 -8
3 -8 0
	

"""
