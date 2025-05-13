from fish import Fish
import constants as cs

class Shark(Fish):

    def __init__(self, pos_x: int, pos_y: int):
        super().__init__(pos_x, pos_y)
        self.energy = cs.INI_SHARK_STARTING_ENERGY

    def eat(self):
        self.energy += cs.INI_SHARK_EATING_REGEN
        if self.energy > cs.INI_SHARK_STARTING_ENERGY:
            self.energy = cs.INI_SHARK_STARTING_ENERGY

    def can_repro(self):
        return True if self.repro_time >= cs.INI_SHARK_TIME_TO_REPRODUCE else False

    def can_starve(self):
        return True if self.energy <= 0 else False
    
    def __str__(self):
        return f'shark {self.pos_y}, {self.pos_x}, {self.repro_time}, {self.energy}'

