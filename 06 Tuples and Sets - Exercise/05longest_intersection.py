##################################### variant 01 #####################################

lines = int(input())

longest_intersect = set()

for row in range(lines):
    data = input().split('-')
    first_start, first_end = tuple(map(int, data[0].split(',')))
    second_start, second_end = tuple(map(int, data[1].split(',')))
    first_set = {num for num in range(first_start, first_end + 1)}
    second_set = {num for num in range(second_start, second_end + 1)}
    intersect = first_set.intersection(second_set)
    if len(intersect) > len(longest_intersect):
        longest_intersect = intersect

print(f"Longest intersection is [{', '.join(str(n) for n in longest_intersect)}] with length {len(longest_intersect)}")


##################################### variant 02 #####################################
class First:

    def __init__(self, some_data):
        self.some_data = some_data
        self.first_set = set()

    def range(self):
        first_start, first_end = tuple(map(int, self.some_data[0].split(',')))
        self.first_set = {num for num in range(first_start, first_end + 1)}

    def return_tom_main(self):
        return self.first_set


class Second:

    def __init__(self, some_data):
        self.some_data = some_data
        self.second_set = set()

    def range(self):
        second_start, second_end = tuple(map(int, self.some_data[1].split(',')))
        self.second_set = {num for num in range(second_start, second_end + 1)}

    def return_tom_main(self):
        return self.second_set


class Intersect:

    def __init__(self, set_first, set_second):
        self.set_first = set_first
        self.set_second = set_second

    def intersecting_sets(self):
        return self.set_first.intersection(self.set_second)


class Main:

    def __init__(self, some_number):
        self.some_number = some_number
        self.longest_intersect = set()

    def read_data(self):
        for row in range(self.some_number):
            data = input().split('-')
            first_object = First(data)
            first_object.range()
            first_result = first_object.return_tom_main()
            second_object = Second(data)
            second_object.range()
            second_result = second_object.return_tom_main()
            intersect_object = Intersect(first_result, second_result).intersecting_sets()
            if len(intersect_object) > len(self.longest_intersect):
                self.longest_intersect = intersect_object

    def __repr__(self):
        return f"Longest intersection is [{', '.join(str(n) for n in self.longest_intersect)}] with length {len(self.longest_intersect)}"


input_lines = int(input())
output = Main(input_lines)
output.read_data()
print(output)

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
