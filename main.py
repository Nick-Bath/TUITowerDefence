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
import maps.map_generator as map_choice
from system import GameController
from enums.directions import Direction
from enums.game_states import GameState
from menu_options import menu_choice
from utilities.colours import init_colours
		
def main(window: curses.window):
	#game init object wihin god object
	system = GameController(window)
 
	# Minimum window size check
	# WINDOW_MIN_SIZE = (system.max_positions[0] - 1, system.max_positions[1] - 1) # for testing
	# For launch
	WINDOW_MIN_SIZE = (50, 150)

	RESIZE_TEXT = "Window too small. Please resize to at least 50x150"
	if system.max_positions[0] < WINDOW_MIN_SIZE[0] or system.max_positions[1] < WINDOW_MIN_SIZE[1]:
		window.addstr(system.max_positions[0]//2, system.max_positions[1]//2 - (len(RESIZE_TEXT) // 2), RESIZE_TEXT)
		window.refresh()
		time.sleep(3)
		return

	game_state = GameState.START

	

	init_colours()
	error = Error()
	game_state = GameState.START
 
	while 1:
		build_menu_active = False
		selected_tower = None

		player = Player((system.max_positions[0]//2, system.max_positions[1]//2))
		waves_encountered = 0
		enemies_spawned = 0
		towers = []
		clock = 0
		speed_sleeps = [0.01, 0.005, 0.0025]
		speed_lvl = 0
		# Start menu
		if game_state is not GameState.RESTART:
			game_state = menu_choice(window, game_menu(window, game_state))

		# Wave generation
		WAVES_PER_LEVEL = 3
		current_level = 1
		wave_count = 0
		difficulty = 1 # can be enumerated for Jon later
		enemy_sprite = "╭༼☉ɷ⊙༽╭"
		enemy_vel = 1
		current_wave = None

		# Map generation
		map_design = Map(system, WINDOW_MIN_SIZE)
		map_design.enemy_spawn_pos = map_design.enemy_spawn_pos_list[map_choice.MAP_CHOICE]

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
			if key in ("p", "\x1b"):
				game_state = menu_choice(window, game_menu(window, GameState.PAUSED))
				if game_state == GameState.RESTART or game_state == GameState.GAME_OVER:
					break
			elif key in movement_keys:
				player.move(system.playerMovement(key))
			#build given build menu is open
			elif key == "b" and build_menu_active == True:
				build_menu_active = False
				selected_tower = None
				if player.money - Tower.DEFAULT_COST >= 0:
					towers.append(Tower(player.position))
					player.spend_money(Tower.DEFAULT_COST)
				else:
					error.error_message = "Not Enough Money"
					error.clock_timestamp = clock
			#open build menu
			elif key == "b" and build_menu_active == False:
				build_menu_active = True
			elif key == "q":
				speed_lvl = (speed_lvl + 1) % 3


			
			#refresh screen and render objects
			enemies_spawned = Render.render_objects(system, WINDOW_MIN_SIZE, player, map_design, map_choice.MAP_CHOICE, wave_count, current_level, clock, current_wave.enemy_list, towers, current_wave.enemy_count, enemies_spawned, error.error_message)
			#build menu
			selected_tower = Render.buildMenu(system, player, key, build_menu_active, selected_tower)
			#Time Control
			if (error.clock_timestamp + 400) % 10000 == clock % 10000:
				error.error_message = ""
				error.clock_timestamp = 0
			time.sleep(speed_sleeps[speed_lvl])
			if clock > 10000:
				clock = 1
			else:
				clock += 1


if __name__ == "__main__":
	curses.wrapper(main)
