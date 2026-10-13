#!/usr/bin/env python3

import curses
import time
import math


class Enemy:
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
	def __init__(self):
		self.hp = 50

	def take_damage(self):
		self.hp -= 10

			

		
		
def main(window: curses.window):
	stdscr = curses.initscr()
	curses.noecho() # Turn off key echoing
	curses.cbreak() # Turn off buffered input
	curses.curs_set(0) # Set cursor visibility to off
	stdscr.keypad(True) # Turn on keypad mode
	window.nodelay(True) # doesn't delay when waiting for a key
	curses.use_default_colors() # removes background

	window.box()
	maxy, maxx = stdscr.getmaxyx()
	x, y = int(maxx/2), int(maxy/2)

	player = Player()

	waves_encountered = 0
	wave_completed = True
	enemies_spawned = 0
	enemy_list = []
	towers = []
	clock = 0
	game_speedup = False
	game_over  = False


	while 1:
		

		while game_over is True:
			pass
			

		while game_over is False:
			if len(enemy_list) == 0:
				waves_encountered += 1
				enemy_count = Wave.wave_calc(waves_encountered)
				enemies_spawned = 0
				if Wave.wave_calc(waves_encountered) == 0 or player.hp <= 0:
					window.addstr(0, 2, "Wave: " +str(waves_encountered))
					window.addstr(y, x, "Game Over!")
					game_over = True
				for i in range(enemy_count):
					enemy_list.append(Enemy("😈", 0, int(maxy/2), 1))

			#enemymovement
			i = 0
			for baddie in enemy_list:
				if baddie.x == maxx - 1:
					enemy_list.remove(baddie)
					player.take_damage()
				if clock % 15 == 0 and i < enemies_spawned:
					baddie.move_right(maxx - 1)
				i += 1

			#refresh screen
			window.addstr(2, 2, f"{clock}")
			window.addstr(1, 2, "Enemies = " + str(len(enemy_list)))
			window.addstr(1, maxx - 20, "Player HP: " + str(player.hp))
			if clock % 100 == 0 and clock != 0 and enemies_spawned <= enemy_count:
				enemies_spawned += 1
			i = 0
			for baddie in enemy_list:
				if i < enemies_spawned:
					window.addstr(baddie.y, baddie.x, baddie.character)
					window.addstr(baddie.y + 1, baddie.x, str(baddie.hp))
				i += 1
			for tower in towers:
				window.addstr(tower.y, tower.x, tower.icon)
				for baddie in enemy_list:
					if tower.range_check(baddie.x, baddie.y) and clock % 10 == 0:
						baddie.lose_hp(tower.damage)
						if baddie.hp <= 0:
							enemy_list.remove(baddie)
							enemies_spawned -= 1

			#character
			try:
				key = window.getkey()
			except:
				key = None
			if key == "KEY_LEFT":
				x -= 1
			elif key == "KEY_RIGHT":
				x += 1
			elif key == "KEY_UP":
				y -= 1
			elif key == "KEY_DOWN":
				y += 1
			elif key == "b":
				towers.append(Tower("🗼", x, y))
			elif key == "s":
				enemy_list.append(Enemy("😈", 0, int(maxy/2), 1))
			elif key == "q":
				game_speedup = True

			window.erase()

			#path outline
			for box_y in range(int(maxx)):
				window.addstr(int(maxy/2) - 3, box_y, "--")
				window.addstr(int(maxy/2) + 3, box_y, "-")
			#clear top border
			for box_x in range(-3, 4):
				window.addstr(int(maxy/2) - box_x, 0, " ")
			#bottom bottom border
			for box_x in range (-3, 4):
				window.addstr(int(maxy/2) - box_x, maxx - 1, " ")
	
			window.addstr(y, x, "[]")
			window.addstr(0, 2, "Wave: " +str(waves_encountered))

			#Time Control
			
			if game_speedup is True:
				time.sleep(0.001)
				if clock > 10000:
					clock = 1
				else:
					clock += 1
			else:
				time.sleep(0.01)
				if clock > 10000:
					clock = 1
				else:
					clock += 1
	

if __name__ == "__main__":
	curses.wrapper(main)

