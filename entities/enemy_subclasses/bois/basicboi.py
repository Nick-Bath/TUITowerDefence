from entities.enemy_subclasses.boi import Boi
from utilities.colours import RED


class BasicBoi(Boi):
	"""basicboi class, standard boi"""

	DEFAULT_SPRITE = "╭༼☉ɷ⊙༽╭"
	DEFAULT_COLOR = RED
	DEFAULT_VELOCITY = 1
	DEFAULT_HP = 100
	DEFAULT_LEVEL = 1