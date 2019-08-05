# Stars

# Louis Lozano
# 07-24-2019

# File Name: stars.py

# Python Version: 3.5.3

# Description: 

import sys

import pygame

from pygame.sprite import Group

from settings import Settings

import game_functions as gf

def run_game():
    """Initialize pygame, settings, and screen object."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Stars")

    # Make a group of stars.
    stars = Group()

    # Create a star system
    gf.create_star_system(ai_settings, screen, stars)
    
    # Main game loop.
    while True:
        
        # Let's player quit the game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gf.update_screen(ai_settings, screen, stars)



run_game()
