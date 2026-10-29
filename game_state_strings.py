from enums.game_states import GameState
import maps.map_generator as map

def options(game_state):
    if game_state == GameState.START:
        return ["Start Game", "Select Map", "Load Game", "Exit"]
    elif game_state == GameState.PAUSED:
        return ["Resume", "Restart", "Save Game", "Load Game", "Exit"]
    elif game_state == GameState.MAP_SELECTION:
        return list(map.MAP_OPTIONS)
    else:
        return ["Restart", "Save Score", "Load Game", "Exit"]


def state(game_state):
    if game_state == GameState.START:
        return "TTUI TOWER DEF"
    elif game_state == GameState.PAUSED:
        return "PAUSED"
    elif game_state == GameState.MAP_SELECTION: 
        return "PICK MAP"
    else:
        return "GAME OVER"