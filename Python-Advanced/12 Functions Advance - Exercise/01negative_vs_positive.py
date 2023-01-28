class NegativePositive:

    def __init__(self):
        self.output_message = ''
        self.positive = []
        self.negative = []

        self.main_meth()

    def main_meth(self):
        self.find_positive_and_negative_numbers()
        self.prepare_output_message()

    def find_positive_and_negative_numbers(self):
        [self.positive.append(int(n)) if n.isdigit() else self.negative.append(int(n)) for n in input().split()]

    def prepare_output_message(self):
        self.output_message = str(sum(self.negative)) + '\n' + str(sum(self.positive))
        if sum(self.positive) < abs(sum(self.negative)):
            self.output_message += '\nThe negatives are stronger than the positives'
        else:
            self.output_message += '\nThe positives are stronger than the negatives'

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(NegativePositive())



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
