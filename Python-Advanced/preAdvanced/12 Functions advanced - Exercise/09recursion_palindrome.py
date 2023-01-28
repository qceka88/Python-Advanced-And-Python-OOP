##################################### variant 01 #####################################
def palindrome(word, index):
    if index > len(word) // 2:
        return f'{word} is a palindrome'
    left_part = word[index]
    right_part = word[-1 - index]
    if right_part != left_part:
        return f'{word} is not a palindrome'
    return palindrome(word, index + 1)


# Part below is part from automatic judge system from SoftUni
print(palindrome("abcba", 0))
print(palindrome("peter", 0))


##################################### variant 02 #####################################
class Palindrome:
    def __init__(self, text, index):
        self.text = text
        self.index = index

    def palindrome(self):
        if self.index > len(self.text) // 2:
            return f'{self.text} is a palindrome'
        left_part = self.text[self.index]
        right_part = self.text[-1 - self.index]
        if right_part != left_part:
            return f'{self.text} is not a palindrome'
        return palindrome(self.text, self.index + 1)


def palindrome(word, index):
    output = Palindrome(word, index).palindrome()
    return output


# Part below is part from automatic judge system from SoftUni
print(palindrome("abcba", 0))
print(palindrome("peter", 0))

#################################### TASK CONDITION ############################
'''
              9.	Recursion Palindrome
Write a recursive function called palindrome() that will receive a word and an 
index (always 0). Implement the function, so it returns "{word} is a palindrome" 
if the word is a palindrome and "{word} is not a palindrome" if the word is not 
a palindrome using recursion. Submit only the function in the judge system.

_______________________________________________
Example_01

Test Code	(no input data in this task)
print(palindrome("abcba", 0))	

Output
abcba is a palindrome

_______________________________________________
Example_02

Test Code	(no input data in this task)
print(palindrome("peter", 0))

Output
peter is not a palindrome



'''
