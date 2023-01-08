##################################### variant 01 #####################################
jobs = list(map(int, input().split(', ')))
searched_index = int(input())
tasks = sorted(jobs)

total_cycles = 0
is_found = False
for task in tasks:

    for index, cycles in enumerate(jobs):
        if task == cycles and index == searched_index:
            total_cycles += cycles
            is_found = True
            break
        elif task == cycles and index != searched_index:
            jobs[index] = 'v'
            total_cycles += cycles
            break
    if is_found:
        break

print(total_cycles)
##################################### variant 02 #####################################
class CPU:

    def __init__(self, jobs, searched_index):
        self.jobs = jobs
        self.searched_index = searched_index
        self.total_cycles = 0
        self.is_found = False

    def calculate_computer_time(self):
        for task in sorted(jobs):
            for index, cycles in enumerate(self.jobs):
                if task == cycles and index == self.searched_index:
                    self.total_cycles += cycles
                    self.is_found = True
                    break
                elif task == cycles and index != self.searched_index:
                    self.jobs[index] = 'v'
                    self.total_cycles += cycles
                    break
            if self.is_found:
                break

    def __repr__(self):
        return f'{self.total_cycles}'


jobs = list(map(int, input().split(', ')))
searched_index = int(input())

output = CPU(jobs, searched_index)
output.calculate_computer_time()
print(output)


#################################### TASK CONDITION ############################
'''
                01Scheduling
 
You are hired to create a program that implements SJF (Shortest Job First).
 It works by letting the shortest jobs to take the CPU, so jobs won't get frozen.
On the first line you will be given the jobs as integers (clock-cycles needed to finish the job) 
separated by comma and space ", ". On the second line you will be given the index of the job that 
we are interested in and want to know how many cycles will pass until the job is done.
The tasks that need the least amount of clock-cycles will be completed first. 
For the jobs that need the same amount of clock-cycles, the order is FIFO (First In First Out).
You have to print how many clock-cycles will pass until the task you are interested in is completed. 
For more clarifications, see the examples below.
Input
•	On the first line you will receive numbers separated by ", "
•	On the second line you will receive the index of the task you are interested in
Output
•	Single line: the clock-cycles that will pass until the task you are interested in is finished

_______________________________________________
Example_01

Input
3, 1, 10, 1, 2
0

Output
7

Explanation
The first task will be 1 at index 1 (1 clock-cycle)
Next is 1 at index 3 (total 2 clock-cycles)
Next is 2 at index 4 (total 4 clock-cycles)
Next, we arrive at 3 on index 0 (total 7 clock-cycles) which is the one we need, and we end the program

_______________________________________________
Example_02

Input
4, 10, 10, 6, 2, 99
2

Output
32	

Explanation
2 at index 4 -> total 2 clock-cycles
4 at index 0 -> total 6 clock-cycles
6 at index 3 -> total 12 clock-cycles
10 at index 1 -> total 22 clock-cycles
10 at index 2 -> total 32 clock-cycles

'''
