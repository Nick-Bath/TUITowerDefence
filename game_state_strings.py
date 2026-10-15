from enums.game_states import GameState

def options(game_state):
    if game_state == GameState.START:
        return ["Start Game", "Load Game", "Exit"]
    elif game_state == GameState.PAUSED:
        return ["Resume", "Restart", "Save Game", "Load Game", "Exit"]
    else:
        return ["Restart", "Save Score", "Load Game", "Exit"]


def state(game_state):
    if game_state == GameState.START:
        return "TTUI TOWER DEF"
    elif game_state == GameState.PAUSED:
        return "PAUSED"
    else:
        return "GAME OVER"