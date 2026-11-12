import curses
from entities.player import Player
from utilities.colours import GREEN, RED
from entities.tower import Tower, Magic, Snipper, Rock, Power

TOWER_TYPES = [Snipper, Power, Rock, Magic]

class Render:
	@staticmethod
	def render_objects(system, WINDOW_MIN_SIZE, player, map_design, clock, towers, current_wave, enemy_list, error_message=""):
		system.window.erase()
		CENTER_X = system.max_positions[1]//2 - WINDOW_MIN_SIZE[1]//2
		CENTER_Y = system.max_positions[0]//2 - WINDOW_MIN_SIZE[0]//2

		
		#rendering displayed information
		system.window.addstr(CENTER_Y + 3, CENTER_X + 2, f"{clock}")
		system.window.addstr(CENTER_Y + 2, CENTER_X + 2, "Enemies = " + str(enemy_list.length))

		system.window.addstr(CENTER_Y + 2, CENTER_X + WINDOW_MIN_SIZE[1] - 20, "Player HP: " + str(player.hp))
		system.window.addstr(CENTER_Y + 2, CENTER_X + WINDOW_MIN_SIZE[1] - 50, "Towers: " + str(len(towers)))
		system.window.addstr(CENTER_Y + 3, CENTER_X + WINDOW_MIN_SIZE[1] - 20, "Money: " + str(player.money))
		system.window.addstr(CENTER_Y + 1, CENTER_X + 2, "Level: " +str(current_wave.level) + ", Wave: " +str(current_wave.wave))


		if clock % current_wave.spawn_rate == 0 and clock != 0 and current_wave.enemies_spawned < enemy_list.length:
			for baddie in enemy_list.enemies:
				if not baddie.released:
					baddie.released = True
					break
		#rendering baddies
		try:
			for baddie in enemy_list.enemies:
				if baddie.released:
					system.window.addstr(baddie.position[0], baddie.position[1], baddie.sprite, baddie.color)
					system.window.addstr(baddie.position[0] + 1, baddie.position[1], str(baddie.hp), baddie.color)
		except:
			pass
		#rendering towers
		for tower in towers: 
			system.window.addstr(tower.position[0], tower.position[1], tower.sprite)

		# render projectiles for every enemy (this was only drawing the last enemy's before)
		for baddie in enemy_list.enemies:
			for projectile in baddie.projectiles:
				system.window.addstr(projectile.position[0], projectile.position[1], projectile.sprite)

		# Rendering Map
		system.window.attron(curses.color_pair(GREEN) | curses.A_BOLD)

		for coordinate in map_design.map_coords_hor:
			system.window.addstr(coordinate[0], coordinate[1], "_")

		# Rendering Core
		i = 0
		for line in map_design.core.sprite:
			system.window.addstr(map_design.core.position[0] + i, map_design.core.position[1], line)
			i += 1

		system.window.attroff(curses.color_pair(GREEN) | curses.A_BOLD)

		# Rendering Border
		for coordinate in map_design.border_coords_hor:
			system.window.addstr(coordinate[0], coordinate[1], "_")
		for coordinate in map_design.border_coords_ver:
			system.window.addstr(coordinate[0], coordinate[1], "|")


		# player
		system.window.addstr(player.position[0], player.position[1], player.sprite)
		# Error?
		if len(error_message) > 0:
			system.window.addstr(0, (WINDOW_MIN_SIZE[1]//2) - (len(error_message) // 2), error_message)


	
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
			selected_tower = TOWER_TYPES[int(key) - 1]

		if build_menu_active:
			tower_selection_pad.erase()
			spacing = 0
			for i, tower_class in enumerate(TOWER_TYPES):
				col = i + spacing + 3
				tower_selection_pad.addstr(height - 3, i + spacing + 3, tower_class.DEFAULT_SPRITE)
				tower_selection_pad.addstr(height - 2, i + spacing + 2, f"${tower_class.DEFAULT_COST}")
				if tower_class is selected_tower:
					tower_selection_pad.addch(height - 3, col - 2, "[")
					tower_selection_pad.addch(height - 3, col + 2, "]")
				spacing += 3
			tower_selection_pad.box()
			tower_selection_pad.refresh(0, 0, top, left, top + height - 1, left + width - 1)

		return selected_tower