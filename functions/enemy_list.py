from entities.enemy import Enemy
from utilities.distance import distance
from entities.enemy_subclasses.thickboi import ThickBoi

CLOCK_RATE = 10

class Enemy_list():

	def __init__(self):
		self.enemies = []
		self.length = len(self.enemies)

	def fill(self, wave):
		enemies_to_spawn = wave.wave_calc()
		normal = enemies_to_spawn["normal_enemies"]
		thickbois = enemies_to_spawn["thickbois"]

		if thickbois > 0:
			thickboi_rate = max(1, normal // thickbois)

		for i in range(normal):
			self.enemies.append(Enemy(wave.spawn_pos, wave.audio))
			self.length += 1
			if thickbois > 1:
				if (i + 1) % thickboi_rate == 0:
					self.enemies.append(ThickBoi(wave.spawn_pos, wave.audio))
					thickbois -= 1
					self.length += 1
			elif thickbois == 1:
				if i == normal - 1:
					self.enemies.append(ThickBoi(wave.spawn_pos, wave.audio))
					self.length += 1


	def move_enemies(self, clock, current_wave, map, player):
		for baddie in self.enemies:
			if baddie.released and clock % (CLOCK_RATE/baddie.vel) == 0:
				baddie.move()
				if distance(baddie.position, map.core.position) < map.core.hitbox:
					self.remove_enemy(baddie)
					player.take_damage()

	def check_hp(self, player, towers):
		for baddie in self.enemies:
			if baddie.hp <= 0:
				player.earn_money(baddie.level)
				self.remove_enemy(baddie)
				for tower in towers:
					tower.remove_target(baddie)

	def remove_enemy(self, enemy):
		self.enemies.remove(enemy)
		self.length -= 1