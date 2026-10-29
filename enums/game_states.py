from enum import Enum

class GameState(Enum):
    START = 2
    PAUSED = 3
    PLAYING = 1
    GAME_OVER = 4
    MAP_SELECTION = 5
    RESTART = 6
