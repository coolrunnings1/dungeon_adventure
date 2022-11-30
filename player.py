import pygame
from settings import Settings


class Player:

    def __init__(self, dg_game):
        """settings for character"""
        self.screen = dg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = dg_game.settings

        self.character_image = pygame.image.load('assets/character.png')
        self.character_rect = self.character_image.get_rect()

        self.sword_image = pygame.image.load('assets/weapons/sword/sword.png')
        self.sword_rect = self.sword_image.get_rect()
        # self.sword_rect = self.character_rect()

        # store decimal value for ship's horizontal/vertical coordinate
        self.x = float(self.character_rect.x)
        self.y = float(self.character_rect.y)

        # Movement Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.character_rect.right < self.screen_rect.right:
            self.x += self.settings.character_speed
        if self.moving_left and self.character_rect.left > 0:
            self.x -= self.settings.character_speed
        if self.moving_down and self.character_rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.character_speed
        if self.moving_up and self.character_rect.top > 0:
            self.y -= self.settings.character_speed

    # update rect object from self.x
        self.character_rect.x = self.x
        self.character_rect.y = self.y

    def blit_character(self):
        """Draw character in middle of screen"""
        self.screen.blit(self.character_image, self.character_rect)
        self.screen.blit(self.sword_image, self.character_rect.topright)
