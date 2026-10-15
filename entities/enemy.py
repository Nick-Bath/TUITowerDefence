from entities.entity import Entity

class Enemy(Entity):
	"""Enemy Class"""
	def __init__(self, sprite, position, vel):
		self.__sprite = sprite
		self.__position = position
		self.__vel = vel
		self.__hp = 100

	@property
	def sprite(self):
		return self.__sprite

	@property
	def vel(self):
		return self.__vel

	@property
	def hp(self):
		return self.__hp

	@property
	def position(self):
		return self.__position


	def move(self, direction):
		self.__position = (self.__position[0] + direction[0] * self.__vel, self.__position[1] + direction[1] * self.__vel)
		
	
	def lose_hp(self, damage):
		self.__hp -= damage