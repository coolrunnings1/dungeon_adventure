import pygame
import sys
from settings import Settings
from player import Player
from enemy import Enemy
from random import randint
from cursor import Cursor


class Dungeon_Adventure:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Dungeon Adventure')
        self.settings = Settings()

        # creates rect/surface for screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.screen_surface = pygame.surface.Surface((self.screen_rect.width, self.screen_rect.height))

        # variables for imported modules
        self.player = Player(self, (40, 40))
        self.cursor = Cursor((0, 0))
        self.position = (0, 0)

        # Sprite groups/objects
        self.objects = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.objects.add(self.enemies, self.player, self.cursor)

        for i in range(50):
            self.enemies.add(Enemy((randint(0, self.settings.screen_width),
                                    randint(0, self.settings.screen_height))))
        self.clock = pygame.time.Clock()

        self.position = pygame.mouse.get_pos()

    def run_game(self):
        while True:
            self._check_events()
            self.player.update(self)
            self._update_screen()
            self.collide()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # check how this code actually works
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # check this code too
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEMOTION:
                self.position = pygame.mouse.get_pos()

    def _check_keydown_events(self, event):
        """Respond to pressing keys"""
        if event.key == pygame.K_d:
            self.player.moving_right = True
        if event.key == pygame.K_a:
            self.player.moving_left = True
        if event.key == pygame.K_s:
            self.player.moving_down = True
        if event.key == pygame.K_w:
            self.player.moving_up = True
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to releasing keys"""
        if event.key == pygame.K_d:
            self.player.moving_right = False
        if event.key == pygame.K_a:
            self.player.moving_left = False
        if event.key == pygame.K_s:
            self.player.moving_down = False
        if event.key == pygame.K_w:
            self.player.moving_up = False

    def _update_screen(self):
        self.screen.blit(self.screen_surface, (0, 0))
        self.objects.draw(self.screen)
        self.enemies.draw(self.screen)
        self.enemies.update(self.settings.screen_width, self.settings.screen_height)

        self.player.health_xp_bar()

        self.cursor.update(self.position)

        pygame.display.update()
        self.clock.tick(self.settings.FPS)

    def collide(self):
        for enemy in self.enemies:
            if pygame.sprite.collide_rect(enemy, self.player):
                self.player.get_damage(1)


if __name__ == '__main__':
    dg = Dungeon_Adventure()
    dg.run_game()
