#!/usr/bin/env python3

import curses
import time
import math
from entities.player import Player
from entities.enemy import Enemy
from entities.wave import Wave
from entities.tower import Tower
from utilities.render import Render

from system import GameController
from enums.directions import Direction
		
def main(window: curses.window):
	#game init object wihin god object
	system = GameController(window)
	player = Player((system.max_positions[0]//2, system.max_positions[1]//2))

	waves_encountered = 0
	wave_completed = True
	enemies_spawned = 0
	enemy_list = []
	towers = []
	clock = 0
	game_speedup = False
	game_over  = False
	enemy_direction = Direction.RIGHT.value

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
					window.addstr(system.max_positions[0]//2, system.max_positions[1]//2 - 4, "Game Over!")
					game_over = True
				for i in range(enemy_count):
					enemy_list.append(Enemy("╭༼☉ɷ⊙༽╭", ((system.max_positions[0]//2), 0), 1))

			#enemymovement
			i = 0
			for baddie in enemy_list:
				if baddie.position[1] == system.max_positions[1] - 8:
					enemy_list.remove(baddie)
					player.take_damage()
				if clock % 15 == 0 and i < enemies_spawned:
					baddie.move(enemy_direction)
				i += 1

			#character
			try:
				key = window.getkey()
				movement_keys = ("KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT")
				if key in movement_keys:
					player.move(system.playerMovement(key))
				elif key == "b":
					towers.append(Tower(player.position))			
			except:
				pass
			#refresh screen and render objects
			enemies_spawned = Render.RenderObjects(window, system.max_positions, player, waves_encountered, clock, enemy_list, towers, enemy_count, enemies_spawned)

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

