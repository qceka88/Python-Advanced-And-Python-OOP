class FileReader:

    def __init__(self, file):
        self.file = file
        self.sum = 0

    def read_the_file(self):
        with open(self.file, 'r') as data:
            for row in data:
                self.sum += int(row)

    def __repr__(self):
        return str(self.sum)


file = 'text.txt'
output = FileReader(file)
output.read_the_file()
print(output)
