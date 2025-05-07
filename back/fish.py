

class Fish:

    def __init__(self, pos_x: int, pos_y: int):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.repro_time = 0


    def can_repro(self, ini_repro_fish):
        return True if self.repro_time >= ini_repro_fish else False

    def __str__(self):
        return f'the fish {self.pos_x}, {self.pos_y}, {self.repro_time}'



#TEST
ini_repro_fish = 6

fish1 = Fish(10,10)
fish1.repro_time = 4
print(fish1.can_repro(ini_repro_fish))