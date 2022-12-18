##################################### variant 01 #####################################

from collections import deque

number_of_pumps = int(input())
stations = deque([input().split() for _ in range(number_of_pumps)])

founded_index = False

for index in range(len(stations)):
    fuel_tank = 0
    for i, data in enumerate(stations):
        petrol, distance = int(data[0]), int(data[1])
        fuel_tank += petrol
        if fuel_tank - distance >= 0:
            fuel_tank -= distance
            if i == len(stations) - 1:
                founded_index = True
        else:
            break
    if founded_index:
        print(index)
        break
    # Can be also stations.rotate(-1)
    stations.append(stations.popleft())

##################################### variant 02 #####################################

from collections import deque


class Journey:

    def __init__(self, some_stations):
        self.some_stations = some_stations

    def check_journey(self):
        fuel_tank = 0
        for i, data in enumerate(self.some_stations):
            petrol, distance = int(data[0]), int(data[1])
            fuel_tank += petrol
            if fuel_tank - distance >= 0:
                fuel_tank -= distance
                if i == len(stations) - 1:
                    return True
            else:
                return False


class Index:

    def __init__(self, some_stations):
        self.some_stations = some_stations
        self.smallest_index = 0

    def action(self):
        for index in range(len(self.some_stations)):
            check = Journey(self.some_stations).check_journey()

            if check:
                self.smallest_index = index
                break
            # Can be also stations.rotate(-1)
            self.some_stations.append(self.some_stations.popleft())

    def __repr__(self):
        return f"{self.smallest_index}"


number_of_pumps = int(input())
stations = deque([input().split() for _ in range(number_of_pumps)])

output = Index(stations)
output.action()
print(output)

#################################### TASK CONDITION ############################
"""
                     5. Truck Tour
There is a circle road with N petrol pumps. The petrol pumps are numbered 
0 to (N−1) (both inclusive). For each petrol pump, you will receive two 
pieces of information (separated by a single space): 
-	The amount of petrol the petrol pump will give you
-	The distance from that petrol pump to the next petrol pump (kilometers)
You are a truck driver, and you want to go all around the circle. You know 
that the truck consumes 1 liter of petrol per 1 kilometer, and its tank has 
infinite petrol capacity. In the beginning, the tank is empty, but you start
your journey at a petrol pump so you can fill it with the given amount of petrol.
Your task is to calculate the first petrol pump from where the truck will be 
able to complete the circle. You never miss filling its tank at a petrol pump.
Input
•	On the first line, you will receive the number of petrol pumps - N
•	On the next N lines, you will receive the amount of petrol that each 
petrol pump will give and the distance between that petrol pump and the 
next petrol pump, separated by a single space
Output
•	An integer which will be the smallest index of a petrol pump from 
which you can start the tour
Constraints
•	1 ≤ N ≤ 1000001
•	1 ≤ amount of petrol, distance ≤ 1000000000
•	You will always have at least one point from where the truck will 
be able to complete the circle

____________________________________________________________________________________________
Example_01

Input
3
1 5
10 3
3 4	

Output
1


____________________________________________________________________________________________
Example_02

Input
5
22 5
14 10
52 7
21 12
36 9	

Output
0

"""