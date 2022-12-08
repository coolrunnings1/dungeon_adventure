import pygame
from pygame.sprite import Sprite
from settings import Settings


class Cursor(Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.surface.Surface((16, 16))
        self.image.blit(pygame.image.load('assets/cursor.png'), (0, 0))
        self.rect = self.image.get_rect()

    def update(self, position):
        self.rect.center = position

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
