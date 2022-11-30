import pygame
from pygame.sprite import Sprite
from settings import Settings


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('assets/brick_wall.png')
        self.rect = self.image.get_rect(topleft=pos)

