from entities.enemy import Enemy
from utilities.distance import distance

class Enemy_list():

	def __init__(self):
		self.enemies = []
		self.length = len(self.enemies)

	def fill(self, wave):
		length = wave.wave_calc()
		for _ in range(0, length): # check for off by 1 error
			self.enemies.append(Enemy(wave.sprite, wave.spawn_pos, wave.enemy_vel, wave.audio))
		self.length = length
		return self.enemies


	def move_enemies(self, clock, current_wave, map, player):
		i = 0
		for baddie in self.enemies:
			if clock % 15 == 0 and i < current_wave.enemies_spawned:
				baddie.move()
				if distance(baddie.position, map.core.position) < map.core.hitbox:
					self.remove_enemy(baddie)
					player.take_damage()
			i += 1

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