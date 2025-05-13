import pygame
import sys


def create_display(p_width, p_height, p_cell_size):
    # Dimensions
    rows = p_height
    cols = p_width
    width = cols * p_cell_size
    height = rows * p_cell_size

    # Initialiazing pygame
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Wa-tor simulation")

    return screen


def update_display(p_ocean: list, p_screen, p_cell_size: int) -> None:

    # Colors
    # Water
    BLUE = (2, 62, 138)
    # Fish
    YELLOW = (255, 225, 35)
    # Shark
    RED = (255, 24, 0)


    # Affichage de la grille
    for y, line in enumerate(p_ocean):
        for x, value in enumerate(line):
            rect = pygame.Rect(x * p_cell_size, y * p_cell_size, p_cell_size, p_cell_size)

            if p_ocean[y][x] == '🐠':
                color = YELLOW
            elif p_ocean[y][x] == '🦈':
                color = RED
            else:
                color = BLUE
            pygame.draw.rect(p_screen, color, rect)
            # pygame.draw.rect(screen, WHITE, rect, 1)  # Borders

    pygame.display.flip()


    # time.sleep(0.1)

# create_display()
# update_display()

pygame.quit()
sys.exit()

