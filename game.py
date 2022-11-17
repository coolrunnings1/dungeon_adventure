import pygame
import sys
from settings import Settings
from player import Player


class Dungeon_Adventure:

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.player = Player(self)

    def run_game(self):
        while True:
            self._check_events()
            self.player.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # check how this code actually works
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # check this code too
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to pressing keys"""
        if event.key == pygame.K_d:
            self.player.moving_right = True
        if event.key == pygame.K_a:
            self.player.moving_left = True

    def _check_keyup_events(self, event):
        """Respond to releasing keys"""
        if event.key == pygame.K_d:
            self.player.moving_right = False
        if event.key == pygame.K_a:
            self.player.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.player.blit_character()  # update blitting the character onto screen
        pygame.display.flip()


if __name__ == '__main__':
    dg = Dungeon_Adventure()
    dg.run_game()
