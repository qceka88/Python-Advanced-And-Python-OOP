##################################### variant 01 #####################################

from collections import deque

input_robots = deque(input().split(';'))
hours, minutes, seconds = input().split(':')
starting_time = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)
products = deque()

while True:
    command = input()
    if command == 'End':
        break
    products.append(command)

runtime_robots = {}
robots_data = {}

for i in range(len(input_robots)):
    model, time = (input_robots.popleft()).split('-')
    robots_data[model] = 0
    runtime_robots[model] = int(time)

runtime = starting_time
while products:
    current_product = products.popleft()
    runtime += 1
    for model, time in robots_data.items():
        if runtime >= time:
            current_time = runtime % (24 * 60 * 60)
            hh = current_time // 3600
            mm = ((current_time % 3600) // 60)
            ss = ((current_time % 3600) % 60)
            print(f"{model} - {current_product} [{hh:02d}:{mm:02d}:{ss:02d}]")
            robots_data[model] = runtime_robots[model] + runtime
            break

    else:
        products.append(current_product)

##################################### variant 02 #####################################

from collections import deque


class Main:

    def __init__(self, some_robots, some_time):
        self.some_robots = some_robots
        self.some_time = some_time
        self.products = deque()
        self.runtime_robots = {}
        self.robots_data = {}
        self.log = ''

    def fill_product_list(self):
        while True:
            command = input()
            if command == 'End':
                break
            self.products.append(command)

    def fill_robots_data(self):
        for _ in range(len(self.some_robots)):
            model, time = (self.some_robots.popleft()).split('-')
            self.robots_data[model] = 0
            self.runtime_robots[model] = int(time)

    def processing_products(self):
        runtime = (int(self.some_time[0]) * 3600) + (int(self.some_time[1]) * 60) + int(self.some_time[2])
        while self.products:
            current_product = self.products.popleft()
            runtime += 1
            for model, time in self.robots_data.items():
                if runtime >= time:
                    current_time = runtime % (24 * 60 * 60)
                    hh = current_time // 3600
                    mm = ((current_time % 3600) // 60)
                    ss = ((current_time % 3600) % 60)
                    self.log += f"{model} - {current_product} [{hh:02d}:{mm:02d}:{ss:02d}]\n"
                    self.robots_data[model] = self.runtime_robots[model] + runtime
                    break

            else:
                self.products.append(current_product)

    def __repr__(self):
        return self.log


input_robots = deque(input().split(';'))
input_time = input().split(':')
output = Main(input_robots, input_time)
output.fill_product_list()
output.fill_robots_data()
output.processing_products()
print(output)


#################################### TASK CONDITION ############################
"""
                             7.	*Robotics
There is a robotics factory. The current project is assembly-line robots.
Each robot has a processing time – it is the time in seconds the robot needs 
to process a product. When a robot is free, it should take a product for 
processing and log its name, product, and processing start time.
Each robot processes a product coming from the assembly line. A product is 
coming from the line each second (so the first product should appear 
at [start time + 1 second]). If a product passes the line and there is not 
a free robot to take it, it should be queued at the end of the line again.
The robots are standing in the line in the order of their appearance.
Input
•	On the first line, you will receive the robots' names and their processing 
times in the format "robotName-processTime;robotName-processTime;robotName-processTime..."
•	On the second line, you will get the starting time in the format "hh:mm:ss"
•	Next, until the "End" command, you will get a product on each line.
Output 
•	Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"

____________________________________________________________________________________________
Example_01

Input
ROB-15;SS2-10;NX8000-3
8:00:00
detail
glass
wood
apple
End	

Output
ROB - detail [08:00:01]
SS2 - glass [08:00:02]
NX8000 - wood [08:00:03]
NX8000 - apple [08:00:06]


____________________________________________________________________________________________
Example_02

Input
ROB-8
7:59:59
detail
glass
wood
sock
End	

Output
ROB - detail [08:00:00]
ROB - wood [08:00:08]
ROB - glass [08:00:16]
ROB - sock [08:00:24]

"""