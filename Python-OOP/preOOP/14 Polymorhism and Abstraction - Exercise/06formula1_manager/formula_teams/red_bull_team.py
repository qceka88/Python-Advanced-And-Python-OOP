from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    @property
    def sponsors(self):
        team_sponsors = {
            "Oracle":
                {1: 1_500_000,
                 2: 800_000},
            "Honda":
                {8: 20_000,
                 10: 10_000}
        }

        return team_sponsors

    @property
    def team_expenses(self):
        return -250_000
