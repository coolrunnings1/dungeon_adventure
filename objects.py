import pygame

from settings import Settings


class Objects:
    def __init__(self):
        # get display surface
        self.display_surface = pygame.display.get_surface()

        # srpite Group Setup
        self.visible_objects = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

        self.settings = Settings()

    def create_map(self):
        for row in self.settings.game_map:
            print(row)

    def run(self):
        while True:
            self.visible_objects.draw(self.display_surface)
            self.create_map()
