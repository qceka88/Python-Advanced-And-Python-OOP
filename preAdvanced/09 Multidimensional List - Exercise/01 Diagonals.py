##################################### variant 01 #####################################

from collections import deque

size = int(input())

matrix = [[int(x) for x in input().split(', ')] for row in range(int(size))]

primary_diagonal = []
secondary_diagonal = deque()

for i in range(len(matrix)):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.appendleft(matrix[(len(matrix) - 1) - i][i])

print(f'Primary diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}')

##################################### variant 02 #####################################

from collections import deque


class Main:

    def __init__(self, some_size):
        self.some_size = some_size
        self.matrix = []
        self.primary_diagonal = []
        self.secondary_diagonal = deque()
        self.log = ''

    def create_matrix(self):
        self.matrix = [[int(x) for x in input().split(', ')] for row in range(int(self.some_size))]

    def find_diagonals(self):
        for i in range(len(self.matrix)):
            self.primary_diagonal.append(self.matrix[i][i])
            self.secondary_diagonal.appendleft(self.matrix[(len(self.matrix) - 1) - i][i])

    def printing(self):
        print(f'Primary diagonal: {", ".join(map(str, self.primary_diagonal))}. Sum: {sum(self.primary_diagonal)}')
        print(
            f'Secondary diagonal: {", ".join(map(str, self.secondary_diagonal))}. Sum: {sum(self.secondary_diagonal)}')


size = int(input())
output = Main(size)
output.create_matrix()
output.find_diagonals()
output.printing()
