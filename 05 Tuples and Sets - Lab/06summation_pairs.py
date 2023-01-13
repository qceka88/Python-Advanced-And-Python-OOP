from collections import deque


class SummationsPairs:

    def __init__(self):
        self.sequence = deque(map(int, input().split()))
        self.target = int(input())
        self.message = ''
        self.main()

    def check_numbers_for_pairs(self):
        for _ in range(len(self.sequence)):
            first_number = self.sequence.popleft()
            for _ in range(len(self.sequence)):
                second_number = self.sequence.popleft()
                if first_number + second_number == self.target:
                    self.message += f'{first_number} + {second_number} = {self.target}\n'
                    break
                else:
                    self.sequence.append(second_number)
            else:
                self.sequence.append(first_number)

    def main(self):
        self.check_numbers_for_pairs()

    def __repr__(self):
        return self.message


if __name__ == '__main__':
    print(SummationsPairs())

#################################### TASK CONDITION ############################
"""
                    6.	Summation Pairs
The task is not included in the Judge system. On the first line, 
you will receive a sequence of numbers separated by space. On the 
second line, you'll receive a target number. Your task is to find 
the pairs of numbers whose sum equals the target number. For each 
found pair print "{number} + {number} = {target_number}". You may 
NOT use the same element twice to fulfill the condition above.
Can you come up with an algorithm that has less time complexity?

____________________________________________________________________________________________
Example_01

Input
1 5 4 2 2 3 1 3 2
4	

Output
1 + 3 = 4
1 + 3 = 4
2 + 2 = 4

____________________________________________________________________________________________
Example_02

Input
11 8 5 6 9 2 9 7 3 4
11 	

Output
8 + 3 = 11
5 + 6 = 11
9 + 2 = 11
7 + 4 = 11

"""