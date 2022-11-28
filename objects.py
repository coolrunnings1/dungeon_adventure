import pygame
from pygame.sprite import Sprite


class Objects:
    def __init__(self):


        # get display surface
        self.display_surface = pygame.display.get_surface()

        # srpite Group Setup
        self.visible_objects = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        for

    def run(self):
        self.visible_objects.draw(self.display_surface)


