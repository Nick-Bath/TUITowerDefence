import sys
from enums.game_states import GameState
import maps.map_generator as map
#from game_state_strings import options, state
from game_menu import game_menu
def menu_choice(stdscr, selection):
    if selection == "Exit":
        sys.exit()
    elif selection == "Restart":
        return GameState.RESTART
    elif selection in ("Resume", "Start Game"):
        return GameState.PLAYING
    elif selection == "Save Game":
        pass
    elif selection == "Load Game":
        pass
    elif selection == "Select Map":
        choice = game_menu(stdscr, GameState.MAP_SELECTION)
        map.MAP_CHOICE =  map.MAP_OPTIONS[choice]
    elif selection == "Save Score":
        pass
    return GameState.START    