import os


class DirectoryCollection:

    def __init__(self, dir):
        self.dir = dir
        self.collected_data = {}
        self.search_files_and_directories(self.dir)

    def search_files_and_directories(self, dir):
        for file_name in os.listdir(dir):
            file = os.path.join(dir, file_name)
            self.is_file_or_directory(file, file_name)

    def is_file_or_directory(self, file, file_name):
        if os.path.isfile(file):
            extension = file.split('.')[-1]
            if extension not in self.collected_data:
                self.collected_data[extension] = []
            self.collected_data[extension].append(file_name)

        elif os.path.isdir(file):
            self.search_files_and_directories(file)


class SortResult:

    def __init__(self, data):
        self.data = data
        self.sorted_result = []

    def sorting_collected_data(self):
        for ext, files in sorted(self.data.collected_data.items()):
            format_data = f".{ext}\n" + '\n'.join(f'- - - {file}' for file in sorted(files)) + '\n'
            self.sorted_result.append(format_data)


class CreateReportFile:

    def __init__(self, data):
        self.data = data

    def create_report_file(self):
        with open('report.txt', 'w') as file:
            file.write('\n'.join(self.data.sorted_result))


directory_input = input()
dir_object = DirectoryCollection(directory_input)
sort_result = SortResult(dir_object)
sort_result.sorting_collected_data()
report_object = CreateReportFile(sort_result)
report_object.create_report_file()
