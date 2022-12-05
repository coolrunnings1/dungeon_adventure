import pygame
from pygame.sprite import Sprite
from settings import Settings


class Player(Sprite):

    def __init__(self):
        super().__init__()
        """settings for character"""
        self.image = pygame.image.load('assets/character.png')
        self.rect = self.image.get_rect()

        # store decimal value for player's horizontal/vertical coordinate
        self.x = self.settings.

        self.rect.x = self.x
        self.rect.y = self.y

        self.settings = Settings()

        self.move = False

    def move(self):
        while self.move:
            print('k')
            if self.x < self.settings.screen_width:
                self.rect.x += self.settings.character_speed
            if self.x < 0:
                self.rect.x -= self.settings.character_speed

        # update rect object from self.x

