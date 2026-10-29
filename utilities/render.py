import curses
from entities.player import Player
from maps.map_generator import Map
from utilities.colours import GREEN, RED


class Render:
	@staticmethod
	def render_objects(system, player, map_design, MAP_CHOICE, wave_count, current_level, clock, enemy_list, towers, enemy_count, enemies_spawned, error_message=""):
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
		try:
			for baddie in enemy_list:
				if i < enemies_spawned:
					system.window.addstr(baddie.position[0], baddie.position[1], baddie.sprite, curses.color_pair(RED))
					system.window.addstr(baddie.position[0] + 1, baddie.position[1], str(baddie.hp), curses.color_pair(RED))
				i += 1
		except:
			pass
		#rendering towers
		for tower in towers: 
			system.window.addstr(tower.position[0], tower.position[1], tower.sprite)
			tower.prune_targets(enemy_list)
			for baddie in enemy_list:
				tower.range_check(baddie)
			tower.fire(clock)

		# move projectiles and apply hits, once per enemy per frame
		for baddie in enemy_list:
			baddie.update_projectiles(clock)

		# remove dead enemies (iterate over a copy so the list can change safely)
		for baddie in list(enemy_list):
			if baddie.hp <= 0:
				player.earn_money(baddie.level)
				enemy_list.remove(baddie)
				enemies_spawned -= 1
				for tower in towers:
					tower.remove_target(baddie)

		# render projectiles for every enemy (this was only drawing the last enemy's before)
		for baddie in enemy_list:
			for projectile in baddie.projectiles:
				system.window.addstr(projectile.position[0], projectile.position[1], projectile.sprite)

		# Map
		system.window.attron(curses.color_pair(GREEN) | curses.A_BOLD)

		# This refreshes coords until maps become a pad
		map_design.map_coords_hor = []
		map_design.map_coords_ver = []
		map_design.map_list[MAP_CHOICE](system)

		
		system.window.attroff(curses.color_pair(GREEN) | curses.A_BOLD)

		# player
		system.window.addstr(player.position[0], player.position[1], player.sprite)
		# Error?
		if len(error_message) > 0:
			system.window.addstr(0, (system.max_positions[1]//2) - (len(error_message) // 2), error_message)


		return enemies_spawned

	
	@staticmethod
	def buildMenu(system, player, key, build_menu_active, selected_tower):
		height, width = 4, 19
		if player.position > (system.max_positions[0]//2, system.max_positions[1]//2):
			top, left = player.position[0] + 1, player.position[1] - width // 2 + 1
		else:
			top, left = player.position[0] - 4, player.position[1] - width // 2 + 1

		tower_selection_pad = curses.newpad(height, width)
		alt_tower_list = ["۩", "✪", "♖", "✷"]
		
		if key in ("1", "2", "3", "4"):
			selected_tower = int(key) - 1

		if build_menu_active:
			tower_selection_pad.erase()
			spacing = 0
			for i in range(len(alt_tower_list)):
				col = i + spacing + 3
				tower_selection_pad.addstr(height - 3, i + spacing + 3, alt_tower_list[i])
				tower_selection_pad.addstr(height - 2, i + spacing + 2, "$10")
				if i == selected_tower:
					tower_selection_pad.addch(height - 3, col - 2, "[")
					tower_selection_pad.addch(height - 3, col + 2, "]")
				spacing += 3
			tower_selection_pad.box()
			tower_selection_pad.refresh(0, 0, top, left, top + height - 1, left + width - 1)

		return selected_tower