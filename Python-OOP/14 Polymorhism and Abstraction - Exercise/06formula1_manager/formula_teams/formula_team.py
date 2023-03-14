from abc import ABC, abstractmethod


class FormulaTeam(ABC):

    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @property
    @abstractmethod
    def sponsors(self):
        ...

    @property
    @abstractmethod
    def expenses(self):
        ...

    def calculate_revenue_after_race(self, race_pos: int):
        profit = 0 - self.expenses

        for sponsor, contract in self.sponsors.items():
            for position, award in contract.items():
                if race_pos <= position:
                    profit += award
                    break

        self.budget += profit

        return f"The revenue after the race is {profit}$. Current budget {self.budget}$"
