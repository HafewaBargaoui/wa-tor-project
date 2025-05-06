from fish import Fish


class Shark(Fish):
    def __init__(self, pos_x: int, pos_y: int, repro_time: int, energy: int):
        super().__init__(pos_x, pos_y, repro_time)
        self.energy = energy

    def eat(self, regen: int):
        self.energy += regen

    def move(self, list_a_move: list):
        pass

    def repro(self):
        pass
    
    def __str__(self):
        return f'le requin {self.pos_x}, {self.pos_y}, {self.repro_time}, {self.energy}'

