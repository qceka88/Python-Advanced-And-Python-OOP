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
    def team_expenses(self):
        ...

    def calculate_revenue_after_race(self, race_pos: int):
        earned_money = self.team_expenses
        for sponsor, data in self.sponsors.items():
            for position, money in data.items():
                if race_pos <= position:
                    earned_money += money
                    break

        self.budget += earned_money
        return f"The revenue after the race is {earned_money}$. Current budget {self.budget}$"
