import pygame
from maze import Maze
from pygame.locals import (QUIT, K_ESCAPE, KEYDOWN)


# Pygame initialization
pygame.init()

# Loading resources :

# Creating the Window with title
window = pygame.display.set_mode((450, 450))
pygame.display.set_caption("Game")

# Load image game
wall = pygame.image.load("images/mur.png").convert()  # load image for wall
start = pygame.image.load("images/depart.png").convert()  # Load image
arrival = pygame.image.load("images/arrivee.png").convert()  # Load

continue_game = 1
while continue_game:
    for event in pygame.event.get():
        # If user quit the program stops
        if event.type == QUIT:
            continue_game = 0

        # If the user presses a key
        if event.type == KEYDOWN:
            # If the key is ESCAPE
            if event.key == K_ESCAPE:
                continue_game = 0
            # If the key is ENTER

    level = Maze("l1")
    level.display(window, wall)
    # Refresh the screen
    pygame.display.flip()
