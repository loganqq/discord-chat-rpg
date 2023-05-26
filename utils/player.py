import os
import json


class Player:
    def __init__(
        self,
        name: str = '',
        level: int = 1,
        hp: int = 100,
        mp: int = 20
    ) -> None:

        self.name: str = name
        self.level = level
        self.hp: int = hp
        self.mp: int = mp

    def write_player(self) -> None:
        """Updates the given player's json. Creates one upon player creation

        Returns:
            str: Status of the write.
        """

        subdirectory = 'players'
        file_name = os.path.join(subdirectory, f'{self.name}-{self.level}.json')

        player_dict = {
            "name": self.name,
            "level": self.level,
            "hp": self.hp,
            "mp": self.mp
        }

        with open(file_name, 'w') as file:
            json.dump(player_dict, file)


def get_players() -> list[Player]:
    result = []
    directory = 'players'

    for filename in os.listdir(directory):
        # print(filename)
        file = os.path.join(directory, filename)
        # print(file)

        with open(file, 'r') as f:
            player_dict = json.load(f)

            name = player_dict['name']
            level = player_dict['level']
            hp = player_dict['hp']
            mp = player_dict['mp']

            player = Player(name, level, hp, mp)

        result.append(player)

    return result


def list_players() -> str:
    result = '\nList of players:\n'
    players = get_players()

    for i, player in enumerate(players):
        result += (f'{i+1}. {player.name} - lvl {player.level}\n')

    return result


def player_list_is_empty() -> bool:

    path = 'C:\\Users\\lupea\\Documents\\Projects\\Discord\\discord-chat-rpg\\players'

    dir = os.listdir(path)

    if len(dir) == 0:
        return True
    else:
        return False
