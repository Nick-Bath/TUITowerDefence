from entities.enemy import Enemy
from utilities.colours import BLUE
import curses

class ThickBoi(Enemy):
	"""thickboi class, more hp, slower"""

	DEFAULT_SPRITE = "╭༼ ◉෴◉ ༽ƪ╮"
	DEFAULT_COLOR = BLUE
	DEFAULT_VELOCITY = 0.5
	DEFAULT_HP = 200
	DEFAULT_LEVEL = 2