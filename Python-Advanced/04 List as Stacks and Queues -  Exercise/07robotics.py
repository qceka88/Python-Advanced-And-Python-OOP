import time
from collections import deque


class Robotics:

    def __init__(self):
        self.robots = {}
        self.time = 0
        self.products = deque()
        self.log = []
        self.main_meth()

    def process_robots_data(self):
        for robot in input().split(';'):
            robot_name, robot_time = robot.split('-')
            if robot_name not in self.robots:
                self.robots[robot_name] = [int(robot_time), 0]

    def process_starting_time(self):
        h, m, s = input().split(':')
        self.time = int(h) * 3600 + int(m) * 60 + int(s)

    def take_product_to_production_line(self):
        while True:
            data = input()
            if data == 'End':
                break
            self.products.append(data)

    def convert_seconds_to_HH_MM_SS(self):
        value = time.strftime('%H:%M:%S', time.gmtime(self.time))
        return value

    def robot_process_the_product(self, free_robots, product):
        robot_name = list(free_robots)[0]
        self.robots[robot_name][1] = self.time + self.robots[robot_name][0]
        converted_time = self.convert_seconds_to_HH_MM_SS()
        self.log.append(f'{robot_name} - {product} [{converted_time}]')

    def check_for_free_robots(self):
        return {name: data for name, data in self.robots.items() if data[1] <= self.time}

    def robots_start_to_work(self):
        while self.products:
            product = self.products.popleft()
            self.time += 1
            free_robots = self.check_for_free_robots()
            if free_robots:
                self.robot_process_the_product(free_robots, product)
            else:
                self.products.append(product)

    def main_meth(self):
        self.process_robots_data()
        self.process_starting_time()
        self.take_product_to_production_line()
        self.robots_start_to_work()

    def __repr__(self):
        return '\n'.join(self.log)


if __name__ == '__main__':
    print(Robotics())


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