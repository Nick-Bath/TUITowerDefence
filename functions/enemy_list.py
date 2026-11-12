from entities.enemy import Enemy


class Enemy_list():
	def __init__(self):
		self.enemies = []
		self.length = 0

	def fill(self, wave):
		length = wave.wave_calc()
		for _ in range(0, length): # check for off by 1 error
			self.enemies.append(Enemy(wave.sprite, wave.spawn_pos, wave.enemy_vel, wave.audio))
		self.length = length
		return self.enemies