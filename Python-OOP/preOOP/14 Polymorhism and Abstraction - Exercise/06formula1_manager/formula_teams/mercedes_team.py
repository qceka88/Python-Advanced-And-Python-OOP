from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    @property
    def sponsors(self):
        team_sponsors = {
            "Petronas":
                {1: 1_000_000,
                 3: 500_000},
            "TeamViewer":
                {5: 100_000,
                 7: 50_000}
        }

        return team_sponsors

    @property
    def team_expenses(self):
        return -200_000
