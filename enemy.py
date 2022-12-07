import random
from random import Random

import pygame
from pygame.sprite import Sprite
from settings import Settings


class Enemy(Sprite):

    def __init__(self, position):
        super().__init__()
        """settings for Enemy"""
        self.settings = Settings()
        self.random = Random()

        self.image = pygame.surface.Surface((40, 40))
        self.image.blit(pygame.image.load('assets/crab.png'), (0, 0))
        self.image.blit(pygame.image.load('assets/crab.png'), (0, 0))

        self.rect = self.image.get_rect()
        self.rect.center = position

        self.health = 100

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.direction = 1

        self.velocity = 2

    def move(self, x, y):

        self.rect.x += self.velocity
        self.rect.y += self.velocity

        if self.rect.x < 0:
            self.direction *= -1
            self.y += random.randint(1, 5) * self.direction
            self.rect.x = 0

        if self.rect.x > x:
            self.direction *= -1
            self.y += random.randint(1, 5) * self.direction
            self.rect.x = x

        if self.rect.y < 0:
            self.direction *= -1
            self.x += random.randint(1, 5) * self.direction
            self.rect.left = 0

        if self.rect.left > y:
            self.direction *= -1
            self.y += random.randint(1, 5) * self.direction
            self.rect.left = y

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surface):
        self.move(self.settings.screen_width, self.settings.screen_height)
        surface.blit(self.image, (self.x, self.y))
