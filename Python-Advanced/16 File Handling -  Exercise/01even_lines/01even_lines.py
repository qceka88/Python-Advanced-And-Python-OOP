class EvenLines:
    __symbols = ["-", ",", ".", "!", "?"]
    __modifier = '@'

    def __init__(self, input_file):
        self.input_file = input_file
        self.result = []

    def transform_text(self):
        def replace_symbols_in_row(row):
            for symbol in EvenLines.__symbols:
                row = row.replace(symbol, EvenLines.__modifier)
            return row

        def row_reverse(row):
            reversed_row = ' '.join(row.split()[::-1])
            return reversed_row

        with open(self.input_file, 'r') as data:
            for number, row in enumerate(data):
                if number % 2 == 0:
                    symbol_replace = replace_symbols_in_row(row)
                    reverse_row = row_reverse(symbol_replace)
                    self.result.append(reverse_row)

    def __repr__(self):
        return '\n'.join(self.result)


file = 'text.txt'
lines_object = EvenLines(file)
lines_object.transform_text()
print(lines_object)
