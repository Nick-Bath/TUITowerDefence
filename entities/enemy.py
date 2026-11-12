from entities.entity import Entity
from enums.directions import Direction
from entities.projectile import Projectile
from utilities.distance import distance

class Enemy(Entity):
	"""Enemy Class"""
	DEFAULT_HP = 100
	DEFAULT_LEVEL = 1
	DEFAULT_DIRECTION = Direction.RIGHT.value
	DEFAULT_SPRITE = "╭༼☉ɷ⊙༽╭"
	DEFAULT_VELOCITY = 1

	def __init__(self, position, audio):
		self.__sprite = self.DEFAULT_SPRITE
		self.__position = position
		self.__vel = self.DEFAULT_VELOCITY
		self.__hp = self.DEFAULT_HP
		self.__level = self.DEFAULT_LEVEL
		self.__direction = self.DEFAULT_DIRECTION
		self.__projectiles = []
		self.__audio = audio
		self.__route_position = 0

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

	@property
	def projectiles(self):
		return self.__projectiles

	def add_projectile(self, position, damage, projectile_sprite, projectile_sound):
		self.__projectiles.append(Projectile(position, self, damage, projectile_sprite, projectile_sound))

	def update_projectiles(self, clock):
		to_remove = []
		for projectile in self.projectiles:
			if distance(projectile.position, self.position) == 0:
				self.__audio.play(projectile.sound)
				self.lose_hp(projectile.damage)
				to_remove.append(projectile)
			elif clock % projectile.speed == 0:
				projectile.move(self)
		for projectile in to_remove:
			self.projectiles.remove(projectile)

	@current_direction.setter
	def current_direction(self, direction):
		self.__current_direction = direction

	def move(self, enemy_route):
		self.__route_position += 1
		self.__position = enemy_route[self.__route_position]
		
	
	def lose_hp(self, damage):
		self.__hp -= damage
		#self.__audio.play("scissors")
		