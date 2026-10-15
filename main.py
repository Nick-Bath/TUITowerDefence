#!/usr/bin/env python3

import curses
import time
import math
from game_menu import game_menu
from entities.player import Player
from entities.enemy import Enemy
from entities.wave import Wave
from entities.tower import Tower

from utilities.render import Render
from utilities.error import Error

from system import GameController
from enums.directions import Direction
from enums.game_states import GameState
from menu_choices import menu_choice
from utilities.colours import init_colours
		
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
	game_state = GameState.START
	enemy_direction = Direction.RIGHT.value
 
	init_colours()
	error = Error()
	

	while 1:
		
		while game_state is not game_state.GAME_OVER:
			if len(enemy_list) == 0:
				waves_encountered += 1
				enemy_count = Wave.wave_calc(waves_encountered)
				enemies_spawned = 0
				if Wave.wave_calc(waves_encountered) == 0 or player.hp <= 0:
					window.addstr(0, 2, "Wave: " +str(waves_encountered))
					game_state = GameState.GAME_OVER

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
			except:
				key = None
			movement_keys = ("KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT")
			if key in ("p", "\x1b") or game_state == GameState.START or game_state == GameState.GAME_OVER:
				if game_state == GameState.PLAYING:
					game_state = GameState.PAUSED
				game_state = menu_choice(game_menu(window, game_state))
			elif key in movement_keys:
				player.move(system.playerMovement(key))
			elif key == "b":
				if player.money - Tower.DEFAULT_COST >= 0:
					towers.append(Tower(player.position))
					player.spend_money(Tower.DEFAULT_COST)
				else:
					error.error_message = "Not Enough Money"	
					error.clock_timestamp = clock
			elif key == "q":
				game_speedup = True if game_speedup == False else False
			

			#refresh screen and render objects
			enemies_spawned = Render.render_objects(system, player, waves_encountered, clock, enemy_list, towers, enemy_count, enemies_spawned, error.error_message)

			#Time Control
			if (error.clock_timestamp + 400) % 10000 == clock % 10000:
				error.error_message = ""
				error.clock_timestamp = 0
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

