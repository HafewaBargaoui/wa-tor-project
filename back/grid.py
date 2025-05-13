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
            y = random.randint(0, self.height-1)
            if self.ocean[y][x] == "💧": 
                self.ocean[y][x] = "🦈"
                new_shark = Shark(x, y)
                self.list_population.append(new_shark)

                counter_shark+=1
        counter_fish = 0
        while counter_fish < cs.INI_FISH_STARTING_POPULATION :
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)

            if self.ocean[y][x] == "💧":
                self.ocean[y][x] = "🐠"
                new_fish = Fish(x, y)
                self.list_population.append(new_fish)
                counter_fish+=1
    
    def get_random_animal(self):
        random_int = random.randint(0,len(self.list_population)-1)
        selected_animal = self.list_population.pop(random_int)
        return selected_animal

    def add_next_cycle_animals(self, animal):
        self.list_next_cycle_population.append(animal)

# x+1 -> right
# x-1 -> left
# y+1 -> upwards
# y-1 -> downwards

    def can_move(self, animal, x, y):
        if self.ocean[y][x] == "💧" or (type(animal) is Shark and self.ocean[y][x] == "🐠") :
            return True, self.ocean[y][x]
        else:
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

        # test right
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

        # test left
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

        # test down
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
        
        # test up
        can_m, content = self.can_move(animal, animal.pos_x, new_pos_y)
        if can_m:
            list_moves.append("u")
            if type(animal) is Shark:
                if content == "🐠":
                    list_prio1.append("u")

        if list_prio1:
            action = "eat"
        else:
            action = "move"
        
        return (action, list_prio1) if list_prio1 else (action, list_moves)


    def move(self, animal):
        my_moves = self.get_moves(animal)
        if not my_moves[1]:
            return False
        direction = random.choice(my_moves[1])
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
            self.eat(animal)
        self.reproduce(animal, old_pos_x, old_pos_y)


    def eat(self, animal):
        for indice_animal in range(0,len(self.list_population)):
            if animal.pos_x == self.list_population[indice_animal].pos_x and animal.pos_y == self.list_population[indice_animal].pos_y:
                del self.list_population[indice_animal]
                break
        else:
            for indice_animal in range(0,len(self.list_next_cycle_population)):
                if animal.pos_x == self.list_next_cycle_population[indice_animal].pos_x and animal.pos_y == self.list_next_cycle_population[indice_animal].pos_y:
                    del self.list_next_cycle_population[indice_animal]
                    break

        animal.eat()


    def reproduce(self, animal, old_pos_x, old_pos_y):
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
            animal.energy -= 1
            if not animal.can_starve():
                self.add_next_cycle_animals(animal)
            else:
                self.ocean[animal.pos_y][animal.pos_x] = "💧"
        if type(animal) is Fish:
            self.add_next_cycle_animals(animal)
    
    def cycle(self):
        while self.list_population:
            animal = self.get_random_animal()
            self.move(animal)
            self.finish_animal_turn(animal)

        self.list_population = self.list_next_cycle_population
        self.list_next_cycle_population = []


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

