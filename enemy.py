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

        self.rect = self.image.get_rect()
        self.rect.center = position

        self.health = 100

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.direction = 1

        self.x_velocity = 2
        self.y_velocity = 2

    def update(self, x, y):
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

        if self.rect.left < 0:
            self.x_velocity = random.randint(1, 5)
            self.rect.left = 0

        if self.rect.right > x:
            self.x_velocity = random.randint(-5, -1)
            self.rect.right = x

        if self.rect.top < 0:
            self.y_velocity = random.randint(1, 5)
            self.rect.top = 0

        if self.rect.bottom > y:
            self.y_velocity = random.randint(-5, -1)
            self.rect.bottom = y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
