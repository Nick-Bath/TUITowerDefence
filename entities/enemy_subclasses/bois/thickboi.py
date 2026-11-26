from entities.enemy_subclasses.boi import Boi
from utilities.colours import BLUE


class ThickBoi(Boi):
	"""thickboi class, more hp, slower"""

	DEFAULT_SPRITE = "╭༼ ◉෴◉ ༽ƪ╮"
	DEFAULT_COLOR = BLUE
	DEFAULT_VELOCITY = 0.5
	DEFAULT_HP = 200
	DEFAULT_LEVEL = 2