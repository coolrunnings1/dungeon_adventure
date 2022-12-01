import pygame
from settings import Settings
from player import Player


class Weapons:
    def __init__(self, dg_game):
        self.screen = dg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = dg_game.settings
        self.player = dg_game.player

        self.sword_idle_image = pygame.image.load('assets/weapons/sword/sword.png')
        self.sword_rect = self.sword_idle_image.get_rect()

        self.sword_right_image = pygame.image.load('assets/weapons/sword/sword_right.png')
        self.sword_rect = self.sword_right_image.get_rect()

        self.attack = False
        self.idle = False

    def update(self):
        if self.attack:
            self.screen.blit(self.sword_right_image, self.player.character_rect.midright)
        elif not self.attack:
            self.screen.blit(self.sword_idle_image, self.player.character_rect.midright)

    def blit_weapon(self):
        """blit the sword with the player"""
        self.screen.blit(self.sword_idle_image, self.player.character_rect.midright)
