from project.player import Player


class Team:

    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player_obj: Player):
        if player_obj in self.__players:
            return f"Player {player_obj.name} has already joined"

        self.__players.append(player_obj)

        return f"Player {player_obj.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        try:
            player = next(filter(lambda p: p.name == player_name, self.__players))
            self.__players.remove(player)

            return player

        except StopIteration:

            return f"Player {player_name} not found"
