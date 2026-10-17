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

from maps.map_generator import Map

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
	enemies_spawned = 0
	towers = []
	clock = 0
	game_speedup = False
	game_state = GameState.START
 
	init_colours()
	error = Error()

	# Wave generation
	WAVES_PER_LEVEL = 3
	current_level = 1
	wave_count = 0
	difficulty = 1 # can be enumerated for Jon later
	enemy_sprite = "╭༼☉ɷ⊙༽╭"
	enemy_vel = 1
	current_wave = None

	# Map generation
	MAP_CHOICE = 0
	map_design = Map(system, MAP_CHOICE)
	map_design.enemy_spawn_pos = map_design.enemy_spawn_pos_list[MAP_CHOICE]

	

	while 1:
		
		while game_state is not game_state.GAME_OVER:
			# Game Over check
			if player.hp <= 0:
				window.addstr(0, 2, "Wave: " +str(waves_encountered))
				game_state = GameState.GAME_OVER

			# Wave generation
			# This can be wave controller in system?
			if current_wave == None or len(current_wave.enemy_list) == 0:
				enemies_spawned = 0
				wave_count += 1
				if wave_count > WAVES_PER_LEVEL:
					wave_count = 1
					current_level += 1

				current_wave = Wave(current_level, wave_count, difficulty, enemy_sprite, map_design.enemy_spawn_pos, enemy_vel)
			# wave movement
			if current_wave.wave_movement(clock, map_design, enemies_spawned):
				player.take_damage()


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
			enemies_spawned = Render.render_objects(system, player, map_design, MAP_CHOICE, wave_count, current_level, clock, current_wave.enemy_list, towers, current_wave.enemy_count, enemies_spawned, error.error_message)

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

