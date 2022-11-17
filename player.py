import pygame

class Player:

    def __init__(self, dg_game):
        """settings for character"""
        self.screen = dg_game.screen
        self.screen_rect = self.screen.get_rect()

        self.character_image = pygame.image.load('assets/character.png')
        self.character_rect = self.character_image.get_rect()

    def blit_character(self):
        """Draw character in middle of screen"""
        self.screen.blit(self.character_image, (self.screen_rect))


