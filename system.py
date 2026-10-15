
import curses
from enums.directions import Direction

class GameController:
    def __init__(self, window):
        self.window = window
        stdscr = curses.initscr()
        curses.noecho() # Turn off key echoing
        curses.cbreak() # Turn off buffered input
        curses.curs_set(0) # Set cursor visibility to off
        stdscr.keypad(True) # Turn on keypad mode
        self.window.nodelay(True) # doesn't delay when waiting for a key
        curses.use_default_colors() # removes background
        self.window.box()
        self.max_positions = stdscr.getmaxyx()

    
    def playerMovement(self, key) -> Direction:
        match key:
            case "KEY_UP":
                return Direction.UP.value
            case "KEY_DOWN":
                return Direction.DOWN.value
            case "KEY_LEFT":
                return Direction.LEFT.value
            case "KEY_RIGHT":
                return Direction.RIGHT.value
        
        """elif key == "s":
            enemy_list.append(Enemy("༼☉ɷ⊙༽", 0, int(maxy/2), 1))
            return enemy_list"""
        