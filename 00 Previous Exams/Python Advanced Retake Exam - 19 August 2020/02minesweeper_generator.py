##################################### variant 01 #####################################

def check_cell_value(some_row, some_col, bombs, some_size, some_moves):
    value = 0
    for way in some_moves.values():
        cell_row = some_row + way[0]
        cell_col = some_col + way[1]
        if 0 <= cell_row < some_size and 0 <= cell_col < some_size:
            if [cell_row, cell_col] in bombs:
                value += 1
    return value


size = int(input())
bombs_number = int(input())
bombs_location = [list(map(int, input()[1:-1].split(','))) for bomb in range(bombs_number)]

moves = {'u': (-1, 0), 'ul': (-1, -1), 'ur': (-1, 1),
         'd': (1, 0), 'dl': (1, -1), 'dr': (1, 1),
         'l': (0, -1), 'r': (0, 1)}

matrix = []

for row in range(size):
    current_row = []
    for col in range(size):
        cell = 0
        if [row, col] in bombs_location:
            cell = '*'
        else:
            cell = check_cell_value(row, col, bombs_location, size, moves)
        current_row.append(cell)
    matrix.append(current_row)

print('\n'.join(' '.join(map(str, row)) for row in matrix))


##################################### variant 01 #####################################

class MinesweeperGenerator:

    def __init__(self, size, number_of_bombs):
        self.size = size
        self.number_of_bombs = number_of_bombs
        self.bombs_location = []
        self.field = []
        self.moves = {'u': (-1, 0), 'ul': (-1, -1), 'ur': (-1, 1),
                      'd': (1, 0), 'dl': (1, -1), 'dr': (1, 1),
                      'l': (0, -1), 'r': (0, 1)}

    def add_bomb_locations_to_list(self):
        for bomb in range(self.number_of_bombs):
            self.bombs_location.append(list(map(int, input()[1:-1].split(','))))

    def check_cell_value(self, some_row, some_col):
        value = 0
        for way in self.moves.values():
            cell_row = some_row + way[0]
            cell_col = some_col + way[1]
            if 0 <= cell_row < self.size and 0 <= cell_col < self.size:
                if [cell_row, cell_col] in self.bombs_location:
                    value += 1
        return value

    def generate_mines_and_cells_on_field(self):
        for row in range(self.size):
            current_row = []
            for col in range(self.size):
                cell = 0
                if [row, col] in self.bombs_location:
                    cell = '*'
                else:
                    cell = self.check_cell_value(row, col)
                current_row.append(cell)
            self.field.append(current_row)

    def __repr__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.field)


size_of_matrix = int(input())
bombs_number = int(input())

output = MinesweeperGenerator(size_of_matrix, bombs_number)
output.add_bomb_locations_to_list()
output.generate_mines_and_cells_on_field()
print(output)

#################################### TASK CONDITION ############################
'''
 
                                02 Minesweeper Generator
 
Everybody remembers the old mines game. Now it is time to create your own.
You will be given an integer n for the size of the mines field with square shape and another one for the 
number of bombs that you have to place in the field. On the next n lines, you will receive the position for 
each bomb. Your task is to create the game field placing the bombs at the correct positions and mark 
them with "*", and calculate the numbers in each cell of the field. Each cell represents a number of all 
bombs directly near it (up, down, left, right and the 4 diagonals).     
                            
 
Input
•	On the first line, you are given the integer n – the size of the square matrix.
•	On the second line – the number of the bombs.
•	The next n lines holds the position of each bomb.
Output
•	Print the matrix you've created.
Constraints
•	The size of the square matrix will be between [2…15].

_______________________________________________
Example_01

Input
4
4
(0, 3)
(1, 1)
(2, 2)
(3, 0)

Output
1 1 2 *
1 * 3 2
2 3 * 1
* 2 1 1

_______________________________________________
Example_02

Input
5
3
(1, 1)
(2, 4)
(4, 1)

Output
1 1 1 0 0
1 * 1 1 1
1 1 1 1 *
1 1 1 1 1
1 * 1 0 0

'''
