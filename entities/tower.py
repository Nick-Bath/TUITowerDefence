import math
from entities.projectile import Projectile
from utilities.distance import distance

class Tower:
	DEFAULT_SPRITE = "۩۩"
	"""Tower Class"""
	DEFAULT_DAMAGE = 10
	DEFAULT_RANGE = 20
	DEFAULT_COST = 10
	DEFAULT_MAX_TARGETS = 1
	DEFAULT_N_TARGETS = 0
	DEFAULT_FIRE_RATE = 20
	def __init__(self, position):
		self.__sprite = self.DEFAULT_SPRITE
		self.__position = position
		self.__damage = self.DEFAULT_DAMAGE
		self.__range = self.DEFAULT_RANGE
		self.__cost = self.DEFAULT_COST
		self.__targets = []
		self.__n_targets = self.DEFAULT_N_TARGETS
		self.__max_targets = self.DEFAULT_MAX_TARGETS
		self.__fire_rate = self.DEFAULT_FIRE_RATE

	@property
	def sprite(self):
		return self.__sprite

	@property
	def position(self):
		return self.__position

	@property
	def damage(self):
		return self.__damage

	@property
	def range(self):
		return self.__range
	
	@property
	def cost(self):
		return self.__cost

	@property
	def targets(self):
		return self.__targets

	@property
	def n_targets(self):
		return self.__n_targets

	@property
	def max_targets(self):
		return self.__max_targets

	@property
	def fire_rate(self):
		return self.__fire_rate

	def add_target(self, enemy):
		if self.__n_targets < self.__max_targets:
			self.__n_targets += 1
			self.__targets.append(enemy)


	def remove_target(self, enemy):
		if enemy in self.__targets:
			self.__targets.remove(enemy)
			self.__n_targets -= 1

	def prune_targets(self, enemy_list):
		# drop targets that were removed from the game by anything (death, reaching the core)
		for enemy in list(self.__targets):
			if enemy not in enemy_list:
				self.remove_target(enemy)

	def range_check(self, enemy):
		if distance(enemy.position, self.__position) < self.__range:
			if enemy not in self.__targets: 
				self.add_target(enemy)
		elif enemy in self.__targets:
				self.remove_target(enemy)

	def fire(self, clock):
		if clock % self.__fire_rate == 0:
			for enemy in self.__targets:
				enemy.add_projectile(self.__position, self.__damage)
			