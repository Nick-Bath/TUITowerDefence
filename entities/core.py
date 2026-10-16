from entities.entity import Entity

class Core(Entity):
    DEFAULT_SPRITE = [
            " /\\",
            "<  >",
            " \\/"
    ]
    def __init__(self, position):
        self.__sprite = "BOOB"
        self.__position = position

    @property 
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: tuple):
        self.__position= position

    @property
    def sprite(self):
        return self.__sprite