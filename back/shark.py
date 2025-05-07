from fish import Fish
import uuid


class Shark(Fish):

    def __init__(self, pos_x: int, pos_y: int, repro_time: int, ini_energy: int):
        super().__init__(pos_x, pos_y, repro_time)
        self.energy = ini_energy
        self.id = uuid.uuid4()


    def eat(self, regen: int):
        self.energy += regen

    def move(self, list_a_move: list):
        pass

    def repro(self):
        pass

    #TODO to remove: can_move will be decided by the grid
    def can_move(self):
        return True

    def can_repro(self, param_repro_shark):
        return True if self.repro_time >= param_repro_shark and self.can_move() else False

    def __str__(self):
        return f'shark {self.pos_x}, {self.pos_y}, {self.repro_time}, {self.energy}, {self.id}'


#TODO to be replaced with repro_shark from the ini file
ini_repro_shark = 5

#TODO to be replaced with energy from the ini file
ini_energy = 10

#TODO to be replaced with regen from the ini file
ini_regen = 5



shark1 = Shark(1,2,6,10)
print(shark1)


if shark1.can_move():
    print('shark1 moves')
else:
    print('shark1 reste sur place')


if shark1.can_repro(ini_repro_shark):
    print('shark1 reproduces')
else:
    print('shark1 does not reproduce')
