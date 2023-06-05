import os

from datetime import datetime
from utils.player import Player, get_players, list_players, player_list_is_empty
from utils.log import Logger

from dotenv import load_dotenv
load_dotenv(dotenv_path="C:\\Users\\lupea\\Documents\\Projects\\Discord\\discord-chat-rpg\\.env")

logger = Logger(os.environ.get('LOG_FILE'))


def create_player() -> Player:
    """Creates a new player.
    Takes input for the player name.

    Returns:
        Player: Returns the resulting player object.
    """

    today = datetime.now()
    time_occurred = today.strftime("%m/%d/%Y %H:%M:%S")

    def _get_name() -> str:
        """Gets user input for the name of the new player.

        Returns:
            str: Returns the name that the user inputs.
        """

        return input('Please enter a name: ')

    player = Player(_get_name())

    logger.log({
        'date': time_occurred,
        'message': 'Player created',
        'instance_key': player.name
    })

    player.write_player()

    return player


def select_player() -> Player:
    """Handles functionality to select an already created player.

    Returns:
        Player: Returns the selection.
    """

    print(list_players())

    players = get_players()

    choice = int(input('Enter the number of the player you wish to choose: '))

    return players[choice-1]


def options_menu(player: Player | None = None) -> None:
    """Prints out the options to the player. Players can choose to continue if they
    have a character, create one if not, or quit the game. 

    Args:
        player (Player | None, optional): Provides an exsisting player object if one has been created. Defaults to None.
    """

    print('############################')
    if not player_list_is_empty():
        print('# - Select Player -        #')
    else:
        player = Player()
    print('# - New Character -        #')
    print('# - Quit -                 #')
    print('############################')

    choice = input('Type your choice (select, new, quit): ')
    choice = choice.lower()

    if choice == 'select':
        player = select_player()
    elif choice == 'new':
        player = create_player()
    elif choice == 'quit':
        exit()
    else:
        print('Incorrect choice selected')

        if player:
            options_menu(player=player)
        else:
            options_menu()

    game(player=player)


def welcome_screen(player: Player | None = None) -> None:
    """Displays the welcome message upon script execution

    Args:
        player (Player | None, optional): Existing player object. Defaults to None if no player exists.
    """

    print('############################')
    print('#    Welcome to the RPG    #')
    if player:
        print(f'  Playing as: {player.name}')
    print('# Press ENTER to continue! #')
    print('############################')

    if input('') == '':
        if player:
            options_menu(player=player)
        else:
            options_menu()


def game(player: Player) -> None:
    """The main game loop

    Args:
        player (Player): The player object currently being used.
    """

    print(f'Beginning the game as: {player.name}')


if __name__ == '__main__':
    welcome_screen()
