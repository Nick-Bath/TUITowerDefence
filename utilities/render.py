from entities.player import Player

class Render:
	@staticmethod
	def render_objects(window, max_positions, player, waves_encountered, clock, enemy_list, towers, enemy_count, enemies_spawned, error_message=""):
		window.erase()

		#rendering displayed information
		window.addstr(2, 2, f"{clock}")
		window.addstr(1, 2, "Enemies = " + str(len(enemy_list)))
		window.addstr(1, max_positions[1] - 20, "Player HP: " + str(player.hp))
		window.addstr(1, max_positions[1] - 50, "Towers: " + str(len(towers)))
		window.addstr(2, max_positions[1] - 20, "Money: " + str(player.money))
		if clock % 100 == 0 and clock != 0 and enemies_spawned <= enemy_count:
			enemies_spawned += 1
		i = 0
		#rendering baddies
		for baddie in enemy_list:
			if i < enemies_spawned:
				window.addstr(baddie.position[0], baddie.position[1], baddie.sprite)
				window.addstr(baddie.position[0] + 1, baddie.position[1], str(baddie.hp))
			i += 1
		#rendering towers
		for tower in towers: 
			window.addstr(tower.position[0], tower.position[1], tower.sprite)
			for baddie in enemy_list:
				if tower.range_check(baddie) and clock % 10 == 0:
					baddie.lose_hp(tower.damage)
					if baddie.hp <= 0:
						player.earn_money(baddie.level)
						enemy_list.remove(baddie)
						enemies_spawned -= 1
		
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
		if len(error_message) > 0:
			window.addstr(0, (max_positions[1]//2) - (len(error_message) // 2), error_message)
			

		return enemies_spawned