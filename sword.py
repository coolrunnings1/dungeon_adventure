import pygame
from pygame.sprite import Sprite
from settings import Settings
from player import Player


class Weapons(Sprite):

    def __init__(self, dg_game, position):
        super().__init__()

        self.screen = dg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = dg_game.settings

        self.player = Player(self, position)

        self.image = pygame.surface.Surface((self.player.rect.x, self.player.rect.y))
        self.image.blit(pygame.image.load('assets/weapons/sword/sword.png'), (45, 40))
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        #self.rect.center = position

        # self.sword_right_image = pygame.image.load('assets/weapons/sword/sword_right.png')
        # self.sword_right_rect = self.sword_right_image.get_rect()

        # self.cursor_image = pygame.image.load('assets/cursor.png')
        # self.cursor_rect = self.cursor_image.get_rect()

        self.attack = False
        self.rotate = False

    def update(self):
        if self.attack:
            self.screen.blit(self.sword_right_image, self.player.character_rect.midright)
        elif not self.attack:
            self.screen.blit(self.sword_idle_image, self.player.character_rect.midright)

    def rotate(self, angle):
        self.sword_idle_image = pygame.transform.rotate(self.screen, angle, 1)
        self.sword_idle_rect = self.sword_right_rect.copy()
        self.sword_idle_rect.center = self.sword_idle_image.get_rect().center
        self.rotated_image = self.sword_idle_image

    def draw(self, surface):
        """draw the sword with the player"""
        surface.blit(self.image, self.rect)

