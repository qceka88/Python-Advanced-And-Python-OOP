from project.formula_teams.red_bull_team import RedBullTeam
from project.formula_teams.mercedes_team import MercedesTeam


class F1SeasonApp:

    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
            return f"{team_name} has joined the new F1 season."

        if team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)
            return f"{team_name} has joined the new F1 season."

        raise ValueError("Invalid team name!")

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):

        if not any([self.red_bull_team, self.mercedes_team]):
            raise Exception("Not all teams have registered for the season.")

        red_bull = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)
        ahead = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"

        message = f"Red Bull: {red_bull}. Mercedes: {mercedes}. {ahead} is ahead at the {race_name} race."

        return message
