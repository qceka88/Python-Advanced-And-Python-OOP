##################################### variant 01 #####################################

def words_sorting(*args):
    words_and_values = {}
    for word in args:
        sum_of_letters = sum(map(ord, list(word)))
        words_and_values[word] = sum_of_letters
    sorted_result = {}
    sum_of_values = sum(words_and_values.values())
    if sum_of_values % 2 != 0:
        sorted_result = dict(sorted(words_and_values.items(), key=lambda x: -x[1]))
    else:
        sorted_result = dict(sorted(words_and_values.items(), key=lambda x: x[0]))
    return '\n'.join(f"{key} - {value}" for key, value in sorted_result.items())


# Part below is part from automatic judge system from SoftUni
print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))

print(
    words_sorting(
        'cacophony',
        'accolade'
    ))


##################################### variant 02 #####################################

class WordSorting:

    def __init__(self, *args):
        self.words = args
        self.words_and_values = {}
        self.sorted_result = {}

    def calculate_values_of_words(self):
        for word in self.words:
            sum_of_letters = sum(map(ord, list(word)))
            self.words_and_values[word] = sum_of_letters

    def sort_words(self):
        sum_of_values = sum(self.words_and_values.values())
        if sum_of_values % 2 != 0:
            self.sorted_result = dict(sorted(self.words_and_values.items(), key=lambda x: -x[1]))
        else:
            self.sorted_result = dict(sorted(self.words_and_values.items(), key=lambda x: x[0]))

    def __repr__(self):
        return '\n'.join(f"{key} - {value}" for key, value in self.sorted_result.items())


def words_sorting(*args):
    output = WordSorting(*args)
    output.calculate_values_of_words()
    output.sort_words()
    return f'{output}'


# Part below is part from automatic judge system from SoftUni
print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))

print(
    words_sorting(
        'cacophony',
        'accolade'
    ))

#################################### TASK CONDITION ############################
'''
                   03. Words Sorting
Write a function words_sorting which receives a different number of words.
Create a dictionary, which will have as keys the words that the function received. 
For each key, create a value that is the sum of all ASCII values of that key.
Then, sort the dictionary:
•	By values in descending order, if the sum of all values of the dictionary is odd
•	By keys in ascending order, if the sum of all values of the dictionary is even
Note: Submit only the function in the judge system
Input
•	There will be no input, just any number of words passed to your function
Output
•	The function should return a string in the format "{key} - {value}" for each key and value on a separate lines
Constraints:
•	There will be no case with capital letters.
•	There will be no case with a string consisting of other than letters.
_______________________________________________
Example_01

Test Code	(no input data in this task)
print(
    words_sorting(
        'escape', 
        'charm', 
        'mythology'
  ))
  
Output
charm - 523
escape - 625
mythology - 1004

Explanation
All of the ascii values of the 'escape' word are:
e = 101, s = 115, c = 99, a = 97, p = 112, e = 101
Their sum is 625.
We add it in the dictionary {'escape': 625}.
The ascii values of the 'charm' are:
c = 99, h = 104, a = 97, r = 117, m = 109
Their sum is 523.
We add it in the dictionary {'escape': 625, 'charm': 625}
The ascii values of the 'mythology' word are:
m = 109, y = 121, t = 116, h = 104, o = 111, l = 108, o = 111, g = 103, y = 121.
Their sum is 1004.
We add it in the dictionary
{'escape': 625, 'charm': 523, 'mythology': 1004}
When we sum 625 + 523 + 1004 = 2152. The result is even, and we 
sort the dictionary by keys in ascending order.
_______________________________________________
Example_02

Test Code	(no input data in this task)
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

Output  
escape - 625
charm - 523
eye - 323	
_______________________________________________
Example_03

Test Code	(no input data in this task)
print(
    words_sorting(
        'cacophony',         
        'accolade'
  ))	

Output  
accolade - 812
cacophony - 964	

'''
