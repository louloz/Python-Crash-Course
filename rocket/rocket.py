# Rocket

# Louis Lozano
# 07-16-2019

# File Name: rocket.py

# Python Version: 3.5.3

# Description: Makes a ship that can move in 4 directions and limits the ship's
#   range to the edge of the screen.

import sys

import pygame

class Settings():
    """A class to store all settings for Rocket."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (130, 230, 130)

        # Ship settings
        self.ship_speed_factor = 1.5

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set it's starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get it's rect.
        self.image = pygame.image.load('images/SF04.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor

        # Update rect object from self.center and self.bottom
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self):
        """Draw the ship at it's current location."""
        self.screen.blit(self.image, self.rect)

def check_events(ship):
    """Watch for keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Quits the pygame window.
            sys.exit() # Prevents error afterword.

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right.
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                # Move the ship to the left.
                ship.moving_left = True
            if event.key == pygame.K_UP:
                # Move the ship to the up.
                ship.moving_up = True
            if event.key == pygame.K_DOWN:
                # Move the ship to the down.
                ship.moving_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right.
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                # Move the ship to the left.
                ship.moving_left = False
            if event.key == pygame.K_UP:
                # Move the ship to the up.
                ship.moving_up = False
            if event.key == pygame.K_DOWN:
                # Move the ship to the down.
                ship.moving_down = False

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Keys')

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Start the main loop for the game.
    while True:

        check_events(ship)
        ship.update()
        update_screen(ai_settings, screen, ship)

run_game()

