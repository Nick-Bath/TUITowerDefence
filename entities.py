
"""Module: Classes"""


import math


class Enemy:
	"""Enemy Class"""
	def __init__(self, character, x, y, vel):
		self.character = character
		self.x = x
		self.y = y
		self.vel = vel
		self.hp = 100

	def move_left(self, maxx):
		self.x -= self.vel
	def move_right(self, maxx):
		self.x += self.vel
	def move_up(self, maxy):
		self.y -= self.vel
		if self.y < 0:
			self.y = maxy
	def move_down(self, maxy):
		self.y += self.vel
		if self.y > maxy:
			self.x = 0
	def lose_hp(self, damage):
		self.hp -= damage

class Tower:
	"""Tower Class"""
	def __init__(self, icon, x, y):
		self.icon = icon
		self.x = x
		self.y = y
		self.damage = 10
		self.range = 20

	def range_check(self, enemy_x, enemy_y):
		if math.sqrt(pow(enemy_x - self.x, 2) + pow(enemy_y - self.y, 2)) < self.range:
			return True 
		return False

class Wave:
	"""Wave Class"""
	def wave_calc(wave):
		if wave == 1:
			return 5
		if wave == 2:
			return 15
		if wave == 3:
			return 20
		if wave == 4:
			return 0

class Player:
	"""Player Class"""
	def __init__(self):
		self.hp = 50
		
	def take_damage(self):
		self.hp -= 10