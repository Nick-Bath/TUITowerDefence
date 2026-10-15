

class Player:
	"""Player Class"""
	DEFAULT_HP = 50
	DEFAULT_SPRITE = "[]"
	DEFAULT_MONEY = 100
	def __init__(self, position):
		self.__hp = self.DEFAULT_HP
		self.__sprite = self.DEFAULT_SPRITE
		self.__position = position
		self.__money = self.DEFAULT_MONEY

	@property
	def sprite(self):
		return self.__sprite

	@property
	def position(self):
		return self.__position

	@property
	def hp(self):
		return self.__hp

	@property
	def money(self):
		return self.__money

	def spend_money(self, cost):
		self.__money -= cost

	def earn_money(self, bounty):
		self.__money += bounty
		
	def take_damage(self):
		self.__hp -= 10

	def move(self, direction):
		self.__position = (self.__position[0] + direction[0], self.__position[1] + direction[1])