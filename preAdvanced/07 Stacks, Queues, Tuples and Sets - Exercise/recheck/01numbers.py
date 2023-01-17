class Numbers:

    def __init__(self):
        self.output_message = ''
        self.commands = {'Add': self.add_numbers,
                         'Remove': self.remove_numbers,
                         'Check': self.check_subset}
        self.rows = {'First': set(),
                     'Second': set()}
        self.main_meth()

    def main_meth(self):
        self.fill_rows_with_numbers()
        self.receive_commands()
        self.prepare_result()

    def fill_rows_with_numbers(self):
        for row in self.rows:
            self.rows[row] = set(int(n) for n in input().split())

    def receive_commands(self):
        number_of_commands = int(input())
        for _ in range(number_of_commands):
            act, *data = input().split()
            self.commands[act](*data)

    def add_numbers(self, *args):
        side = args[0]
        for number in args[1:]:
            self.rows[side].add(int(number))

    def remove_numbers(self, *args):
        side = args[0]
        for number in args[1:]:
            self.rows[side].discard(int(number))

    def check_subset(self, *args):
        if self.rows['First'].issubset(self.rows['Second']) or self.rows['Second'].issubset(self.rows['First']):
            self.output_message += 'True\n'
        else:
            self.output_message += 'False\n'

    def prepare_result(self):
        for row in self.rows:
            self.output_message += f'{", ".join(str(n) for n in self.rows[row])} \n'

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(Numbers())
