import sys
import pygame
import stats as st
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

    st.create_plot()

    # Main loop
    while True:
        print(cs.INI_AUTO_PLAY)
        # Auto mode / one cycle at a time mode
        if cs.INI_AUTO_PLAY:
            key_input = "n"
        else:
            key_input = input('Press "n" to play th next cycle. \nPress "c" to stop \n')

        nb_cycle += 1
        if key_input.lower() == "c":
            break
        if key_input.lower() == "n":
            print(f"Cycle count: {nb_cycle}")
            # Call to the Grid full cycle method
            my_grid.cycle()
            # Updating the pygame display
            update_display(my_grid.ocean, screen, cell_size)
            # Getting the populations
            nb_fish, nb_sharks = my_grid.print_population()
            # Updating the plots with this cycle populations
            st.update_plot(nb_cycle, nb_fish, nb_sharks)

            # Stop the simulation if no sharks / fish are alive
            if not nb_sharks or not nb_fish:
                st.close_plot()
                pygame.quit()
                sys.exit()
                break

main()
