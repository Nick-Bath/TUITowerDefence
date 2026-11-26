from entities.enemy import Enemy
from utilities.distance import distance
from entities.enemy_subclasses.bois.thickboi import ThickBoi
from entities.enemy_subclasses.bois.basicboi import BasicBoi
from entities.enemy_subclasses.bois.bossboi import BossBoi

CLOCK_RATE = 10

class Enemy_list():

	def __init__(self):
		self.enemies = []
		self.length = len(self.enemies)

	def fill(self, wave, map):
		enemies_to_spawn = wave.wave_calc()
		basicbois = enemies_to_spawn["basicbois"]
		thickbois = enemies_to_spawn["thickbois"]
		bossbois = enemies_to_spawn["bossbois"]

		if thickbois > 0:
			thickboi_rate = max(1, basicbois // thickbois)
		if bossbois > 0:
			bossboi_rate = max(1, basicbois // bossbois)

		for i in range(basicbois):
			self.enemies.append(BasicBoi(map, wave.audio))
			self.length += 1
			if thickbois > 1:
				if (i + 1) % thickboi_rate == 0:
					self.enemies.append(ThickBoi(map, wave.audio))
					thickbois -= 1
					self.length += 1
			elif thickbois == 1:
				if i == basicbois - 1:
					self.enemies.append(ThickBoi(map, wave.audio))
					self.length += 1
			if bossbois > 1:
				if (i + 1) % bossboi_rate == 0:
					self.enemies.append(BossBoi(map, wave.audio))
					thickbois -= 1
					self.length += 1
			elif bossbois == 1:
				if i == basicbois - 1:
					self.enemies.append(BossBoi(map, wave.audio))
					self.length += 1



	def move_enemies(self, clock, map, player):
		for baddie in self.enemies:
			if baddie.released and clock % (CLOCK_RATE/baddie.vel) == 0:
				baddie.move(map.enemy_route)
				if distance(baddie.position, map.core.position) < map.core.hitbox:
					self.remove_enemy(baddie)
					player.take_damage()

	def check_hp(self, player, towers, map, audio):
		for baddie in self.enemies:
			if baddie.hp <= 0:
				player.earn_money(baddie.level)
				try:
					baddie.death_trigger(self, map, audio)
				except AttributeError:
					pass
				self.remove_enemy(baddie)
				for tower in towers:
					tower.remove_target(baddie)

	def remove_enemy(self, enemy):
		self.enemies.remove(enemy)
		self.length -= 1