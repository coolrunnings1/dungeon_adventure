import pygame


class Settings:
    def __init__(self):
        self.screen_width = 1040
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        self.character_speed = 2
        self.enemy_speed = 3
        self.character_health = 100
        self.FPS = 60
        self.TILESIZE = 40