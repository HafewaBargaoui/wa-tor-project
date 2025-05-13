import pygame
import sys


def pydisplay(ocean, p_height, p_width):
    # Paramètres de la grille
    # grid = [
    #     [0, 1, 0, 1],
    #     [1, 0, 1, 0],
    #     [0, 1, 0, 1],
    #     [1, 0, 1, 0]
    # ]


    # Dimensions
    cell_size = 50
    rows = p_height
    cols = p_width
    width = cols * cell_size
    height = rows * cell_size

    # Couleurs
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)

    # Initialisation
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Grille avec Pygame")

    # Boucle principale
    running = True
    while running:
        screen.fill(WHITE)

        # Affichage de la grille
        for y in range(rows):
            for x in range(cols):
                rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                color = BLACK if ocean[y][x] == '🐠' else GRAY
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, WHITE, rect, 1)  # Bordures

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

# pydisplay()

pygame.quit()
sys.exit()

