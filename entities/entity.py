"""entity abstract class"""

from abc import ABC, abstractmethod

class Entity(ABC):
	"""entity abstract class"""
	@property
	@abstractmethod
	def sprite(self) -> str: ...

	@property
	@abstractmethod
	def position(self) -> tuple: ...
