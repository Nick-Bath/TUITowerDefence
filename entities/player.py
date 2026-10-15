

class Player:
	"""Player Class"""
	DEFAULT_HP = 50
	DEFAULT_SPRITE = "[]"
	def __init__(self, position):
		self.__hp = self.DEFAULT_HP
		self.__sprite = self.DEFAULT_SPRITE
		self.__position = position

	@property
	def sprite(self):
		return self.__sprite

	@property
	def position(self):
		return self.__position
		
	def take_damage(self):
		self.__hp -= 10

	@property
	def hp(self):
		return self.__hp

	def move(self, direction):
		self.__position = (self.__position[0] + direction[0], self.__position[1] + direction[1])