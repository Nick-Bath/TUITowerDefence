import curses
from entities.core import Core
from utilities.colours import GREEN, RED

MAP_CHOICE = 0
MAP_OPTIONS = {"Map 1": 0, "Map 2": 1}
class Map:
        LANE_HOR_SIZE = 12
        LANE_VER_SIZE = 4


        def __init__ (self, system, WINDOW_MIN_SIZE):
            self.maze_top = (system.max_positions[0] - WINDOW_MIN_SIZE[0]) // 2
            self.maze_left = (system.max_positions[1] - WINDOW_MIN_SIZE[1]) // 2
            self.maze_middle_y = self.maze_top + WINDOW_MIN_SIZE[0] // 2
            self.maze_middle_x = self.maze_left + WINDOW_MIN_SIZE[1] // 2

            


            # These two defaults needs WINDOW_MIN_SIZE, so they have to be defined here instead of as class variables
            DEFAULT_CORE_POS = (self.maze_middle_y - 1, self.maze_middle_x + 67)
            DEFAULT_ENEMY_SPAWN_POS = (self.maze_middle_y, self.maze_middle_x - 75)

            self.map_list = [self.map_one] #fill list with levels
            self.core_spawn_locations = [DEFAULT_CORE_POS]
            self.core = Core(self.core_spawn_locations[MAP_CHOICE])
            self.enemy_spawn_pos_list = [DEFAULT_ENEMY_SPAWN_POS] #this needs to default to level 1 (see DEFAULT_ENEMY_SPAWN_POS)
            self.enemy_spawn_pos = (self.enemy_spawn_pos_list[MAP_CHOICE])
            self.map_coords_hor = []
            self.map_coords_ver = []
            self.border_coords_hor = []
            self.border_coords_ver = []
            self.enemy_route = []

        def map_one(self, system, WINDOW_MIN_SIZE):
            top = self.maze_top
            left = self.maze_left
            bottom = self.maze_top + WINDOW_MIN_SIZE[0] - 1
            right = self.maze_left + WINDOW_MIN_SIZE[1] - 1

            # Maze coordinates
            for x in range(self.maze_left + 1, self.maze_left + WINDOW_MIN_SIZE[1] - 1):
                self.map_coords_hor.append((self.maze_middle_y - 3, x))
                self.enemy_route.append((self.maze_middle_y, x))
                self.map_coords_hor.append((self.maze_middle_y + 3, x))

            # Top and bottom borders
            for x in range(left, right + 1):
                self.border_coords_hor.append((top, x))
                self.border_coords_hor.append((bottom, x))

            # Left and right borders
            for y in range(top + 1, self.maze_middle_y - 2):
                self.border_coords_ver.append((y, left))
                self.border_coords_ver.append((y, right))
            for y in range(self.maze_middle_y + 4, bottom + 1):
                self.border_coords_ver.append((y, left))
                self.border_coords_ver.append((y, right))

        # def map_two(self, system, WINDOW_MIN_SIZE):
        #     self.enemy_spawn_pos = (WINDOW_MIN_SIZE[0] // 5, 0)
        #     self.core.display_sprite(system)

        #     #first horizontal line
        #     range_end = int(WINDOW_MIN_SIZE[1] // 4)
        #     y_coord_top = int(WINDOW_MIN_SIZE[0]/5) - 2
        #     y_coord_bottom = int(WINDOW_MIN_SIZE[0]/5) + 2
        #     for i in range(range_end):
        #         system.window.addstr(y_coord_top, i, "_")
        #         self.map_coords_hor.append((y_coord_top, i))
        #         system.window.addstr(y_coord_bottom, i, "_")
        #         self.map_coords_hor.append((y_coord_bottom, i))

        #     #excess top
        #     for i in range(range_end, range_end + self.LANE_HOR_SIZE):
        #         system.window.addstr(y_coord_top, i, "_")
        #         self.map_coords_hor.append((y_coord_top, i))

        #     #first vertical line
        #     #left
        #     x_coord_left = range_end
        #     range_start = y_coord_bottom + 1
        #     range_end = y_coord_bottom + 8
        #     for i in range(range_start, range_end):
        #         system.window.addstr(i, x_coord_left, "|")
        #         self.map_coords_ver.append((i, x_coord_left))


        #     #right
        #     x_coord_right = x_coord_left + self.LANE_HOR_SIZE
        #     range_start = y_coord_top + 1
        #     range_end -= self.LANE_VER_SIZE
        #     for i in range(range_start, range_end):
        #         system.window.addstr(i, x_coord_right, "|")
        #         self.map_coords_ver.append((i, x_coord_right))
            
        #     #second horizontal line
        #     #top
        #     y_coord_top = range_end - 1
        #     range_start = x_coord_right + 1
        #     range_end = WINDOW_MIN_SIZE[1]
        #     for i in range (range_start, range_end):
        #         system.window.addstr(y_coord_top, i, "_")
        #         self.map_coords_hor.append((y_coord_top, i))
        #     #bottom
        #     y_coord_bottom = y_coord_top + self.LANE_VER_SIZE
        #     range_start -= self.LANE_HOR_SIZE
        #     for i in range (range_start, range_end):
        #         system.window.addstr(y_coord_bottom, i, "_")
        #         self.map_coords_hor.append((y_coord_bottom, i))