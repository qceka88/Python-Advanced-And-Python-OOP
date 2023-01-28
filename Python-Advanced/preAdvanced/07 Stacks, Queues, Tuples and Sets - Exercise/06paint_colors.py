##################################### variant 01 #####################################
from collections import deque

main_colors = ['red', 'yellow', 'blue']
sub_colors = ['orange', 'purple', 'green']

text = deque(input().split())

colors_que = deque()
while text:
    if len(text) > 1:
        first, second = text.popleft(), text.pop()
        straight, reverse = first + second, second + first
        if straight in main_colors or straight in sub_colors:
            colors_que.append(straight)
        elif reverse in main_colors or reverse in sub_colors:
            colors_que.append(reverse)
        else:
            edited_first, edited_second = first[:-1], second[:-1]
            middle = len(text) // 2
            if edited_first:
                text.insert(middle, edited_first)
            if edited_second:
                text.insert(middle, edited_second)
    else:
        substring = text.popleft()
        if substring in main_colors or substring in sub_colors:
            colors_que.append(substring)

for i in range(len(colors_que)):
    color = colors_que.popleft()
    if color == 'orange':
        if ('red' and 'yellow') in colors_que:
            colors_que.append(color)
    elif color == 'purple':
        if ('red' and 'blue') in colors_que:
            colors_que.append(color)
    elif color == 'green':
        if ('blue' and 'yellow') in colors_que:
            colors_que.append(color)
    else:
        colors_que.append(color)

print(list(colors_que))
##################################### variant 02 #####################################
from collections import deque


class Main:
    def __init__(self, some_text):
        self.some_text = some_text
        self.main_colors = ['red', 'yellow', 'blue']
        self.sub_colors = ['orange', 'purple', 'green']
        self.colors_que = deque()

    def find_colors(self):
        while self.some_text:
            if len(self.some_text) > 1:
                first, second = self.some_text.popleft(), self.some_text.pop()
                straight, reverse = first + second, second + first
                if straight in self.main_colors or straight in self.sub_colors:
                    self.colors_que.append(straight)
                elif reverse in self.main_colors or reverse in self.sub_colors:
                    self.colors_que.append(reverse)
                else:
                    edited_first, edited_second = first[:-1], second[:-1]
                    middle = len(text) // 2
                    if edited_first:
                        self.some_text.insert(middle, edited_first)
                    if edited_second:
                        self.some_text.insert(middle, edited_second)
            else:
                substring = self.some_text.popleft()
                if substring in self.main_colors or substring in self.sub_colors:
                    self.colors_que.append(substring)

    def find_sub_colors_ingredients(self):
        for current_iteration in range(len(self.colors_que)):
            color = self.colors_que.popleft()
            if color == 'orange':
                if ('red' and 'yellow') in self.colors_que:
                    self.colors_que.append(color)
            elif color == 'purple':
                if ('red' and 'blue') in self.colors_que:
                    self.colors_que.append(color)
            elif color == 'green':
                if ('blue' and 'yellow') in self.colors_que:
                    self.colors_que.append(color)
            else:
                self.colors_que.append(color)

    def __repr__(self):
        return f'{list(self.colors_que)}'


text = deque(input().split())

output = Main(text)
output.find_colors()
output.find_sub_colors_ingredients()
print(output)


#################################### TASK CONDITION ############################
"""

                        6.	Paint Colors
You will have to find all possible color combinations that can be used.
Write a program that finds colors in a string. You will be given a string on a 
single line containing substrings (separated by a single space) from which 
you will be able to form the following colors: 
Main colors: "red", "yellow", "blue"
Secondary colors: "orange", "purple", "green"
To form a color, you should concatenate the first and the last substrings 
and check if you can get any of the above colors' names. If there is only
one substring left, you should use it to do the same check. You can only keep 
a secondary color if the two main colors needed for its creation could be 
formed from the given substrings:
•	orange = red + yellow
•	purple = red + blue
•	green = yellow + blue
Note: You could find some of the main colors needed to keep a secondary 
color after it is found. When you form a color, remove both substrings. 
Otherwise, you should remove the last character of each substring and return 
them in the middle of the original string. If the string contains an odd 
number of substrings, you should put the substrings one position ahead. For example,
if you are given the string "re yellow bye" you could not form a color with 
the substring "re" and "bye", so you should remove the last character and return 
them in the middle of the string: "r by yellow". In the end, print out the 
list with colors in the order in which they are found.
Input
•	Single line string
Output
•	The list with the collected colors
Constrains
•	You will not receive an empty string
•	Please consider only the colors mentioned above
•	There won't be any cases with repeating colors

____________________________________________________________________________________________
Example_01

Input
d yel blu e low redd	

Output
['yellow', 'blue', 'red']

Explanation
First, we take "d" and "redd". After combining those substrings, we don't get 
any of the needed colors, so we remove the last characters from both substrings 
and return them in the middle of the original string, and it becomes "yel blu red e low".
After that, we take "yel" and "low" so the first color we add to our list is 
yellow, and the string we are searching in looks as follows: "blu red e"
Then we take "blu" and "e", and since this color is one of the searched ones 
(blue), we add it to our collection, and the state of the string is now "red".
We should take the last substring and check if it matches some of the colors, 
and since it does, we add it (red) to our colors collection.
Finally, we print all the colors found: yellow, blue, and red in the format shown above.

____________________________________________________________________________________________
Example_02

Input
r ue nge ora bl ed	

Output
['red', 'blue']

Explanation
We don't keep orange because we don't have yellow in the final 
list with colors (combining red and yellow gives us orange).

____________________________________________________________________________________________
Example_03

Input
re ple blu pop e pur d	

Output
['red', 'purple', 'blue']


"""
