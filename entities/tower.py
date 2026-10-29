import math

class Tower:
	DEFAULT_SPRITE = "۩۩"
	"""Tower Class"""
	DEFAULT_DAMAGE = 10
	DEFAULT_RANGE = 20
	DEFAULT_COST = 10
	DEFAULT_MAX_TARGETS = 1
	DEFAULT_N_TARGETS = 0
	def __init__(self, position):
		self.__sprite = self.DEFAULT_SPRITE
		self.__position = position
		self.__damage = self.DEFAULT_DAMAGE
		self.__range = self.DEFAULT_RANGE
		self.__cost = self.DEFAULT_COST
		self.__targets = []
		self.__n_targets = self.DEFAULT_N_TARGETS
		self.__max_targets = self.DEFAULT_MAX_TARGETS

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

	def add_target(self, enemy):
		if self.__n_targets < self.__max_targets:
			self.__n_targets += 1
			self.__targets.append(enemy)
			return True
		return False

	def remove_target(self, enemy):
		self.__targets.remove(enemy)
		self.__n_targets -= 1

	def range_check(self, enemy):
		if math.sqrt(pow(enemy.position[1] - self.__position[1], 2) + pow(enemy.position[0] - self.__position[0], 2)) < self.__range:
			if enemy in self.__targets:
				return True
			elif self.add_target(enemy) is True:
				return True
		else:
			if enemy in self.__targets:
				self.remove_target(enemy)
		return False