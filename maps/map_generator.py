import curses
from entities.core import Core
from utilities.colours import GREEN, RED

MAP_CHOICE = 0
MAP_OPTIONS = {"Map 1": 0, "Map 2": 1}
class Map:
        DEFAULT_CORE_POS = (10, 50)
        DEFAULT_ENEMY_SPAWN_POS = (0, 0) # this somehow needs to access system to get max_positions
        LANE_HOR_SIZE = 12
        LANE_VER_SIZE = 4


        def __init__ (self, system, WINDOW_MIN_SIZE):
            self.map_list = [self.map_one, self.map_two] #fill list with levels
            self.core_spawn_locations = [(system.max_positions[0] // 2 - 1, system.max_positions[1]//2 + (WINDOW_MIN_SIZE[1]//2) - 8), (WINDOW_MIN_SIZE[0] // 2 - 1, WINDOW_MIN_SIZE[1] - 8)]
            self.core = Core(self.core_spawn_locations[MAP_CHOICE])
            self.enemy_spawn_pos_list = [(system.max_positions[0]//2, system.max_positions[1]//2 - (WINDOW_MIN_SIZE[1]//2)), (WINDOW_MIN_SIZE[0] // 5, 0)] #this needs to default to level 1 (see DEFAULT_ENEMY_SPAWN_POS)
            self.enemy_spawn_pos = (self.enemy_spawn_pos_list[MAP_CHOICE])
            self.map_coords_hor = [] #this is awful because it's appending infinitely - fix by making a pad (doesn't get refreshed every loop)
            self.map_coords_ver = [] #see above

        def map_one(self, system, WINDOW_MIN_SIZE):
            for box_y in range(int(system.max_positions[1]//2 - (int(WINDOW_MIN_SIZE[1]) // 2)), int(system.max_positions[1]//2 + (int(WINDOW_MIN_SIZE[1]) // 2))):
                system.window.addstr(int(system.max_positions[0]//2 - 3), box_y, "_")
                self.map_coords_hor.append((int(WINDOW_MIN_SIZE[0]/2) - 3, box_y))
                system.window.addstr(int(system.max_positions[0]//2 + 3), box_y, "_")
                self.map_coords_hor.append((int(WINDOW_MIN_SIZE[0]/2) + 3, box_y))

            #border
            system.window.attroff(curses.color_pair(GREEN) | curses.A_BOLD)
            
            for i in range(int(system.max_positions[1]//2 - (int(WINDOW_MIN_SIZE[1]) // 2)), int(system.max_positions[1]//2 + (int(WINDOW_MIN_SIZE[1]) // 2))):
                system.window.addstr(int(system.max_positions[0]//2 - (int(WINDOW_MIN_SIZE[0]) // 2)), i, "_")
                system.window.addstr(int(system.max_positions[0]//2 + (int(WINDOW_MIN_SIZE[0]) // 2) - 1), i, "_")
            for i in range(int(system.max_positions[0]//2 - (int(WINDOW_MIN_SIZE[0]) // 2) + 1), int(system.max_positions[0]//2 - 3)):
                system.window.addstr(i, int(system.max_positions[1]//2 + (WINDOW_MIN_SIZE[1]//2) - 1), "|")
                system.window.addstr(i, int(system.max_positions[1]//2 - (WINDOW_MIN_SIZE[1]//2)), "|")
            for i in range(int(system.max_positions[0]//2 + 4), int(system.max_positions[0]//2 + (int(WINDOW_MIN_SIZE[0]) // 2))):
                system.window.addstr(i, int(system.max_positions[1]//2 - (WINDOW_MIN_SIZE[1]//2)), "|")
                system.window.addstr(i, int(system.max_positions[1]//2 + (WINDOW_MIN_SIZE[1]//2) - 1), "|")

            system.window.attron(curses.color_pair(GREEN) | curses.A_BOLD)

            self.core.display_sprite(system)

        def map_two(self, system, WINDOW_MIN_SIZE):
            self.enemy_spawn_pos = (WINDOW_MIN_SIZE[0] // 5, 0)
            self.core.display_sprite(system)

            #first horizontal line
            range_end = int(WINDOW_MIN_SIZE[1] // 4)
            y_coord_top = int(WINDOW_MIN_SIZE[0]/5) - 2
            y_coord_bottom = int(WINDOW_MIN_SIZE[0]/5) + 2
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
            range_end = WINDOW_MIN_SIZE[1]
            for i in range (range_start, range_end):
                system.window.addstr(y_coord_top, i, "_")
                self.map_coords_hor.append((y_coord_top, i))
            #bottom
            y_coord_bottom = y_coord_top + self.LANE_VER_SIZE
            range_start -= self.LANE_HOR_SIZE
            for i in range (range_start, range_end):
                system.window.addstr(y_coord_bottom, i, "_")
                self.map_coords_hor.append((y_coord_bottom, i))