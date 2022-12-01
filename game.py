import pygame
import sys
from settings import Settings
from player import Player
from sword import Sword

pygame.init()
pygame.display.set_caption('Dungeon Adventure')

settings = Settings()

# creates rect/surface for screen
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
screen_rect = screen.get_rect()
screen_surface = pygame.surface.Surface((screen_rect.width, screen_rect.height))

# variables for inported modules
player = Player()
weapons = Sword()

# sprite groups
sprite_group = pygame.sprite.Group()
sprite_group.add(player)

clock = pygame.time.Clock()

key = pygame.key.get_pressed()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if key[pygame.K_a]:
                player.move = True
        elif event.type == pygame.KEYUP:
            if key[pygame.K_d]:
                player.move = False

    screen.fill(settings.bg_color)

    # bliting drawn screen on surface
    screen.blit(screen_surface, (0, 0))
    sprite_group.draw(screen)

    player.move

    pygame.display.update()
    clock.tick(settings.FPS)
