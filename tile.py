import pygame
from settings import Settings


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.brick_wall_image = pygame.image.load('assets/brick_wall.png')
        self.brick_wall_rect = self.brick_wall_image.get_rect(topleft=pos)

