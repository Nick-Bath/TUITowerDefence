WINDOW_MIN_SIZE = (50, 150)

def check_window_size(window):
	height, width = window.getmaxyx()

	if height < WINDOW_MIN_SIZE[0] or width < WINDOW_MIN_SIZE[1]:
		window.clear()
		window.box()

		RESIZE_TEXT = "Window too small. Please resize to at least 50x150"

		y = height // 2
		x = width // 2 - (len(RESIZE_TEXT) // 2)

		window.addstr(y, x, RESIZE_TEXT)
		window.addstr(0, 0, f"Height: {height}, Width: {width}")
		window.refresh()

		return False

	return True