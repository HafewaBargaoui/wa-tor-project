import random
from shark import Shark 
from fish import Fish

class Grid:
    list_population= list()
    ini_shark_initial_energy = 5
    ini_repro_time = 10
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def populate_grid(self, ini_shark_initial_population, ini_fish_initial_population):
        ocean=[['w' for _ in range(self.width)] for _ in range(self.height)]
        print(ocean)
        counter_shark =0
        while counter_shark < ini_shark_initial_population :
            x = random.randint(0, self.width-1)
            print(x)
            y = random.randint(0, self.height-1)
            print(y)
            if ocean[y][x] == "w":
                ocean[y][x] = "s"
                new_shark = Shark(x, y, self.ini_shark_initial_energy, self.ini_repro_time)
                self.list_population.append(new_shark)
                print(f"pos_x = {new_shark.pos_x}")

                counter_shark+=1
        counter_fish = 0
        while counter_fish< ini_fish_initial_population :
            x = random.randint(0, self.width-1)
            print(x)
            y = random.randint(0, self.height-1)
            print(y)
            if ocean[y][x] == "w":
                ocean[y][x] = "f"
                new_fish = Fish(x, y, self.ini_repro_time)
                self.list_population.append(new_fish)
                counter_fish+=1

        print(ocean) 
        print(f"{self.list_population[0].pos_x}\n{self.list_population[0].pos_y}") 
        print(f"{self.list_population[1].pos_x}\n{self.list_population[1].pos_y}") 
        print(len(self.list_population))



#TEST
my_grid= Grid(5,10)
my_grid.populate_grid(2, 5)
