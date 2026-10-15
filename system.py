
import curses
from enums.directions import Direction

class GameController:
    def __init__(self, window):
        self.window = window

    def gameStart(self):
        stdscr = curses.initscr()
        curses.noecho() # Turn off key echoing
        curses.cbreak() # Turn off buffered input
        curses.curs_set(0) # Set cursor visibility to off
        stdscr.keypad(True) # Turn on keypad mode
        self.window.nodelay(True) # doesn't delay when waiting for a key
        curses.use_default_colors() # removes background
    
        self.window.box()

        maxy, maxx = stdscr.getmaxyx()
    
        return (maxy, maxx)

    
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
            

        

        



    def towerController(self, towers):
        try:
            key = self.window.getkey()
        except:
            key = none   
        if key == "b":
            if x > 20 and y > maxy/2 + 3 or y < maxy/2 - 3:
                towers.append(Tower("۩۩", x, y))
                return towers

        
        """elif key == "s":
            enemy_list.append(Enemy("༼☉ɷ⊙༽", 0, int(maxy/2), 1))
            return enemy_list"""
        