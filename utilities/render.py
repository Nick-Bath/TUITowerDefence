import curses
from entities.player import Player
from maps.map_generator import Map
from utilities.colours import GREEN, RED


class Render:
	@staticmethod
	def render_objects(system, player, wave_count, current_level, clock, enemy_list, towers, enemy_count, enemies_spawned, error_message=""):
		system.window.erase()

		#rendering displayed information
		system.window.addstr(2, 2, f"{clock}")
		system.window.addstr(1, 2, "Enemies = " + str(len(enemy_list)))
		system.window.addstr(1, system.max_positions[1] - 20, "Player HP: " + str(player.hp))
		system.window.addstr(1, system.max_positions[1] - 50, "Towers: " + str(len(towers)))
		system.window.addstr(2, system.max_positions[1] - 20, "Money: " + str(player.money))
		system.window.addstr(0, 2, "Level: " +str(current_level) + ", Wave: " +str(wave_count))

		if clock % 100 == 0 and clock != 0 and enemies_spawned <= enemy_count:
			enemies_spawned += 1
		i = 0
		#rendering baddies
		for baddie in enemy_list:
			if i < enemies_spawned:
				system.window.addstr(baddie.position[0], baddie.position[1], baddie.sprite, curses.color_pair(RED))
				system.window.addstr(baddie.position[0] + 1, baddie.position[1], str(baddie.hp), curses.color_pair(RED))
			i += 1
		#rendering towers
		for tower in towers: 
			system.window.addstr(tower.position[0], tower.position[1], tower.sprite)
			for baddie in enemy_list:
				if tower.range_check(baddie) and clock % 10 == 0:
					baddie.lose_hp(tower.damage)
					if baddie.hp <= 0:
						player.earn_money(baddie.level)
						enemy_list.remove(baddie)
						enemies_spawned -= 1

		#path outline
		system.window.attron(curses.color_pair(GREEN) | curses.A_BOLD)
		map_test = Map()
		try:
			map_test.map_list[current_level - 1](system)
		except IndexError: #defaults to level 1 when out of maps
			map_test.map_list[0](system)
		
		system.window.attroff(curses.color_pair(GREEN) | curses.A_BOLD)
		# player
		system.window.addstr(player.position[0], player.position[1], player.sprite)
		# Error?
		if len(error_message) > 0:
			system.window.addstr(0, (system.max_positions[1]//2) - (len(error_message) // 2), error_message)
		

		return enemies_spawned