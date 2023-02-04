class Words:

    def __init__(self, words):
        self.words = words
        self.words_to_find = []

    def define_words(self):
        with open(self.words, 'r') as data:
            self.words_to_find = data.read().split()


class InputRows:

    def __init__(self, some_rows):
        self.some_rows = some_rows
        self.single_string = ''

    def convert_input_file_as_single_string(self):
        with open(self.some_rows, 'r') as data:
            for row in data:
                self.single_string += f' {row[:-1]}'


class CountWords:

    def __init__(self, some_words, target_string):
        self.some_words = some_words
        self.target_string = target_string
        self.result = {}

    def find_occurrences(self):
        for word in self.some_words:
            count = self.target_string.count(word)
            self.result[word] = count

    def __repr__(self):
        message = [f'{w} - {c}' for w, c in sorted(self.result.items(), key=lambda x: -x[1])]
        return '\n'.join(message)


words_data = 'words.txt'
input_data = 'input.txt'

words_object = Words(words_data)
words_object.define_words()
input_object = InputRows(input_data)
input_object.convert_input_file_as_single_string()
count_object = CountWords(words_object.words_to_find, input_object.single_string)
count_object.find_occurrences()
print(count_object)
