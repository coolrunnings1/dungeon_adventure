import pygame
import sys
from settings import Settings
from player import Player
from sword import Sword

class Dungeon_Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Space Adventure')
        self.settings = Settings()

        # creates rect/surface for screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.screen_surface = pygame.surface.Surface((self.screen_rect.width, self.screen_rect.height))

        # variables for inported modules
        self.player = Player()
        weapons = Sword()

        # sprite groups
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(self.player)

        self.clock = pygame.time.Clock()

        self.key = pygame.key.get_pressed()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)

            # bliting drawn screen on surface
            self.screen.blit(self.screen_surface, (0, 0))
            self.sprite_group.draw(self.screen)

            self.player.move

            pygame.display.update()
            self.clock.tick(self.settings.FPS)

def __dg_game__ == '__main__':
    game = Dungeon_Game()
    game.run()


