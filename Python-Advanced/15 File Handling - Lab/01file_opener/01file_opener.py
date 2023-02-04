class FileOpener:

    def __init__(self, file):
        self.file = file

    def open_file(self):
        try:
            file = open(self.file, 'r')
            return 'File is found'
        except FileNotFoundError:
            return 'File not found'


file_to_open = 'text.txt'
open_object = FileOpener(file_to_open)
print(open_object.open_file())
