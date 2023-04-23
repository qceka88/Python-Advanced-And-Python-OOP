from project.people.child import Child


class Room:

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children: [Child] = []
        self.expenses: float = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value: float):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        current_amount = 0
        for data in args:
            current_amount += data.get_monthly_expense()

        self.expenses = current_amount
