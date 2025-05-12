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
        self.ocean=[["💧" for _ in range(self.width)] for _ in range(self.height)]
        counter_shark =0
        while counter_shark < cs.INI_SHARK_STARTING_POPULATION :
            x = random.randint(0, self.width-1)
#            print(x)
            y = random.randint(0, self.height-1)
#            print(y)
            if self.ocean[y][x] == "💧": 
                self.ocean[y][x] = "🦈"
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
            if self.ocean[y][x] == "💧":
                self.ocean[y][x] = "🐠"
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


# x+1 -> vers la droite
# x-1 -> vers la gauche
# y+1 -> vers le bas
# y-1 -> vers le haut


# | 0| 1| 2| 3| 4| 5| 6| 7| 8| 9|
# pos_x = 9
# pos_x += 1
# pos_x =% 10

    def can_move(self, animal, x, y):
        if self.ocean[y][x] == "💧" or (type(animal) is Shark and self.ocean[y][x] == "🐠") :
#            print(f'can move: {self.ocean[y][x]}')
            return True, self.ocean[y][x]
        else:
#            print(f'cannot move: {self.ocean[y][x]}')
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
        can_m, content = self.can_move(animal, new_pos_x, animal.pos_y)
        if can_m:
            list_moves.append("r")
            if type(animal) is Shark:
                if content == "🐠":
                    list_prio1.append("r")

        # Checking if left move is the grid
        if animal.pos_x - 1 < 0:
            new_pos_x = self.width - 1
        else:
            new_pos_x = animal.pos_x - 1

        # test gauche
        can_m, content = self.can_move(animal, new_pos_x, animal.pos_y)
        if can_m:
            list_moves.append("l")
            if type(animal) is Shark:
                if content == "🐠":
                    list_prio1.append("l")

        # Checking if down move is the grid
        if animal.pos_y + 1 >= self.height:
            new_pos_y = 0
        else:
            new_pos_y = animal.pos_y + 1

        # test bas
        can_m, content = self.can_move(animal, animal.pos_x, new_pos_y)
        if can_m:
            list_moves.append("d")
            if type(animal) is Shark:
                if content == "🐠":
                    list_prio1.append("d")


        # Checking if up move is the grid
        if animal.pos_y - 1 < 0:
            new_pos_y = self.height - 1
        else:
            new_pos_y = animal.pos_y - 1
        
        # test haut
        can_m, content = self.can_move(animal, animal.pos_x, new_pos_y)
        if can_m:
            list_moves.append("u")
            if type(animal) is Shark:
                if content == "🐠":
                    list_prio1.append("u")

        # print(list_moves)
        # print(list_prio1)
        if list_prio1:
            action = "eat"
        else:
            action = "move"
        
        return (action, list_prio1) if list_prio1 else (action, list_moves)


    def move(self, animal):
        my_moves = self.get_moves(animal)
        if not my_moves[1]:
#            print("can't move")
            return False
        direction = random.choice(my_moves[1])
#        print(direction)
        old_animal = self.ocean[animal.pos_y][animal.pos_x]
        old_pos_x=animal.pos_x
        old_pos_y= animal.pos_y
        self.ocean[animal.pos_y][animal.pos_x] = "💧"
        if direction == "r":
            if animal.pos_x + 1 >= self.width:
                animal.pos_x= 0
            else:
                animal.pos_x = animal.pos_x + 1

        if direction == "l":
            if animal.pos_x - 1 < 0:
                animal.pos_x= self.width -1
            else:
                animal.pos_x = animal.pos_x -1 
        if direction == "u":
            if animal.pos_y - 1 < 0:
                animal.pos_y= self.height-1
            else:
                animal.pos_y = animal.pos_y - 1
        if direction == "d":
            if animal.pos_y + 1 >= self.height:
                animal.pos_y= 0
            else:
                animal.pos_y = animal.pos_y + 1
        self.ocean[animal.pos_y][animal.pos_x] = old_animal

        if my_moves[0] == "eat" :
            # print('Action mange')
            self.eat(animal)
        self.reproduce(animal, old_pos_x, old_pos_y)


    def eat(self, animal):
        for indice_animal in range(0,len(self.list_population)):
            # print(f"Animal dans for eat 1ere list {animal}")
            if animal.pos_x == self.list_population[indice_animal].pos_x and animal.pos_y == self.list_population[indice_animal].pos_y:
                # print(f"fish a manger {self.list_population[indice_animal]}")
                del self.list_population[indice_animal]
                break
        else:
            for indice_animal in range(0,len(self.list_next_cycle_population)):
                # print(f"Animal dans for eat 2eme list {animal}")
                if animal.pos_x == self.list_next_cycle_population[indice_animal].pos_x and animal.pos_y == self.list_next_cycle_population[indice_animal].pos_y:
                    # print(f"fish manger 2 eme list{self.list_next_cycle_population[indice_animal]}")
                    del self.list_next_cycle_population[indice_animal]
                    break

        # print(f"liste a jour :{self.list_population} ")
        # print(f"liste next cycle a jour :{self.list_next_cycle_population} ")
        # print(f"animal energie avant manger {animal.energy}")
        animal.eat()
        # print(f"animal energie apres manger {animal.energy}")


    def reproduce(self, animal, old_pos_x, old_pos_y):
        #reproduce
        if animal.can_repro():
            if type(animal) is Shark:
                self.ocean[old_pos_y][old_pos_x] = "🦈"
                new_shark = Shark(old_pos_x,old_pos_y)
                self.list_next_cycle_population.append(new_shark)
            else:
                self.ocean[old_pos_y][old_pos_x] = "🐠"
                new_fish = Fish(old_pos_x,old_pos_y)
                self.list_next_cycle_population.append(new_fish)
            animal.repro_time = 0
        else:
            animal.repro_time +=1


    def print_grid(self):
        for i in range (cs.INI_GRID_HEIGHT): 
            row = "  "
            for j in range(cs.INI_GRID_WIDTH):
                row += self.ocean[i][j] + "  "
            print(row)



    def finish_animal_turn(self, animal):
        if type(animal) is Shark:
            # print(f' Energie du requin avant réduction: {animal.energy}')
            animal.energy -= 1
            if not animal.can_starv():
                # print(f'Shark does not starve {animal.energy}')
                # retirer le "s" de la grille affichage
                self.add_next_cycle_animals(animal)
            else:
                # print(f'shark is dead {animal.energy}')
                self.ocean[animal.pos_y][animal.pos_x] = "💧"
        if type(animal) is Fish:
            self.add_next_cycle_animals(animal)
    
    def cycle(self):
        # self.print_grid()
        while self.list_population:
            animal = self.get_random_animal()
            # print(animal)
            self.move(animal)
            self.finish_animal_turn(animal)
            # print(f"liste next cycle population boucle while {self.list_next_cycle_population}")
        
        self.print_grid()

        self.list_population = self.list_next_cycle_population
        self.list_next_cycle_population = []

        # print(f"liste population: {self.list_population}")
        # print(f"liste next cycle population: {self.list_next_cycle_population}")


    def print_population(self):
        nb_fishes = 0
        nb_sharks = 0

        for animal in self.list_population:
            if type(animal) is Shark:
                nb_sharks += 1
            else:
                nb_fishes += 1

        print("")
        print(f"🦈 count: {nb_sharks}")
        print(f"🐠 count: {nb_fishes}")

        if nb_fishes == 0 or nb_sharks == 0:
            return True
                         
                         
# my_grid= Grid()
# my_grid.populate_grid()
# animal = my_grid.get_random_animal()
# print(animal)
# my_moves = my_grid.get_moves(animal)
# # print(f'moves: {my_moves}')
# if my_moves[0] == "eat":
#     print('Manger')
# else:
#     print('pas faim')
# my_grid.print_grid()
# my_grid.move(animal)
# my_grid.finish_animal_turn(animal)
# print(my_grid.list_next_cycle_population)
# my_grid.print_grid()