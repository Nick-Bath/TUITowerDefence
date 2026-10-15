import math

class Tower:
	DEFAULT_SPRITE = "۩۩"
	"""Tower Class"""
	def __init__(self, position):
		self.__sprite = self.DEFAULT_SPRITE
		self.__position = position
		self.damage = 10
		self.range = 20

	@property
	def sprite(self):
		return self.__sprite

	@property
	def position(self):
		return self.__position

	def range_check(self, enemy):
		if math.sqrt(pow(enemy.position[1] - self.__position[1], 2) + pow(enemy.position[0] - self.__position[0], 2)) < self.range:
			return True 
		return False