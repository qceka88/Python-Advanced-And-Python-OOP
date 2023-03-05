from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:

    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team, budget):
        if team == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)

        elif team == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)

        else:
            raise ValueError("Invalid team name!")

        return f"{team} has joined the new F1 season."

    def new_race_results(self, race_name, red_bull_pos, mercedes_pos):
        if not any([self.mercedes_team, self.red_bull_team]):
            raise Exception("Not all teams have registered for the season.")

        leadership = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"

        red_bull_result = self.red_bull_team.calculate_revenue_after_race(red_bull_pos),
        mercedes_result = self.mercedes_team.calculate_revenue_after_race(mercedes_pos),

        message = f"Red Bull: {red_bull_result[0]}. Mercedes: {mercedes_result[0]}. " \
                  f"{leadership} is ahead at the {race_name} race."

        return message
