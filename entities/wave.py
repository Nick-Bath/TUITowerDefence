from entities.enemy import Enemy
from enums.directions import Direction
import math

class Wave():
	"""Wave Class"""
	direction = Direction.RIGHT.value
	SPRITE_SIZE_HOR = 9
	SPRITE_SIZE_VER = 1
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

	def wave_movement(self, clock, map_design, enemies_spawned):
		i = 0
		take_damage = False
		for enemy in self.enemy_list:
			if math.sqrt(pow(enemy.position[1] - map_design.core.position[1], 2) + pow(enemy.position[0] - map_design.core.position[0], 2)) < map_design.core.hitbox:
				self.enemy_list.remove(enemy)
				take_damage = True
			if clock % 15 == 0 and i < enemies_spawned:
				if enemy.current_direction == Direction.RIGHT.value:
					for coord in map_design.map_coords_ver:
						if enemy.position[0] == coord[0] and enemy.position[1] == coord[1] - self.SPRITE_SIZE_HOR:
							enemy.current_direction = Direction.DOWN.value
				if enemy.current_direction == Direction.DOWN.value:
					for coord in map_design.map_coords_hor:
						if enemy.position[0] == coord[0] - 1 - self.SPRITE_SIZE_VER and enemy.position[1] == coord[1]:
							enemy.current_direction = Direction.RIGHT.value
				enemy.move(enemy.current_direction)
			i += 1
		return take_damage