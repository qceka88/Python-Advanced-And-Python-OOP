class LongestIntersection:

    def __init__(self):
        self.output_message = ''
        self.rows = int(input())
        self.longest_intersection = set()
        self.first_set = set()
        self.second_set = set()
        self.main_meth()

    def main_meth(self):
        self.process_input_data()
        self.prepare_output_message()

    def process_input_data(self):
        for _ in range(self.rows):
            data = input().split('-')
            self.fill_first_set_with_numbers(data[0])
            self.fill_second_set_with_numbers(data[1])
            self.update_the_longest_intersection()

    def fill_first_set_with_numbers(self, data):
        first_set = set()
        start, end = [int(x) for x in data.split(',')]
        for number in range(start, end + 1):
            first_set.add(number)
        self.first_set = first_set

    def fill_second_set_with_numbers(self, data):
        second_set = set()
        start, end = [int(x) for x in data.split(',')]
        for number in range(start, end + 1):
            second_set.add(number)
        self.second_set = second_set

    def update_the_longest_intersection(self):
        current_intersection = self.first_set & self.second_set
        if len(current_intersection) > len(self.longest_intersection):
            self.longest_intersection = current_intersection

    def prepare_output_message(self):
        length = len(self.longest_intersection)
        row_of_symbols = ', '.join(str(s) for s in self.longest_intersection)
        self.output_message = f'Longest intersection is [{row_of_symbols}] with length {length}'

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(LongestIntersection())


#################################### TASK CONDITION ############################
"""

                            5.	Longest Intersection
Write a program that finds the longest intersection. You will be given a 
number N. On each of the next N lines you will be given two ranges in the 
format: "{first_start},{first_end}-{second_start},{second_end}". You should 
find the intersection of these two ranges. The start and end numbers in the 
ranges are inclusive.  Finally, you should find the longest intersection of 
all N intersections, print the numbers that are included and its length in 
the format: "Longest intersection is [{longest_intersection_numbers}] with 
length {length_longest_intersection}" 
Note: in each range, there will always be an intersection. 
If there are two equal intersections, print the first one.

____________________________________________________________________________________________
Example_01

Input
3
0,3-1,2
2,10-3,5
6,15-3,10	

Output
Longest intersection is [6, 7, 8, 9, 10] with length 5	The intersection of [0-3] and [1-2] is [1-2] (length 2)

Explanation
The intersection of [2-10] and [3-5] is [3-5] (length 3)
The intersection of [6-15] and [3-10] is [6-10] (length 5) - which is the longest

____________________________________________________________________________________________
Example_02

Input
5
0,10-2,5
3,8-1,7
1,8-2,4
4,7-2,5
1,10-2,11

Explanation
Longest intersection is [2, 3, 4, 5, 6, 7, 8, 9, 10] with length 9	

"""
