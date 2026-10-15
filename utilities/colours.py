import curses

RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, BLACK = range(1, 9)


def init_colours():
    curses.use_default_colors() # removes background
    curses.init_pair(RED, curses.COLOR_RED, -1)
    curses.init_pair(GREEN, curses.COLOR_GREEN, -1)
    curses.init_pair(YELLOW, curses.COLOR_YELLOW, -1)
    curses.init_pair(BLUE, curses.COLOR_BLUE, -1)
    curses.init_pair(MAGENTA, curses.COLOR_MAGENTA, -1)
    curses.init_pair(CYAN, curses.COLOR_CYAN, -1)
    curses.init_pair(WHITE, curses.COLOR_WHITE, -1)
    curses.init_pair(BLACK, curses.COLOR_BLACK, -1)

# Import to file with: from utilities.colours import COLOURS, YOU, WANT
# Turn it on and off with "windowname".attron(curses.color_pair(RED)) and then "windowname".attroff(curses.color_pair(RED))
# Assign to a variable: style = curses.color_pair(RED) | curses.A_BOLD
# or if you just use it once window.addstr(1, x, "PAUSED", curses.color_pair(RED) | curses.A_BOLD)
# Or window.addstr(1, x, "Printed in the style", style)