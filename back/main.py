import sys
import pygame
import grid as gd
import constants as cs
from display import update_display, create_display

def main():
    # Verifying if the number of sharks + fishes fits into the grid
    if cs.INI_GRID_WIDTH * cs.INI_GRID_HEIGHT < cs.INI_FISH_STARTING_POPULATION + cs.INI_SHARK_STARTING_POPULATION\
        + cs.INI_ROCK_STARTING_POPULATION:
        print(f"The starting population of fishes + sharks would overpopulate the grid")
        return

    # Creating the Grid
    my_grid = gd.Grid()
    # Populating the Grid
    my_grid.populate_grid()
    # Print the generated ocean before cycle 1
    my_grid.print_grid()

    nb_cycle = 0
    cell_size = 5
    screen = create_display(cs.INI_GRID_WIDTH, cs.INI_GRID_HEIGHT, cell_size)

    # Main loop
    while True:
        nb_cycle += 1
        print(f"Cycle count: {nb_cycle}")
        my_grid.cycle()
        update_display(my_grid.ocean, screen, cell_size)
        return_value = my_grid.print_population()
        if return_value:
            break


    pygame.quit()
    sys.exit()

        # key_input = input('Press "n" to play th next cycle. \nPress "c" to stop \n')
        # if key_input.lower() == "c":
        #     break
        # if key_input.lower() == "n":
        #     cpt = 0
        #     nb_cycle += 1
        #     print(f"Cycle count: {nb_cycle}")
        #     return_value = True
        #     while cpt <= 100000:
        #         my_grid.cycle()
        #         return_value = my_grid.print_population()
        #         print(f"Cycle: {cpt}")
        #         if return_value:
        #             break
        #         cpt += 1


main()
