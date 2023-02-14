class RallyRacing:
    __moves = {'up': (-1, 0),
               'down': (1, 0),
               'left': (0, -1),
               'right': (0, 1)}

    def __init__(self, track_size, number_racing):
        self.result = []
        self.__actions = {'T': self.tunnel,
                          'F': self.finish,
                          '.': self.move}
        self.track_size = track_size
        self.number_racing = number_racing
        self.is_finish = False
        self.track = []
        self.car_data = [[0, 0], 0]
        self.tunnels = []
        self.main_method()

    def main_method(self):
        self.create_track()
        self.start_racing()
        self.prepare_result()

    def create_track(self):
        for row in range(self.track_size):
            line = []
            for col, data in enumerate(input().split()):
                line.append(data)
                if data == 'T':
                    self.tunnels.append([row, col])
            self.track.append(line)

    def start_racing(self):
        while not self.is_finish:
            command = input()
            if command == 'End':
                break
            self.car_data[0] = r, c = [
                self.car_data[0][0] + RallyRacing.__moves[command][0],
                self.car_data[0][1] + RallyRacing.__moves[command][1]
            ]

            symbol = self.track[r][c]
            self.__actions[symbol]()

    def tunnel(self):
        if self.tunnels[0] == self.car_data[0]:
            self.car_data[0] = self.tunnels[1]
        else:
            self.car_data[0] = self.tunnels[0]
        for i in self.tunnels:
            self.track[i[0]][i[1]] = '.'
        self.move(travel=30)

    def move(self, travel=10):
        self.car_data[1] += travel

    def finish(self):
        self.move()
        self.is_finish = True

    def prepare_result(self):
        self.track[self.car_data[0][0]][self.car_data[0][1]] = 'C'
        if self.is_finish:
            self.result.append(f"Racing car {self.number_racing} finished the stage!")
        else:
            self.result.append(f"Racing car {self.number_racing} DNF.")
        self.result.append(f"Distance covered {self.car_data[1]} km.")
        self.result.extend([''.join(row) for row in self.track])

    def __str__(self):
        return '\n'.join(self.result)


size = int(input())
racing_number = input()

rally = RallyRacing(size, racing_number)
print(rally)

#################################### TASK CONDITION ############################
'''
                               2. Rally Racing

It's time for one of the biggest races in the world, Paris-Dakar. The organizers 
of the event want you to do a program that helps them track the cars through the 
separate stages in the event.
On the first line, you will be given an integer N, which represents the size of a 
square matrix. On the second line you will receive the racing number of the tracked 
race car. On the next N lines you will be given the rows of  the matrix 
(string sequences, separated by whitespace), which will be representing the race route. 
The tracked race car always starts with coordinates [0, 0]. Thеre will be a tunnel 
somewhere across the race route. If the race car runs into the tunnel , the car goes 
through it and exits at the other end. There will be always two positions marked with 
"T"(tunnel). The finish line will be marked with "F". All other positions will be marked 
with "." . Keep track of the kilometers passed. Every time the race car receives a 
direction and moves to the next position of the race route, it covers 10 kilometers. 
If the car goes through the tunnel, it covers NOT 10, but 30 kilometers. On each line, 
after the matrix is given, you will be receiving the directions for the race car.
•	left
•	right
•	up
•	down
The race car starts moving across the race route:
•	If you receive "End" command, before the race car manages to reach the finish line,
 the car is disqualified and the following output should be printed on the Console: 
 "Racing car {racing number} DNF."
•	If the race car comes across a position marked with ".". The car passes 10 kilometers 
for the current move and waits for the next direction.
•	If the race car comes across a position marked with "T" this is the tunnel. The race
 car goes through it and moves to the other position marked with  "T" (the other end of the
  tunnel). The car passes 30 kilometers for the current move. The tunnel stays behind the car,
   so the race route is clear, and both the positions marked with "T", should be marked with ".".
•	If the car reaches the finish line - "F" position, the race is over. The tracked 
race car manages to finish the stage and the following output should be printed on the Console:
 "Racing car {racing number} finished the stage!". Don’t forget that the car has covered
  another 10 km with the last move.
Input
•	On the first line you will receive N - the size of the square matrix (race route)
•	On the second line you will receive the racing number of the tracked car
•	On the next N lines, you will receive the race route (elements will be separated by a space).
•	On the following lines, you will receive directions (left, right, up, down).
•	On the last line, you will receive the command "End".
Output
•	If the racing car has reached the finish line before the "End" command is given,
 print on the Console: "Racing car {racing number} finished the stage!"
•	If the "End"  command is given and the racing car has not reached the finish line yet, 
the race ends and the following message is printed on the Console: "Racing car {racing number} DNF."
•	On the second line, print the distance that the tracked race car has covered: 
"Distance covered {kilometers passed} km." 
•	At the end, mark the last known position of the race car with "C" and print the final 
state of the matrix (race route). The row elements in the output matrix should NOT be separated 
by a whitespace.
Constraints
•	The directions will always lead to coordinates in the matrix.
•	There will always be two positions marked with "T" , representing the tunnel in the race route.
•	The size of the square matrix (race route) will be between [4…10].

_______________________________________________
Example_01

Input
. . . . .
. . . T .
. . . . .
. T . . .
. . F . .
down
right
right
right
down
right
up
down
right
up
End	

Output
Racing car 01 finished the stage!
Distance covered 80 km.
.....
.....
.....
.....
..C..	

Explanation
The race car starts moving from position[0,0].The first command is down, so the moving 
direction is down. The race car is in position[1,0]. Next three commands are right, so 
the race car  comes across the tunnel – "T". The current car position is [1,3]. Swap the 
"T" with "." The race car goes through the tunnel, so its next position is [3,1]. Swap the 
"T" with "." Next direction is down, so the race car position is [4,1]. Next direction is
right, so the race car position is [4,2]. The race car reaches the finish line before the 
"End" command. So it manages to finish the stage. The remaining directions will be ignored 
and no more moves are going to be executed.


_______________________________________________
Example_02

Input
10
45
. . . . . . . . . . 
. . T . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . F . . .
. . . . . . . . . .
. . . . . . . . . . 
. . . . . . . T . .
right
down
down
right
up
left
up
up
End	

Output
Racing car 45 DNF.
Distance covered 100 km.
..........
..........
..........
..........
..........
..........
......F...
......C...
..........
..........	

'''