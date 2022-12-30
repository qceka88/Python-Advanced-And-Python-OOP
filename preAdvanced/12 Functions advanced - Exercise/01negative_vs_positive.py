##################################### variant 01 #####################################
def negative_vs_positive(*args):
    sum_positive = 0
    sum_negative = 0
    for num in args:
        if num > 0:
            sum_positive += num
        else:
            sum_negative += num
    return sum_negative, sum_positive


numbers_line = list(map(int, input().split()))
negative_sum, positive_sum = negative_vs_positive(*numbers_line)

print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")

##################################### variant 02 #####################################
class NegativeVsPositive:

    def __init__(self, *args):
        self.numbers = args
        self.positive_sum = 0
        self.negative_sum = 0
        self.message = ''

    def negative_vs_positive(self):
        for num in self.numbers:
            if num > 0:
                self.positive_sum += num
            else:
                self.negative_sum += num

    def result(self):
        if abs(self.negative_sum) > self.positive_sum:
            self.message = "The negatives are stronger than the positives"
        else:
            self.message = "The positives are stronger than the negatives"

    def __repr__(self):
        return f'{self.negative_sum}\n{self.positive_sum}\n{self.message}'


list_of_numbers = list(map(int, input().split()))
output = NegativeVsPositive(*list_of_numbers)
output.negative_vs_positive()
output.result()
print(output)


#################################### TASK CONDITION ############################
'''
                            1.	Negative vs Positive
You will receive a sequence of numbers (integers) separated by a single space. 
Separate the negative numbers from the positive. Find the total sum of 
the negatives and positives, and print the following:
•	On the first line, print the sum of the negatives
•	On the second line, print the sum of the positives
•	On the third line:
o	If the absolute negative number is larger than the positive number:
	"The negatives are stronger than the positives"
o	If the positive number is larger than the absolute negative number:
	"The positives are stronger than the negatives"
Note: you will not receive any zeroes in the input.

_______________________________________________
Example_01

Input
1 2 -3 -4 65 -98 12 57 -84	

Output
-189
137
The negatives are stronger than the positives

_______________________________________________
Example_02

Input
1 2 3	

Output
0
6
The positives are stronger than the negatives

'''
