# drawing project 1
# Author: julian
# Date: jan 6 2026

from turtle import Pen

import pygame


def game():
    pygame.init()

    # COLOURS - (R, G, B)
    # CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (128, 128, 128)

    # CONSTANTS
    WIDTH = 500
    HEIGHT = 500
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Your Title Here")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(WHITE)

        pygame.draw.line(screen, BLACK, (200, 200), (200, 400))
        pygame.draw.line(screen, BLACK, (200, 200), (250, 200))
        pygame.draw.line(screen, BLACK, (200, 300), (250, 300))
        pygame.draw.line(screen, BLACK, (250, 300), (250, 400))
        pygame.draw.line(screen, BLACK, (250, 400), (200, 400))
        pygame.draw.line(screen, BLACK, (350, 200), (450, 200))
        pygame.draw.line(screen, BLACK, (450, 200), (450, 400))

        # # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()
