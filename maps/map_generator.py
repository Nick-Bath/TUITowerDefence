import curses
from entities.core import Core

class Map:
        DEFAULT_CORE_POS = (10, 50)
        DEFAULT_ENEMY_SPAWN_POS = (0, 0) # this somehow needs to access system to get max_positions
        LANE_HOR_SIZE = 12
        LANE_VER_SIZE = 4

        def __init__ (self, system, MAP_CHOICE):
                self.map_list = [self.map_one, self.map_two] #fill list with levels
                self.core_spawn_locations = [(system.max_positions[0] // 2 - 1, system.max_positions[1] - 8), (system.max_positions[0] // 2, system.max_positions[1] - 8)]
                self.core = Core(self.core_spawn_locations[MAP_CHOICE])
                self.enemy_spawn_pos_list = [(system.max_positions[0]//2, 0), (system.max_positions[0] // 5, 0)] #this needs to default to level 1 (see DEFAULT_ENEMY_SPAWN_POS)
                self.enemy_spawn_pos = (self.enemy_spawn_pos_list[MAP_CHOICE])
                self.map_coords_hor = [] #this is awful because it's appending infinitely - fix by making a pad (doesn't get refreshed every loop)
                self.map_coords_ver = [] #see above

        def map_one(self, system):
            for box_y in range(int(system.max_positions[1])):
                system.window.addstr(int(system.max_positions[0]/2) - 3, box_y, "_")
                self.map_coords_hor.append((int(system.max_positions[0]/2) - 3, box_y))
                system.window.addstr(int(system.max_positions[0]/2) + 3, box_y, "_")
                self.map_coords_hor.append((int(system.max_positions[0]/2) + 3, box_y))

            self.enemy_spawn_pos = ((system.max_positions[0]//2), 0)
            self.core.display_sprite(system)

        def map_two(self, system):
            self.enemy_spawn_pos = (system.max_positions[0] // 5, 0)
            self.core.display_sprite(system)

            #first horizontal line
            range_end = int(system.max_positions[1] // 4)
            y_coord_top = int(system.max_positions[0]/5) - 2
            y_coord_bottom = int(system.max_positions[0]/5) + 2
            for i in range(range_end):
                system.window.addstr(y_coord_top, i, "_")
                self.map_coords_hor.append((y_coord_top, i))
                system.window.addstr(y_coord_bottom, i, "_")
                self.map_coords_hor.append((y_coord_bottom, i))

            #excess top
            for i in range(range_end, range_end + self.LANE_HOR_SIZE):
                system.window.addstr(y_coord_top, i, "_")
                self.map_coords_hor.append((y_coord_top, i))

            #first vertical line
            #left
            x_coord_left = range_end
            range_start = y_coord_bottom + 1
            range_end = y_coord_bottom + 8
            for i in range(range_start, range_end):
                system.window.addstr(i, x_coord_left, "|")
                self.map_coords_ver.append((i, x_coord_left))


            #right
            x_coord_right = x_coord_left + self.LANE_HOR_SIZE
            range_start = y_coord_top + 1
            range_end -= self.LANE_VER_SIZE
            for i in range(range_start, range_end):
                system.window.addstr(i, x_coord_right, "|")
                self.map_coords_ver.append((i, x_coord_right))
            
            #second horizontal line
            #top
            y_coord_top = range_end - 1
            range_start = x_coord_right + 1
            range_end = system.max_positions[1]
            for i in range (range_start, range_end):
                system.window.addstr(y_coord_top, i, "_")
                self.map_coords_hor.append((y_coord_top, i))
            #bottom
            y_coord_bottom = y_coord_top + self.LANE_VER_SIZE
            range_start -= self.LANE_HOR_SIZE
            for i in range (range_start, range_end):
                system.window.addstr(y_coord_bottom, i, "_")
                self.map_coords_hor.append((y_coord_bottom, i))