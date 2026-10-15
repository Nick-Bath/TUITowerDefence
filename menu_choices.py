import sys
from enums.game_states import GameState
def menu_choice(selection):
    if selection == "Exit":
        sys.exit
    elif selection == "Restart":
        #Reset values
        #return GameState.Playing
        pass
    elif selection in ("Resume", "Start Game"):
        return GameState.PLAYING
    elif selection == "Save Game":
        pass
    elif selection == "Load Game":
        pass
    elif selection == "Save Score":
            pass
    