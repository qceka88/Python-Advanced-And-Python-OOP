class FileWriter:

    def __init__(self, file_name, content):
        self.file_name = file_name
        self.content = content

    def create_file_and_write_content_in_file(self):
        file_name = f'{self.file_name}.txt'

        with open(file_name, 'w') as file:
            file.write(self.content)


file_name = 'my_first_file'
content = 'I just created my first file!'

file_object = FileWriter(file_name, content)
file_object.create_file_and_write_content_in_file()
