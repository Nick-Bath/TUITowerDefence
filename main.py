#!/usr/bin/env python3

import curses
import time
import math
from entities import Enemy, Player, Tower, Wave
from system import GameController
from enums.directions import Direction

		
def main(window: curses.window):
	#game init object wihin god object
	system = GameController(window)
	
	max_positions = system.gameStart()
	player = Player((max_positions[0]//2, max_positions[1]//2))

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
					window.addstr(max_positions[0]//2, max_positions[1]//2 - 4, "Game Over!")
					game_over = True
				for i in range(enemy_count):
					enemy_list.append(Enemy("╭༼☉ɷ⊙༽╭", ((max_positions[0]//2), 0), 1))

			#enemymovement
			i = 0
			for baddie in enemy_list:
				if baddie.position[1] == max_positions[1] - 8:
					enemy_list.remove(baddie)
					player.take_damage()
				if clock % 15 == 0 and i < enemies_spawned:
					baddie.move(enemy_direction)
				i += 1

			#refresh screen
			window.addstr(2, 2, f"{clock}")
			window.addstr(1, 2, "Enemies = " + str(len(enemy_list)))
			window.addstr(1, max_positions[1] - 20, "Player HP: " + str(player.hp))
			window.addstr(1, max_positions[1] - 50, "Towers: " + str(len(towers)))
			if clock % 100 == 0 and clock != 0 and enemies_spawned <= enemy_count:
				enemies_spawned += 1
			i = 0
			for baddie in enemy_list:
				if i < enemies_spawned:
					window.addstr(baddie.position[0], baddie.position[1], baddie.sprite)
					window.addstr(baddie.position[0] + 1, baddie.position[1], str(baddie.hp))
				i += 1
			for tower in towers: #rendering object
				window.addstr(tower.position[0], tower.position[1], tower.sprite)
				for baddie in enemy_list:
					if tower.range_check(baddie) and clock % 10 == 0:
						baddie.lose_hp(tower.damage)
						if baddie.hp <= 0:
							enemy_list.remove(baddie)
							enemies_spawned -= 1

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

			window.erase()

			#rendering object
			#path outline
			for box_y in range(int(max_positions[1])):
				window.addstr(int(max_positions[0]/2) - 3, box_y, "-")
				window.addstr(int(max_positions[0]/2) + 3, box_y, "-")
			#clear top border
			for box_x in range(-3, 4):
				window.addstr(int(max_positions[0]/2) - box_x, 0, " ")
			#bottom bottom border
			for box_x in range (-3, 4):
				window.addstr(int(max_positions[0]/2) - box_x, max_positions[1] - 1, " ")
	
			window.addstr(player.position[0], player.position[1], player.sprite)
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

