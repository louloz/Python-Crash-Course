# Keys

# Louis Lozano
# 07-16-2019

# File Name: keys.py

# Python Version: 3.5.3

# Description: Makes a screen and prints event.key when a key is pressed.

import sys

import pygame

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Keys')

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # Quits the pygame window.
                sys.exit() # Prevents error afterword.

            elif event.type == pygame.KEYDOWN:
                print(event.key)

        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()
