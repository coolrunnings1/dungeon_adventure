import pygame
import sys
from settings import Settings
from player import Player
from enemy import Enemy
from sword import Weapons


# from weapons import Objects

class Dungeon_Adventure:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Dungeon Adventure')
        self.settings = Settings()

        # creates rect/surface for screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.screen_surface = pygame.surface.Surface((self.screen_rect.width, self.screen_rect.height))

        # variables for inported modules
        self.player = Player(self, (40, 40))
        self.enemy = Enemy(self.screen_rect.center)
        self.sword = Weapons(self, self.player.rect)

        # Sprite groups/objects
        self.objects = pygame.sprite.Group()
        self.objects.add(self.enemy, self.player, self.sword)

        self.clock = pygame.time.Clock()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.player.attack = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.player.attack = False

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
        if event.key == pygame.K_SPACE:
            self.player.get_damage(10)
            print(f"{self.player.current_health}")

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
        self.enemy.move(self.settings.screen_width, self.settings.screen_height)
        self.player.health_xp_bar()
        pygame.display.update()
        self.clock.tick(self.settings.FPS)

    def collide(self):
        if pygame.sprite.collide_rect(self.enemy, self.player):
            self.player.current_health -= 10
            print(f"Collision: player health={self.player.current_health}")


if __name__ == '__main__':
    dg = Dungeon_Adventure()
    dg.run_game()
