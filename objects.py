import pygame
from settings import Settings
from tile import Tile
from player import Player


class Objects:
    def __init__(self):
        self.settings = Settings()
        # get display surface
        self.display_surface = pygame.display.get_surface()

        # srpite Group Setup
        self.visible_objects = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        for row_num, row in enumerate(self.settings.game_map):
            for col_num, col in enumerate(row):
                x = col_num * self.settings.TILESIZE
                y = row_num * self.settings.TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_objects])
                if col == 'p':
                    Player((x,y),[self.visible_objects])

    def run(self):
        self.visible_objects.draw(self.display_surface)
