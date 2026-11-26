from abc import ABC, abstractmethod

class Tower(ABC):
	"""Abstract Tower Class"""
	@property
	@abstractmethod
	def sprite(self) -> str: ...
		

	@property
	@abstractmethod
	def position(self) -> tuple: ...

	@property
	@abstractmethod
	def damage(self) -> int: ...

	@property
	@abstractmethod
	def range(self) -> int: ...

	@property
	@abstractmethod
	def cost(self) -> int: ...

	@property
	@abstractmethod
	def targets(self) -> list: ...

	@property
	@abstractmethod
	def n_targets(self) -> list: ...

	@property
	@abstractmethod
	def max_targets(self) -> int: ...

	@property
	@abstractmethod
	def fire_rate(self) ->  int: ...

	@abstractmethod
	def add_target(self, enemy): ...

	@abstractmethod
	def remove_target(self, enemy): ...

	@abstractmethod
	def prune_targets(self, enemy_list): ...

	@abstractmethod
	def range_check(self, enemy): ...
		
	@abstractmethod
	def fire(self, clock): ...
