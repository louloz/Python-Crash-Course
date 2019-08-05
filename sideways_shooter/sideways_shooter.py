# Sideways Shooter

# Louis Lozano
# 07-19-2019

# File Name: sideways_shooter.py

# Python Version: 3.5.3

# Description: 

import pygame

from pygame.sprite import Group

from settings import Settings

from ship import Ship

import game_functions as gf

def run_game():
    """Initialize pygame, settings and screen object."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Sideways Shooter")

    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
