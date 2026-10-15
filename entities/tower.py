import math

class Tower:
	DEFAULT_SPRITE = "۩۩"
	"""Tower Class"""
	DEFAULT_DAMAGE = 10
	DEFAULT_RANGE = 20
	DEFAULT_COST = 10
	def __init__(self, position):
		self.__sprite = self.DEFAULT_SPRITE
		self.__position = position
		self.__damage = self.DEFAULT_DAMAGE
		self.__range = self.DEFAULT_RANGE
		self.__cost = self.DEFAULT_COST

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

	def range_check(self, enemy):
		if math.sqrt(pow(enemy.position[1] - self.__position[1], 2) + pow(enemy.position[0] - self.__position[0], 2)) < self.__range:
			return True 
		return False