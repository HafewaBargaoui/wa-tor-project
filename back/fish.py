import uuid
import random


class Fish:

    #TODO to be replaced by repro_fish from the ini file
    ini_repro_fish = 6


    def __init__(self, pos_x: int, pos_y: int, repro_time: int):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.repro_time = repro_time
        self.id = uuid.uuid4()

    def move(self, list_a_move: list):
        random.choice(list_a_move)

    def repro(self):
        pass

    #TODO to remove: can_move will be decided by the gris
    def can_move(self):
        return True


    def can_repro(self, ini_repro_fish):
        return True if self.repro_time >= ini_repro_fish and self.can_move() else False

    
    def __str__(self):
        return f'the fish {self.pos_x}, {self.pos_y}, {self.repro_time}'
    





    
fish1 = Fish(10,10,15)
print(fish1.can_repro(5))