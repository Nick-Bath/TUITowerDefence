from entities.enemy_subclasses.boi import Boi
from utilities.colours import YELLOW
from entities.enemy_subclasses.bois.basicboi import BasicBoi


class BossBoi(Boi):
	"""bossboi class, more hp, when dead spawns basicbois"""

	DEFAULT_SPRITE = "ᕦ༼ ✖෴✖ ༽ᕤ"
	DEFAULT_COLOR = YELLOW
	DEFAULT_VELOCITY = 0.5
	DEFAULT_HP = 400
	DEFAULT_LEVEL = 3
	DEFAULT_BASICBOIS = 5

	def death_trigger(self, enemy_list, map, audio):
		min_range = self._route_position - self.DEFAULT_BASICBOIS * 2
		if min_range < 0:
			min_range = 0
		max_range = self._route_position + self.DEFAULT_BASICBOIS * 2
		if max_range > len(self.route) - 1:
			max_range = len(self.route) - 1
		for route_position in range(min_range, max_range + 1,(max_range - min_range) // self.DEFAULT_BASICBOIS):
			enemy_list.enemies.append(BasicBoi(map, audio, released=True, route_position=route_position))
			enemy_list.length += 1

