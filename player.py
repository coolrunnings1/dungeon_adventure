import pygame
from settings import Settings
from enemy import Enemy
from pygame.sprite import Sprite


class Player(Sprite):

    def __init__(self, dg_game, position):
        super().__init__()
        """settings for character"""

        self.screen = dg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = dg_game.settings

        self.image = pygame.surface.Surface((120, 80))
        self.image.blit(pygame.image.load('assets/character.png'), (40, 40))

        self.rect = self.image.get_rect()
        self.rect.center = position

        self.current_health = 1000
        self.max_health = 1000
        self.health_bar_length = 120
        self.health_ratio = self.max_health / self.health_bar_length

        self.current_xp = 0
        self.max_xp = 1000
        self.xp_bar_length = 120
        self.xp_ratio = self.max_xp / self.xp_bar_length

        # store decimal value for player's horizontal/vertical coordinate
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self, pos):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.character_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.character_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.character_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.character_speed

        # update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y
        self.health_xp_bar()

    def get_damage(self, amount):
        if self.current_health > 0:
            self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0

    def get_health(self, amount):
        if self.current_health < self.max_health:
            self.current_health += amount
        if self.current_health >= self.max_health:
            self.current_health = self.max_health

    def get_xp(self, amount):
        if self.current_xp > 0:
            self.current_xp -= amount
        if self.current_xp <= 0:
            self.current_xp = 0

    def health_xp_bar(self):
        pygame.draw.rect(self.image, (0, 0, 0), (0, 11, self.max_health / self.health_ratio, 10))
        pygame.draw.rect(self.image, (0, 255, 0), (0, 11, self.current_health / self.health_ratio, 10))

        pygame.draw.rect(self.image, (255, 255, 255), (0, 11, self.health_bar_length, 10), 1)
        pygame.draw.rect(self.image, (0, 0, 255), (0, 0, self.current_xp / self.health_ratio, 10))
        pygame.draw.rect(self.image, (255, 255, 255), (0, 0, self.xp_bar_length, 10), 1)
