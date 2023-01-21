class Bombs:

    def __init__(self):
        self.output_message = ''
        self.rows = int(input())
        self.matrix = []
        self.bombs = []
        self.main_meth()

    def main_meth(self):
        self.fill_matrix_with_elements()
        self.define_bombs_locations()
        self.start_bombing()
        self.prepare_output_message()

    def fill_matrix_with_elements(self):
        self.matrix = [[int(x) for x in input().split()] for _ in range(self.rows)]

    def define_bombs_locations(self):
        self.bombs = [[int(i) for i in bomb.split(',')] for bomb in input().split()]

    def start_bombing(self):
        for bomb in self.bombs:
            x, y = bomb
            power_of_bomb = self.matrix[x][y]
            if power_of_bomb > 0:
                self.matrix[x][y] = 0
                collateral_damage = self.check_range_of_bomb(x, y)
                self.detonate_bomb_and_damage_cells(collateral_damage, power_of_bomb)

    def check_range_of_bomb(self, x, y):
        cells_for_destroy = []
        for row in range(x - 1, x + 2):
            for col in range(y - 1, y + 2):
                if 0 <= row < self.rows and 0 <= col < len(self.matrix[row]):
                    cells_for_destroy.append([row, col])
        return cells_for_destroy

    def detonate_bomb_and_damage_cells(self, cells, explosion):
        for target in cells:
            cell_value = self.matrix[target[0]][target[1]]
            if cell_value > 0:
                self.matrix[target[0]][target[1]] -= explosion

    def prepare_output_message(self):
        alive_cells = [cell for row in self.matrix for cell in row if cell > 0]
        self.output_message = f'Alive cells: {len(alive_cells)}\n'
        self.output_message += f'Sum: {sum(alive_cells)}\n'
        self.output_message += '\n'.join(' '.join(str(x) for x in row) for row in self.matrix)

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(Bombs())



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
