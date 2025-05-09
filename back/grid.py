import random
import constants as cs
from shark import Shark 
from fish import Fish

class Grid:
    list_population= list()
    list_next_cycle_population = list()
    ocean = list()

    def __init__(self):
        self.width = cs.INI_GRID_WIDTH
        self.height = cs.INI_GRID_HEIGHT

    def populate_grid(self):
        self.ocean=[['w' for _ in range(self.width)] for _ in range(self.height)]
        counter_shark =0
        while counter_shark < cs.INI_SHARK_STARTING_POPULATION :
            x = random.randint(0, self.width-1)
#            print(x)
            y = random.randint(0, self.height-1)
#            print(y)
            if self.ocean[y][x] == "w":
                self.ocean[y][x] = "s"
                new_shark = Shark(x, y)
                self.list_population.append(new_shark)
#                print(f"pos_x = {new_shark.pos_x}")

                counter_shark+=1
        counter_fish = 0
        while counter_fish < cs.INI_FISH_STARTING_POPULATION :
            x = random.randint(0, self.width-1)
#            print(x)
            y = random.randint(0, self.height-1)
#            print(y)
            if self.ocean[y][x] == "w":
                self.ocean[y][x] = "f"
                new_fish = Fish(x, y)
                self.list_population.append(new_fish)
                counter_fish+=1

        # print(self.ocean) 
        # print(f"{self.list_population[0].pos_x}\n{self.list_population[0].pos_y}") 
        # print(f"{self.list_population[1].pos_x}\n{self.list_population[1].pos_y}") 
        # print(len(self.list_population))
    
    def get_random_animal(self):
        random_int = random.randint(0,len(self.list_population)-1)
        selected_animal = self.list_population.pop(random_int)
        return selected_animal

    def add_next_cycle_animals(self, animal):
        self.list_next_cycle_population.append(animal)


    def select_animal_action(self, animal):
        if type(animal) is Shark:
#            eat, reproduce, move
            pass

        elif type(animal) is Fish:
            print('fish')
        else:
            print('ne se prononce pas')

# x+1 -> vers la droite
# x-1 -> vers la gauche
# y+1 -> vers le bas
# y-1 -> vers le haut


# | 0| 1| 2| 3| 4| 5| 6| 7| 8| 9|
# pos_x = 9
# pos_x += 1
# pos_x =% 10

    def can_move(self, x, y):
        if self.ocean[y][x] == "w" or (type(animal) is Shark and self.ocean[y][x] == "f") :
            print(f'can move: {self.ocean[y][x]}')
            return True, self.ocean[y][x]
        else:
            print(f'cannot move: {self.ocean[y][x]}')
            return False, self.ocean[y][x]


    def get_moves(self, animal):
        list_moves = list()
        list_prio1 = list()

        #TODO can be upgraded with modulo
        # pos = -1 -> modulo -1 = 9
        # res = pos % 10
        # print(res)
        # Checking if right move is the grid
        if animal.pos_x + 1 >= self.width:
            new_pos_x = 0
        else:
            new_pos_x = animal.pos_x + 1

        # test droite
        can_m, content = self.can_move(new_pos_x, animal.pos_y)
        if can_m:
            list_moves.append("r")
            if type(animal) is Shark:
                if content == "f":
                    list_prio1.append("r")

        # Checking if left move is the grid
        if animal.pos_x - 1 < 0:
            new_pos_x = self.width - 1
        else:
            new_pos_x = animal.pos_x - 1

        # test gauche
        can_m, content = self.can_move(new_pos_x, animal.pos_y)
        if can_m:
            list_moves.append("l")
            if type(animal) is Shark:
                if content == "f":
                    list_prio1.append("l")

        # Checking if down move is the grid
        if animal.pos_y + 1 >= self.height:
            new_pos_y = 0
        else:
            new_pos_y = animal.pos_y + 1

        # test bas
        can_m, content = self.can_move(animal.pos_x, new_pos_y)
        if can_m:
            list_moves.append("d")
            if type(animal) is Shark:
                if content == "f":
                    list_prio1.append("d")


        # Checking if up move is the grid
        if animal.pos_y - 1 < 0:
            new_pos_y = self.height - 1
        else:
            new_pos_y = animal.pos_y - 1
        
        # test haut
        can_m, content = self.can_move(animal.pos_x, new_pos_y)
        if can_m:
            list_moves.append("u")
            if type(animal) is Shark:
                if content == "f":
                    list_prio1.append("u")

        # print(list_moves)
        # print(list_prio1)
        if list_prio1:
            action = "eat"
        else:
            action = "move"
        
        return (action, list_prio1) if list_prio1 else (action, list_moves)


    def move():
        pass

    def reproduce():
        pass

    def eat():
        pass

#TEST

my_grid= Grid()
my_grid.populate_grid()
animal = my_grid.get_random_animal()
print(animal)

my_moves = my_grid.get_moves(animal)


print(f'moves: {my_moves}')

if my_moves[0] == "eat":
    print('Maanger')
else:
    print('pas faim')

my_grid.add_next_cycle_animals(animal)
print(my_grid.ocean)


