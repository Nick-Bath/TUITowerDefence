from entities.entity import Entity
from enums.directions import Direction
from entities.projectile import Projectile
from utilities.distance import distance
import curses
from utilities.colours import RED

class Enemy(Entity):
	"""Enemy Class"""
	DEFAULT_HP = 100
	DEFAULT_LEVEL = 1
	DEFAULT_DIRECTION = Direction.RIGHT.value
	DEFAULT_SPRITE = "╭༼☉ɷ⊙༽╭"
	DEFAULT_VELOCITY = 1
	DEFAULT_COLOR = RED

	def __init__(self, position, audio):
		super().__init__()
		self._sprite = self.DEFAULT_SPRITE
		self.color = curses.color_pair(self.DEFAULT_COLOR)
		self._position = position
		self._vel = self.DEFAULT_VELOCITY
		self._hp = self.DEFAULT_HP
		self._level = self.DEFAULT_LEVEL
		self._direction = self.DEFAULT_DIRECTION
		self._projectiles = []
		self._audio = audio
		self.released = False
		self._route_position = 0

	@property
	def sprite(self):
		return self._sprite

	@property
	def vel(self):
		return self._vel

	@property
	def hp(self):
		return self._hp

	@property
	def position(self):
		return self._position

	@property
	def level(self):
		return self._level

	@property
	def direction(self):
		return self._direction

	@property
	def projectiles(self):
		return self._projectiles

	def add_projectile(self, position, damage, projectile_sprite, projectile_sound):
		self._projectiles.append(Projectile(position, self, damage, projectile_sprite, projectile_sound))

	def update_projectiles(self, clock):
		to_remove = []
		for projectile in self.projectiles:
			if distance(projectile.position, self.position) == 0:
				self._audio.play(projectile.sound)
				self.lose_hp(projectile.damage)
				to_remove.append(projectile)
			elif clock % projectile.speed == 0:
				projectile.move(self)
		for projectile in to_remove:
			self.projectiles.remove(projectile)

	@direction.setter
	def current_direction(self, direction):
		self._direction = direction

	def move(self, enemy_route):
		self._route_position += 1
		self._position = enemy_route[self._route_position]
		
	
	def lose_hp(self, damage):
		self._hp -= damage
		