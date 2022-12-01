import pygame
from pygame.sprite import Sprite
from settings import Settings
from player import Player


class Sword(Sprite):

    def __init__(self):
        super().__init__()

        self.sword_idle_image = pygame.image.load('assets/weapons/sword/sword.png')
        self.sword_rect = self.sword_idle_image.get_rect()

        self.sword_right_image = pygame.image.load('assets/weapons/sword/sword_right.png')
        self.sword_rect = self.sword_right_image.get_rect()

        self.cursor_image = pygame.image.load('assets/cursor.png')
        self.cursor_rect = self.cursor_image.get_rect()

        self.attack = False

    def update(self):
        if self.attack:
            self.screen.blit(self.sword_right_image, self.player.character_rect.midright)
        elif not self.attack:
            self.screen.blit(self.sword_idle_image, self.player.character_rect.midright)

    def move(self, pos):
        self.cursor_rect.center = self.settings.pos

    def blit_weapon(self):
        """blit the sword with the player"""
        self.screen.blit(self.sword_idle_image, self.player.character_rect.midright)
