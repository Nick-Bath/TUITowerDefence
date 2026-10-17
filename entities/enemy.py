from entities.entity import Entity
from enums.directions import Direction

class Enemy(Entity):
	"""Enemy Class"""
	DEFAULT_HP = 100
	DEFAULT_LEVEL = 1
	def __init__(self, sprite, position, vel):
		self.__sprite = sprite
		self.__position = position
		self.__vel = vel
		self.__hp = self.DEFAULT_HP
		self.__level = self.DEFAULT_LEVEL
		self.__current_direction = Direction.RIGHT.value

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

	@property
	def level(self):
		return self.__level

	@property
	def current_direction(self):
		return self.__current_direction

	@current_direction.setter
	def current_direction(self, direction):
		self.__current_direction = direction

	def move(self, direction):
		self.__position = (self.__position[0] + direction[0] * self.__vel, self.__position[1] + direction[1] * self.__vel)
		
	
	def lose_hp(self, damage):
		self.__hp -= damage