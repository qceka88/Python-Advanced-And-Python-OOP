import os


class DeleteFile:

    def __init__(self, file):
        self.file = file

    def remove_file(self):
        try:
            os.remove(self.file)
            return 'File removed successfully!'
        except FileNotFoundError:
            return 'File not found!'


file = 'text.txt'

delete_obj = DeleteFile(file)
print(delete_obj.remove_file())
