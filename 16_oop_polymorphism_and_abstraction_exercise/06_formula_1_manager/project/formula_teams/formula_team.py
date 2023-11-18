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
            raise ValueError('F1 is an expensive sport, find more sponsors!')

        self.__budget = value

    @staticmethod
    @abstractmethod
    def get_sponsors_and_expenses():
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        sponsors, expenses = self.get_sponsors_and_expenses()
        revenue = 0

        for sponsor in sponsors.values():
            for place, reward in sponsor.items():
                if race_pos <= place:
                    revenue += reward
                    break

        revenue -= expenses
        self.budget += revenue

        return f'The revenue after the race is {revenue}$. Current budget {self.budget}$'
