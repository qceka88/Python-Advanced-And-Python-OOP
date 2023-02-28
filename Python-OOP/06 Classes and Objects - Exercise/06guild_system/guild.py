class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player_obj):
        if player_obj.guild != "Unaffiliated":

            if player_obj.guild == self.name:
                return f"Player {player_obj.name} is already in the guild."

            return f"Player {player_obj.name} is in another guild."

        player_obj.guild = self.name
        self.players.append(player_obj)
        return f"Welcome player {player_obj.name} to the guild {self.name}"

    def kick_player(self, player_name):
        try:
            player_obj = next(filter(lambda p: p.name == player_name, self.players))
            self.players.remove(player_obj)
            player_obj.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        except StopIteration:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players = '\n'.join(p.player_info() for p in self.players)
        message = f"Guild: {self.name}\n{players}"
        return message
