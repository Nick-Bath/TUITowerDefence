from entities.enemy import Enemy

class Wave():
	"""Wave Class"""
	# sprite, spawn_pos, vel can eventually be enemy_type?
	def __init__(self, level, wave, difficulty, sprite, spawn_pos, enemy_vel):
		self.level = level
		self.wave = wave
		self.difficulty = difficulty
		self.sprite = sprite
		self.spawn_pos = spawn_pos
		self.enemy_vel = enemy_vel
		self.enemy_list = self.create_enemy_list()
		self.enemy_count = len(self.enemy_list)

	def wave_calc(self):
		return (self.level + self.wave) * self.difficulty

	def create_enemy_list(self):
		self.enemylist = []
		for _ in range(0, self.wave_calc()): # check for off by 1 error
			self.enemylist.append(Enemy(self.sprite, self.spawn_pos, self.enemy_vel))
		return self.enemylist

	def wave_movement(self, system, clock, enemies_spawned, enemy_direction):
		i = 0
		take_damage = False
		for enemy in self.enemy_list:
			if enemy.position[1] == system.max_positions[1] - 8:
				self.enemy_list.remove(enemy)
				take_damage = True
			if clock % 15 == 0 and i < enemies_spawned:
				enemy.move(enemy_direction)
			i += 1
		return take_damage