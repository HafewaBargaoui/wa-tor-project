from grid import Grid
import constants as cs
import pygame
import time

def main():
    # my_grid= Grid()
    # my_grid.populate_grid()
    # my_grid.print_grid()

    # nb_cycle = 0

    pydisplay(cs.INI_GRID_HEIGHT, cs.INI_GRID_WIDTH)

    # while True:

    #     key_input = input('Press "n" to play th next cycle. \nPress "c" to stop \n')
    #     if key_input.lower() == "c":
    #         break
    #     if key_input.lower() == "n":
    #         cpt = 0
    #         nb_cycle += 1
    #         print(f"Cycle count: {nb_cycle}")
    #         return_value = True
    #         while cpt <= 100000 :
    #             my_grid.cycle()
    #             return_value = my_grid.print_population()
    #             print(f"Cycle: {cpt}")
    #             if return_value:
    #                 break
    #             cpt += 1


def pydisplay(p_height, p_width):
    # Paramètres de la grille
    # grid = [
    #     [0, 1, 0, 1],
    #     [1, 0, 1, 0],
    #     [0, 1, 0, 1],
    #     [1, 0, 1, 0]
    # ]


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

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (200, 200, 200)
    BLUE = (2, 62, 138)
    YELLOW = (255, 225, 35)
    RED = (255, 24, 0)

    # Initialisation
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Wa-tor simulation")


    # Boucle principale
    running = True
    while running:
        # key_input = input('Press "n" to play th next cycle. \nPress "c" to stop \n')
        # if key_input.lower() == "c":
        #     break
        # if key_input.lower() == "n":
        cpt = 0
        nb_cycle += 1
        print(f"Cycle count: {nb_cycle}")
        return_value = True
        while cpt <= 100000 :
            my_grid.cycle()

            # Affichage de la grille
            for y in range(rows):
                for x in range(cols):
                    rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)

                    if my_grid.ocean[y][x] == '🐠':
                        color = YELLOW
                    elif my_grid.ocean[y][x] == '🦈':
                        color = RED
                    else:
                        color = BLUE
                    pygame.draw.rect(screen, color, rect)
#                    pygame.draw.rect(screen, WHITE, rect, 1)  # Borders

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


            running = my_grid.print_population()
            print(f"Cycle: {cpt}")
            cpt += 1
#            time.sleep(0.1)

main()

