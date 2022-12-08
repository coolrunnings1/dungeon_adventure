import math

import pygame
from pygame.sprite import Sprite
from settings import Settings
from player import Player


class Bullet(Sprite):

    def __init__(self, x, y, speed, targetx, targety):
        super().__init__()

        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.x_velocity = 2
        self.y_velocity = 2
        self.angle = math.atan2(targetx-x, targety-y)

        self.dx = math.cos(self.angle) * speed
        self.dy = math.sin(self.angle) * speed

    def update(self):
        self.rect.x += int(self.dx)
        self.rect.y += int(self.dy)

    def draw(self, surface):
        """draw the sword with the player"""
        surface.blit(self.image, (self.x, self.y))

