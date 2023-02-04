from string import punctuation


class LineNumbers:

    def __init__(self, file):
        self.file = file
        self.result = []

    def count_symbols(self, row):
        letters, marks = 0, 0
        for symbol in row:
            if symbol in punctuation:
                marks += 1
            else:
                letters += 1
        return letters, marks

    def read_lines(self):
        with open(self.file, 'r') as data:
            for num, row in enumerate(data):
                letters, marks = self.count_symbols(row)

                message = f'Line {num + 1}: {row[:-1]} ({letters})({marks})\n'
                self.result.append(message)

    def write_output_file(self):
        with open('output.txt', 'a') as data:
            for row in self.result:
                data.write(row)


file_to_read = 'text.txt'
line_object = LineNumbers(file_to_read)
line_object.read_lines()
line_object.write_output_file()
