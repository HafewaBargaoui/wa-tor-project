import constants as cs

class Fish:

    def __init__(self, pos_x: int, pos_y: int):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.repro_time = 0

    def can_repro(self):
        return True if self.repro_time >= cs.INI_FISH_TIME_TO_REPRODUCE else False

    def __str__(self):
        return f'the fish {self.pos_y}, {self.pos_x}, {self.repro_time}'
