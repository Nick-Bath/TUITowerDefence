from entities.enemy import Enemy
from enums.directions import Direction
from functions.enemy_list import Enemy_list


class Wave():
	"""Wave Class"""
	direction = Direction.RIGHT.value
	SPRITE_SIZE_HOR = 9
	SPRITE_SIZE_VER = 1
	DEFAULT_ENEMIES_SPAWNED = 0
	DEFAULT_LEVEL = 1
	DEFAULT_WAVE = 0
	DEFAULT_DIFFICULTY = 1
	DEFAULT_WAVES_PER_LEVEL = 3
	DEFAULT_SPAWN_RATE = 100

	# sprite, spawn_pos, vel can eventually be enemy_type?
	def __init__(self, spawn_pos, audio):
		self.level = self.DEFAULT_LEVEL
		self.wave = self.DEFAULT_WAVE
		self.difficulty = self.DEFAULT_DIFFICULTY
		self.spawn_pos = spawn_pos
		self.audio = audio
		self.enemies_spawned = self.DEFAULT_ENEMIES_SPAWNED
		self.waves_per_level = self.DEFAULT_WAVES_PER_LEVEL
		self.spawn_rate = self.DEFAULT_SPAWN_RATE

	def wave_calc(self):
		enemies_to_spawn = {
			"normal_enemies": 0,
			"thickbois": 0
		}
		thickbois = self.level // 2
		enemies_to_spawn["normal_enemies"] = (self.level + self.wave) * self.difficulty
		if thickbois > 0:
			enemies_to_spawn["thickbois"] = thickbois
		return enemies_to_spawn


	def new_wave(self, enemy_list):
		if enemy_list.length == 0:
			self.enemies_spawned = 0
			self.wave += 1
			if self.wave > self.waves_per_level:
				self.wave = 1
				self.level += 1
			enemy_list.fill(self)
