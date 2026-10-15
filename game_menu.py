import curses
from game_state_strings import options, state
from utilities.colours import BLUE

def game_menu(stdscr, game_state):
	maxh, maxw = stdscr.getmaxyx()
	win_h, win_w = 10, 20
	win = curses.newwin(win_h, win_w, (maxh - win_h) // 2, (maxw - win_w) // 2)
	win.keypad(True)
	win.nodelay(False)
	style = curses.color_pair(BLUE) | curses.A_BOLD
	options_list = options(game_state)
	state_text = state(game_state)
	selected = 0
	
	while True:
		win.erase()
		win.attron(style)
		win.border("|","|","+","+","|","|","|","|")
		win.addstr(1, (win_w - len(state_text)) // 2, state_text)
		for option_n, option in enumerate(options_list):
			if option_n == selected:
				highlight = curses.A_REVERSE | curses.A_BOLD
			else:
				highlight = style
			win.addstr(3 + option_n, (win_w - len(option)) // 2, option, highlight)
		win.attroff(style)
		win.refresh
		

		key = win.getkey()
		if key == "KEY_UP":
			selected = (selected - 1) % len(options_list)
		elif key == "KEY_DOWN":
			selected = (selected + 1) % len(options_list)
		elif key == "\n":
			return options_list[selected]
		elif key in ("p", "\x1b"): # ESCAPE character
			return "Resume"
	
