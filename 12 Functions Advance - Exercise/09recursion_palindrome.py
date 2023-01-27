class Palindrome:

    def __init__(self, *args):
        self.word = args[0]
        self.index = args[1]
        self.is_palindrome = None

    def main_meth(self):
        self.check_is_word_a_palindrome()
        return self.return_result()

    def check_is_word_a_palindrome(self):
        mid = len(self.word) // 2
        left = self.word[self.index]
        right = self.word[len(self.word) - self.index - 1]
        self.check_for_base(mid, left, right)

    def check_for_base(self, mid, left, right):
        self.index += 1
        if left != right:
            self.is_palindrome = False
        elif mid == self.index:
            self.is_palindrome = True
        else:
            return self.check_is_word_a_palindrome()

    def return_result(self):
        return f'{self.word} is a palindrome' if self.is_palindrome else f'{self.word} is not a palindrome'


def palindrome(*args):
    output = Palindrome(*args).main_meth()
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