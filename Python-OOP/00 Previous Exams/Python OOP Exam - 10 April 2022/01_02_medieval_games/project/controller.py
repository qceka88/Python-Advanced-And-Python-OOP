from project.player import Player
from project.supply.supply import Supply


class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players: Player):
        added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies: Supply):
        [self.supplies.append(s) for s in supplies]

    def sustain(self, player_name: str, sustenance_type: str):
        player = [p for p in self.players if p.name == player_name]
        if player and sustenance_type in ["Food", "Drink"]:
            if not player[0].need_sustenance:
                return f"{player_name} have enough stamina."

            supply_to_consume = None
            for idx in range(len(self.supplies) - 1, -1, -1):
                supply = self.supplies[idx]
                if supply.__class__.__name__ == sustenance_type:
                    supply_to_consume = self.supplies.pop(idx)
                    break
            else:
                raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

            if player[0].stamina + supply_to_consume.energy > 100:
                player[0].stamina = 100
            else:
                player[0].stamina += supply_to_consume.energy

            return f"{player_name} sustained successfully with {supply_to_consume.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player01 = [p for p in self.players if p.name == first_player_name][0]
        player02 = [p for p in self.players if p.name == second_player_name][0]

        if player01.stamina == 0 or player02.stamina == 0:
            message = []
            if player01.stamina == 0:
                message.append(f"Player {player01.name} does not have enough stamina.")

            if player02.stamina == 0:
                message.append(f"Player {player02.name} does not have enough stamina.")

            return '\n'.join(message)

        if player01.stamina < player02.stamina:
            if player02.stamina - (player01.stamina / 2) < 1:
                player02.stamina = 0
                return f"Winner: {player01.name}"
            else:
                player02.stamina -= (player01.stamina / 2)
            if player01.stamina - (player02.stamina / 2) < 1:
                player01.stamina = 0
                return f"Winner: {player02.name}"
            else:
                player01.stamina -= (player02.stamina / 2)
        elif player02.stamina < player01.stamina:
            if player01.stamina - (player02.stamina / 2) < 1:
                player01.stamina = 0
                return f"Winner: {player02.name}"
            else:
                player01.stamina -= (player02.stamina / 2)
            if player02.stamina - (player01.stamina / 2) < 1:
                player02.stamina = 0
                return f"Winner: {player01.name}"
            else:
                player02.stamina -= (player01.stamina / 2)

        if player01.stamina < player02.stamina:
            return f"Winner: {player02.name}"
        else:
            return f"Winner: {player01.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        players = "\n".join(str(p) for p in self.players)
        food = "\n".join(f.details() for f in self.supplies)
        return players + "\n" + food
