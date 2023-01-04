##################################### variant 01 #####################################
from collections import deque

vowels = deque(input().split())
consonants = input().split()
searched_word = ["rose", "tulip", "lotus", "daffodil"]

founded_word = {}

success = False

while vowels and consonants and not success:
    vowel = vowels.popleft() if vowels else ''
    consonant = consonants.pop() if consonants else ''
    for word in searched_word:
        if word not in founded_word:
            founded_word[word] = [[]] * len(word)
        if vowel or consonant in word:
            for index, letter in enumerate(word):
                if vowel == letter:
                    founded_word[word][index] = vowel
                if consonant == letter:
                    founded_word[word][index] = consonant
        if word == f'{"".join(map(str, founded_word[word]))}':
            success = True
            break

if success:
    print(f'Word found: {word}')
else:
    print('Cannot find any word!')
if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(consonants)} ')
##################################### variant 01 #####################################
from collections import deque


class FlowerFinder:

    def __init__(self, vowels, consonants, words_to_find):
        self.vowels = vowels
        self.consonants = consonants
        self.words_to_find = words_to_find
        self.founded_word = {}
        self.is_found = False
        self.message = ''

    def create_pattern_for_search(self, some_word):
        self.founded_word[some_word] = [[]] * len(some_word)

    def fill_founded_word_dict(self, vowel, consonant, word):
        for index, letter in enumerate(word):
            if vowel == letter:
                self.founded_word[word][index] = vowel
            if consonant == letter:
                self.founded_word[word][index] = consonant

    def try_to_find_flower(self):
        while self.vowels and self.consonants and not self.is_found:
            vowel = self.vowels.popleft() if self.vowels else ''
            consonant = self.consonants.pop() if self.consonants else ''
            for word in self.words_to_find:
                if word not in self.founded_word:
                    self.create_pattern_for_search(word)
                if vowel or consonant in word:
                    self.fill_founded_word_dict(vowel, consonant, word)
                if word == f'{"".join(map(str, self.founded_word[word]))}':
                    self.message += f'Word found: {word}'
                    self.is_found = True
                    break

    def format_the_result(self):
        if not self.is_found:
            self.message += 'Cannot find any word!'
        if self.vowels:
            self.message += f'\nVowels left: {" ".join(self.vowels)}'
        if self.consonants:
            self.message += f'\nConsonants left: {" ".join(self.consonants)} '

    def __repr__(self):
        return self.message


vowels_que = deque(input().split())
consonants_stack = input().split()
words_for_match = ["rose", "tulip", "lotus", "daffodil"]

output = FlowerFinder(vowels_que, consonants_stack, words_for_match)
output.try_to_find_flower()
output.format_the_result()
print(output)

#################################### TASK CONDITION ############################
'''
                          01.	Flower Finder
You will be given two sequences of characters, representing vowels and consonants.
 Your task is to start checking if the following words could be found:
•	"rose"
•	"tulip"
•	"lotus"
•	"daffodil"
Start by taking the first character of the vowels collection and the last character
 from the consonants collection. Then check if these letters are present in one or 
 more of the given words. If a letter is present, that part of the word is considered 
 found. The word is gradually revealed with each letter found. Continue processing 
 the next couple of letters until you find one of the given words above.
A letter (vowels or consonants) could participate in more than one word or more 
than one time in a word, for example:
•	The letter "o" is present in "rose", "lotus", and "daffodil". 
•	The letter "l" is present in "tulip", "lotus", and "daffodil".
•	The letter "f" is present in the word "daffodil" twice.
The consonant and the vowel are always removed from the collection after trying to 
match them with the letters in the given words (whether successful or not). In the end, 
the program stops when a word is found, or there are no more vowels or consonants.
As a result, if you found a word, print it and the remaining letters in each collection 
in the format described below. Otherwise, print "Cannot find any word!" on the first line 
and the remaining letters in each sequence in the format described below.
Look at the provided examples for a better understanding of the problem.
Input
•	On the first line, you will receive vowels, separated by a single space (" ").
•	On the second line, you will receive consonants, separated by a single space (" ").
Output
•	On the first line:
o	If a word is found, print it in the format: "Word found: {word_found}"
o	Otherwise, print: "Cannot find any word!"
•	On the next lines, print the remaining letters in each collection (if there are any left):
o	"Vowels left: {vowel_one} {vowel_two} … {vowel_N}"
o	"Consonants left: {consonants_one} {consonants_two} … {consonants_N}"
Constraints
•	All letters will be lowercase.
•	The letter 'y' will always be a vowel.
•	The letter 'w' will always be a consonant.

_______________________________________________
Example_01

Input
o e a o e a i
p r s x r	

Output
Word found: rose
Vowels left: o e a i
Consonants left: p r

Example
Start by taking the first volew "o" and the last consonant "r". They are found in 
words "rose", "lotus", and "daffodil".
Then, take "e" and "x". They are found in thr word "rose".
Then, take "a" and "s". They are found in words "rose", "lotus", and "daffodil".
The word "rose" is found, so we print it. Then we print the remaining letters in each sequence.

_______________________________________________
Example_02

Input
a a a
x r l t p p

Output
Cannot find any word!
Consonants left: x r l

_______________________________________________
Example_03

Input
u a o i u y o e
p m t l

Output
Word found: tulip
Vowels left: u y o e

'''