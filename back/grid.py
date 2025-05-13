import random
import constants as cs
from shark import Shark 
from fish import Fish

class Grid:
    # list containing the animals (Fish + Shark) who still have to play this cycle
    list_population= list()
    # list containing the animals (Fish + Shark) who already played this cycle AND are still alive for the next cycle
    list_next_cycle_population = list()
    # list containing the visual representation of the Grid
    ocean = list()

    def __init__(self) -> None:
        """ Grid Constructor
        """
        self.width = cs.INI_GRID_WIDTH
        self.height = cs.INI_GRID_HEIGHT


    def populate_grid(self) -> None:
        """ Method to initialize the Grid with the number of shaks and fishes
        """
        # Populating the ocean(visual grid) with water
        self.ocean=[["💧" for _ in range(self.width)] for _ in range(self.height)]
        counter_shark = 0
        # Adding sharks
        while counter_shark < cs.INI_SHARK_STARTING_POPULATION :
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            # the shark can be placed in a water tile only
            if self.ocean[y][x] == "💧":
                # Populating the ocean with sharks randomly placed
                self.ocean[y][x] = "🦈"
                # Adding the fish to the list_population
                new_shark = Shark(x, y)
                self.list_population.append(new_shark)
                counter_shark += 1
        counter_fish = 0
        # Adding fishes
        while counter_fish < cs.INI_FISH_STARTING_POPULATION :
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            # the fish can be placed in a water tile only
            if self.ocean[y][x] == "💧":
                # Populating the ocean with fishes randomly placed
                self.ocean[y][x] = "🐠"
                # Adding the fish to the list_population
                new_fish = Fish(x, y)
                self.list_population.append(new_fish)
                counter_fish+=1


    def get_random_animal(self) -> Fish|Shark:
        """ Method that returns a random Shark or Fish from the list_population

        Returns:
            Fish|Shark: animal selected to "play"
        """
        random_int = random.randint(0,len(self.list_population)-1)
        selected_animal = self.list_population.pop(random_int)
        return selected_animal


    def add_next_cycle_animals(self, animal: Fish|Shark) -> None:
        """ Method to add an animal to the list_next_cycle_population

        Args:
            animal (Fish|Shark): animal to add
        """
        self.list_next_cycle_population.append(animal)


    def can_move(self, animal: Fish|Shark, x: int, y: int) -> bool:
        """ Method that indicates if a move is possible

        Args:
            animal (Fish|Shark): Animal to be tested
            x (int): x position to be tested
            y (int): y position to be tested

        Returns:
            bool: the move to the x,y tile is possible
        """
        if self.ocean[y][x] == "💧" or (type(animal) is Shark and self.ocean[y][x] == "🐠") :
            return True, self.ocean[y][x]
        else:
            return False, self.ocean[y][x]


    def get_moves(self, animal: Fish|Shark) -> tuple:
        """ Method that returns a tuple with the animal possibilities

        Args:
            animal (Fish|Shark): Playing animal

        Returns:
            tuple: prefered moves | possible moves
        """
        # list containing all possible moves
        list_moves = list()
        # list containing priority moves
        list_prio1 = list()

        # x+1 -> right
        # x-1 -> left
        # y-1 -> upwards
        # y+1 -> downwards

        # Checking if the tile is inside the grid after moving
        # Checking right move
        if animal.pos_x + 1 >= self.width:
            new_pos_x = 0
        else:
            new_pos_x = animal.pos_x + 1

        # Getting right move priority|possibility
        can_m, content = self.can_move(animal, new_pos_x, animal.pos_y)
        if can_m:
            list_moves.append("r")
            if type(animal) is Shark:
                if content == "🐠":
                    list_prio1.append("r")

        # Checking left move
        if animal.pos_x - 1 < 0:
            new_pos_x = self.width - 1
        else:
            new_pos_x = animal.pos_x - 1

        # Getting left move priority|possibility
        can_m, content = self.can_move(animal, new_pos_x, animal.pos_y)
        if can_m:
            list_moves.append("l")
            if type(animal) is Shark:
                if content == "🐠":
                    list_prio1.append("l")

        # Checking down move
        if animal.pos_y + 1 >= self.height:
            new_pos_y = 0
        else:
            new_pos_y = animal.pos_y + 1

        # Getting down move priority|possibility
        can_m, content = self.can_move(animal, animal.pos_x, new_pos_y)
        if can_m:
            list_moves.append("d")
            if type(animal) is Shark:
                if content == "🐠":
                    list_prio1.append("d")

        # Checking up move
        if animal.pos_y - 1 < 0:
            new_pos_y = self.height - 1
        else:
            new_pos_y = animal.pos_y - 1
        
        # Getting up move priority|possibility
        can_m, content = self.can_move(animal, animal.pos_x, new_pos_y)
        if can_m:
            list_moves.append("u")
            if type(animal) is Shark:
                if content == "🐠":
                    list_prio1.append("u")

        # if list_prio1 is not empty, the animal is a shark and the prefered action is "eat"
        if list_prio1:
            action = "eat"
        else:
            action = "move"

        return (action, list_prio1) if list_prio1 else (action, list_moves)


    def move(self, animal: Fish|Shark) -> bool|None:
        """ Method that chooses a move from prefered available moves and applies it

        Args:
            animal (Fish|Shark): animal to be moved

        Returns:
            bool|None: returns False if no move is available
        """
        # Getting prefered moves / available moves (sharks prefer eating to just moving)
        my_moves = self.get_moves(animal)
        # if the animal can't move, it doesn't do anything
        if not my_moves[1]:
            return False
        # we select a random choice from the possible moves
        direction = random.choice(my_moves[1])
        # Saving the animal class for later
        old_animal = self.ocean[animal.pos_y][animal.pos_x]
        # Saving the animal former position (useful for reproduction)
        old_pos_x = animal.pos_x
        old_pos_y = animal.pos_y
        # Putting water in the former location
        self.ocean[animal.pos_y][animal.pos_x] = "💧"

        # Testing the chosen direction (if still inside the grid) can be upgraded with modulo
        # x+1 -> right
        # x-1 -> left
        # y-1 -> upwards
        # y+1 -> downwards

        # Applying move in the random direction
        if direction == "r":
            if animal.pos_x + 1 >= self.width:
                animal.pos_x= 0
            else:
                animal.pos_x = animal.pos_x + 1

        if direction == "l":
            if animal.pos_x - 1 < 0:
                animal.pos_x= self.width - 1
            else:
                animal.pos_x = animal.pos_x - 1

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

        # Updating the ocean with the new position
        self.ocean[animal.pos_y][animal.pos_x] = old_animal

        # if the prefered move is "eat", we have to manage the eaten fish
        if my_moves[0] == "eat" :
            self.eat(animal)
        
        # Applying the reproduce method if the animal can reproduce
        self.reproduce(animal, old_pos_x, old_pos_y)


    def eat(self, animal: Fish|Shark) -> None:
        """ Method that manages animal eating and animal eaten (only sharks eat)

        Args:
            animal (Shark): Current "playing" Shark
        """
        # Deleting the eaten fish from the list_population
        for indice_animal in range(0,len(self.list_population)):
            if animal.pos_x == self.list_population[indice_animal].pos_x and animal.pos_y == self.list_population[indice_animal].pos_y:
                del self.list_population[indice_animal]
                break
        else:
            # If the eaten fish is not in the population list, it is in the next cycle animals
            # Deleting the eaten fish from the list_next_cycle_population
            for indice_animal in range(0,len(self.list_next_cycle_population)):
                if animal.pos_x == self.list_next_cycle_population[indice_animal].pos_x and animal.pos_y == self.list_next_cycle_population[indice_animal].pos_y:
                    del self.list_next_cycle_population[indice_animal]
                    break

        # The Shark gains energy
        animal.eat()


    def reproduce(self, animal: Fish|Shark, old_pos_x: int, old_pos_y: int) -> None:
        """ Method that manages if the current animal is reproducing this cycle

        Args:
            animal (Fish|Shark): current playing animal
            old_pos_x (int): x position where to create the animal's child
            old_pos_y (int): y position where to create the animal's child
        """
        if animal.can_repro():
            if type(animal) is Shark:
                # Adding the animal to the ocean (visual grid)
                self.ocean[old_pos_y][old_pos_x] = "🦈"
                # Creating the child
                new_shark = Shark(old_pos_x,old_pos_y)
                # Adding the child to the next turn animals
                self.list_next_cycle_population.append(new_shark)
            else:
                # Adding the animal to the ocean (visual grid)
                self.ocean[old_pos_y][old_pos_x] = "🐠"
                # Creating the child
                new_fish = Fish(old_pos_x,old_pos_y)
                # Adding the child to the next turn animals
                self.list_next_cycle_population.append(new_fish)
            # Setting reproduction time to 0
            animal.repro_time = 0
        else:
            # Increasing reproduction time by 1
            animal.repro_time +=1

    def print_grid(self) -> None:
        """ Method to print the grid
        """
        for i in range (cs.INI_GRID_HEIGHT): 
            row = "  "
            for j in range(cs.INI_GRID_WIDTH):
                row += self.ocean[i][j] + "  "
            print(row)

    def finish_animal_turn(self, animal: Fish|Shark) -> None:
        """ Method that adds the current playing animal to the next cycle list (if still alive)

        Args:
            animal (Fish|Shark): Current playing animal
        """
        # if the animal is a shark, we have to verify it doesn't starve
        if type(animal) is Shark:
            animal.energy -= 1
            if not animal.can_starve():
                self.add_next_cycle_animals(animal)
            else:
                self.ocean[animal.pos_y][animal.pos_x] = "💧"
        if type(animal) is Fish:
            self.add_next_cycle_animals(animal)


    def cycle(self) -> None:
        """ Method to "play" a full cycle
        """
        # Cycling through all the animals of the list_population
        while self.list_population:
            # Gets a random animal from the list
            animal = self.get_random_animal()
            # Calls the move method of the animal
            self.move(animal)
            # Verifying if the animal is still alive at the end of his turn
            self.finish_animal_turn(animal)

        # Setting up the lists for the next cycle
        self.list_population = self.list_next_cycle_population
        self.list_next_cycle_population = []


    def print_population(self) -> bool:
        """ Method to print this cycle's stats

        Returns:
            bool: the simulation can be stopped (no more Fish|Shark alive)
        """
        nb_fishes = 0
        nb_sharks = 0
        # Counting sharks and fishes
        for animal in self.list_population:
            if type(animal) is Shark:
                nb_sharks += 1
            else:
                nb_fishes += 1

        # Printing stats
        print("")
        print(f"🦈 count: {nb_sharks}")
        print(f"🐠 count: {nb_fishes}")

        # Verifying if the simulation can be stopped
        if nb_fishes == 0 or nb_sharks == 0:
            return True

