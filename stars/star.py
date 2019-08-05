# Stars

# Louis Lozano
# 07-24-2019

# File Name: star.py

# Python Version: 3.5.3

# Description: A class that modules a star.

import pygame

from pygame.sprite import Sprite

class Star(Sprite):
    """A class the models a star."""

    def __init__(self, ai_settings, screen):
        """Initialize star attributes."""
        super(Star, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the star image and set its' rect attribute.
        self.image = pygame.image.load('star_40x40.png')
        self.rect = self.image.get_rect()

        # Set each nre star at the top left of the screen.
        self.x = self.rect.width
        self.y = self.rect.height

        # Store the stars exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the star at its' current location."""
        self.screen.blit(self.image, self.rect)
