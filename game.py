import pygame
import sys
from settings import Settings
from player import Player
# from weapons import Objects


class Dungeon_Adventure:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Dungeon Adventure')

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.clock = pygame.time.Clock()
        # self.objects = Objects()
        self.player = Player(self)

    def run_game(self):
        while True:
            self._update_screen()
            self.player.update()
            #self.objects.run()
            self._check_events()
            # add win/lose conditions

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
        self.screen.fill(self.settings.bg_color)
        self.player.blit_character()  # update blitting the character onto screen
        pygame.display.update()
        self.clock.tick(self.settings.FPS)


if __name__ == '__main__':
    dg = Dungeon_Adventure()
    dg.run_game()
