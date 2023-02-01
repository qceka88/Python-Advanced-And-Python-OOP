from project.player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player_obj: Player):
        if player_obj.guild == self.name:
            return f"Player {player_obj.name} is already in the guild."
        elif player_obj.guild != "Unaffiliated":
            return f"Player {player_obj.name} is in another guild."
        else:
            player_obj.guild = self.name
            self.players.append(player_obj)
            return f"Welcome player {player_obj.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for data in self.players:
            if data.name == player_name and data.guild == self.name:
                data.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        message = f"Guild: {self.name}"
        players_info = '\n'.join(p.player_info() for p in self.players)
        return message + '\n' + players_info


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
# print(guild.kick_player('Hasan'))