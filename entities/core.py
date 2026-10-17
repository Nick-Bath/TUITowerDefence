from entities.entity import Entity

class Core(Entity):
    DEFAULT_SPRITE = [
            " /\\",
            "<  >",
            " \\/"
    ]
    CORE_HITBOX = 6
    def __init__(self, position):
        self.__sprite = self.DEFAULT_SPRITE
        self.__position = position
        self.__hitbox = self.CORE_HITBOX

    def display_sprite(self, system):
        i = 0
        for line in self.__sprite:
            system.window.addstr(self.position[0] + i, self.position[1], line)
            i += 1


    @property 
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: tuple):
        self.__position = position

    @property
    def sprite(self):
        return self.__sprite

    @property
    def hitbox(self):
        return self.__hitbox