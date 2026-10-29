from utilities.distance import distance

class Projectile:
	DEFAULT_SPRITE = "✄"
	DEFAULT_VELOCITY = 2
	def __init__(self, position, enemy, damage):
		self.__sprite = self.DEFAULT_SPRITE
		self.__position = position
		self.__target = enemy.position
		self.__velocity = self.DEFAULT_VELOCITY
		self.__damage = damage
		self.__speed = 15

	@property
	def sprite(self):
		return self.__sprite

	@property
	def position(self):
		return self.__position

	@property
	def target(self):
		return self.__target

	@property
	def velocity(self):
		return self.__velocity

	@property
	def speed(self):
		return self.__speed

	@property
	def damage(self):
		return self.__damage

	def move(self, enemy):
		self.__target = enemy.position
		if self.__target[0] < self.position[0]:
			y = self.position[0] - self.__velocity
		else:
			y = self.position[0] + self.__velocity
		if self.__target[1] < self.position[1]:
			x = self.position[1] - self.__velocity
		else:
			x = self.position[1] + self.__velocity
		self.__position = (y, x)