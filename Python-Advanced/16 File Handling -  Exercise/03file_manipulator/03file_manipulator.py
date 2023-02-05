import os


class CreateFile:

    def __init__(self, *data):
        self.file_name = data[0]

    def action(self):
        file = open(f'{self.file_name}', 'w')
        file.close()

        return True


class AddContent:

    def __init__(self, *data):
        self.file_name = data[0]
        self.content = data[1]

    def action(self):
        with open(f'{self.file_name}', 'a') as file:
            file.write(f'{self.content}\n')

        return True


class ReplaceContent:

    def __init__(self, *data):
        self.file_name = data[0]
        self.old_string = data[1]
        self.new_string = data[2]

    def action(self):
        try:
            file = open(f'{self.file_name}', 'r')
            text = file.readlines()

            for i in range(len(text)):
                text[i] = text[i].replace(self.old_string, self.new_string)

            file = open(f'{self.file_name}', 'w')
            file.write(''.join(text))
            file.close()

            return True

        except FileNotFoundError:
            return False


class DeleteFile:

    def __init__(self, *data):
        self.file_name = data[0]

    def action(self):
        try:
            os.remove(f'{self.file_name}')
            return True

        except FileNotFoundError:
            return False


class FileManipulator:

    def __init__(self, *data):
        self.command = data[0]
        self.info = data[1:]
        self.actions = {
            'Create': CreateFile,
            'Add': AddContent,
            'Replace': ReplaceContent,
            'Delete': DeleteFile,
        }

    def process_input_commands(self):
        status = self.actions[self.command](*self.info).action()
        return status


while True:
    input_data = input().split('-')
    if input_data[0] == 'End':
        break

    file_object = FileManipulator(*input_data).process_input_commands()
    if not file_object:
        print("An error occurred!")
