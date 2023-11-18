from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    @staticmethod
    def get_sponsors_and_expenses():
        sponsors = {'Oracle': {1: 1_500_000, 2: 800_000},
                    'Honda': {8: 20_000, 10: 10_000}}
        expenses = 250_000

        return sponsors, expenses
