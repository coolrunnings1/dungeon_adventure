import pygame
from pygame.sprite import Sprite


class Objects(Sprite):

    def __init__(self, pos, groups):
        super().__init__()

        # get display surface
        self.display_surface = pygame.display.get_surface()

        # srpite Group Setup
        self.visible_objects = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def run(self):

