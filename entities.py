
"""Module: Classes"""

from abc import ABC, abstractmethod
import math



class Entity(ABC):
	@property
	@abstractmethod
	def sprite(self) -> str: ...

	@property
	@abstractmethod
	def position(self) -> tuple: ...


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


class Tower:
	DEFAULT_SPRITE = "۩۩"
	"""Tower Class"""
	def __init__(self, position):
		self.__sprite = self.DEFAULT_SPRITE
		self.__position = position
		self.damage = 10
		self.range = 20

	@property
	def sprite(self):
		return self.__sprite

	@property
	def position(self):
		return self.__position

	def range_check(self, enemy):
		if math.sqrt(pow(enemy.position[1] - self.__position[1], 2) + pow(enemy.position[0] - self.__position[0], 2)) < self.range:
			return True 
		return False




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

class Wave:
	"""Wave Class"""
	@staticmethod
	def wave_calc(wave):
		if wave == 1:
			return 5
		if wave == 2:
			return 15
		if wave == 3:
			return 20
		if wave == 4:
			return 0