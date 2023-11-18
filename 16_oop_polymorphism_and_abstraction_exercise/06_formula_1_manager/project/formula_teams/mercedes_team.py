from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    @staticmethod
    def get_sponsors_and_expenses():
        sponsors = {'Petronas': {1: 1_000_000, 3: 500_000},
                    'TeamViewer': {5: 100_000, 7: 50_000}}
        expenses = 200_000

        return sponsors, expenses
