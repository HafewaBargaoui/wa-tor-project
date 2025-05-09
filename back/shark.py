from fish import Fish
import constants as cs

class Shark(Fish):

    def __init__(self, pos_x: int, pos_y: int):
        super().__init__(pos_x, pos_y)
        self.energy = cs.INI_SHARK_STARTING_ENERGY

    def eat(self, ini_regen: int):
        self.energy += ini_regen

    def can_repro(self):
        return True if self.repro_time >= cs.INI_SHARK_TIME_TO_REPRODUCE else False

    def can_starv(self):
        return True if self.energy <= 0 else False
    
    def __str__(self):
        return f'shark {self.pos_y}, {self.pos_x}, {self.repro_time}, {self.energy}'



#TEST

# ini_repro_shark = 5
# ini_energy = 10
# ini_regen = 5


# shark1 = Shark(1,2,0)
# print(shark1)



# if shark1.can_repro(ini_repro_shark):
#     print('shark1 reproduces')
# else:
#     print('shark1 does not reproduce')


# if shark1.can_starv():
#     print('shark1 die')
# else:
#     print('shark1 does not die')

