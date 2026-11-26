"""Enemy abstract class"""

from abc import ABC, abstractmethod

class Enemy(ABC):
	"""Enemy abstract class"""
	@property
	@abstractmethod
	def sprite(self) -> str: ...

	@property
	@abstractmethod
	def position(self) -> tuple: ...

	@property
	@abstractmethod
	def vel(self) -> int: ...

	@property
	@abstractmethod
	def hp(self) -> int: ...

	@property
	@abstractmethod
	def level(self) -> int: ...

	@property
	@abstractmethod
	def projectiles(self) -> list: ...

	@property
	@abstractmethod
	def direction(self) -> int: ...

	@abstractmethod
	def move(self, enemy_route): ...

	@abstractmethod
	def lose_hp(self, damage): ...

	@abstractmethod
	def update_projectiles(self, clock): ...

	@abstractmethod
	def add_projectile(self, position, damage, projectile_sprite, projectile_sound): ...
