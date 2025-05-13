from back.grid import Grid as gd
import back.constants as cs
import pygame
import time
from front.display import update_display, create_display

def main():
    # Creating the Grid
    my_grid = gd.Grid()
    # Populating the Grid
    my_grid.populate_grid()
    # Print the generated ocean before cycle 1
    my_grid.print_grid()

    nb_cycle = 0
    cell_size = 5
    # pydisplay(cs.INI_GRID_HEIGHT, cs.INI_GRID_WIDTH)
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


def pydisplay(p_height, p_width):
    my_grid= Grid()
    my_grid.populate_grid()
    my_grid.print_grid()

    nb_cycle = 0

    # Dimensions
    cell_size = 5
    rows = p_height
    cols = p_width
    width = cols * cell_size
    height = rows * cell_size

    # Defining colors
    WHITE = (255, 255, 255)
    BLUE = (2, 62, 138)
    YELLOW = (255, 225, 35)
    RED = (255, 24, 0)

    # Initialiazing pygame
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Wa-tor simulation")


    # Main loop
    running = True
    while running:
        nb_cycle += 1
        print(f"Cycle count: {nb_cycle}")
        # Limiting the number of cycles to 100000
        while nb_cycle <= 100000 :
            my_grid.cycle()

            # Building the rectangle to display
            for y in range(rows):
                for x in range(cols):
                    rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                    
                    if my_grid.ocean[y][x] == "🐠":
                        # Replacing "🐠" with a yellow tile
                        color = YELLOW
                    elif my_grid.ocean[y][x] == "🦈":
                        # Replacing "🦈" with a red tile
                        color = RED
                    else:
                        # Replacing "💧" with a blue tile
                        color = BLUE
                    pygame.draw.rect(screen, color, rect)
                    # Tiles borders
                    # pygame.draw.rect(screen, WHITE, rect, 1)  # Borders

            # Drawing the full grid
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


            running = my_grid.print_population()
            print(f"Cycle: {cpt}")
            cpt += 1
#            time.sleep(0.1)

main()

