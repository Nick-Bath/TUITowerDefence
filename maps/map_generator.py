import curses
from entities.core import Core

class Map:
        DEFAULT_CORE_POS = (0, 0)
        def __init__ (self):
                self.map_list = [self.level_one]
                self.core = Core(self.DEFAULT_CORE_POS)

        def level_one(self, system):
            for box_y in range(int(system.max_positions[1])):
                system.window.addstr(int(system.max_positions[0]/2) - 3, box_y, "_")
                system.window.addstr(int(system.max_positions[0]/2) + 3, box_y, "_")
            self.core.position = (system.max_positions[0], system.max_positions[1] - 8)
            system.window.addstr(self.core.position[0], self.core.position[1], self.core.sprite)

        def level_two(self, system):
            for box_y in range(int(system.max_positions[1])):
                system.window.addstr(int(system.max_positions[0]/2) - 3, box_y, "_")
                system.window.addstr(int(system.max_positions[0]/2) + 3, box_y, "_")
            #clear top border
            for box_x in range(-3, 4):
                system.window.addstr(int(system.max_positions[0]/2) - box_x, 0, " ")
            #bottom bottom border
            for box_x in range (-3, 4):
                system.window.addstr(int(system.max_positions[0]/2) - box_x, system.max_positions[1] - 1, " ")