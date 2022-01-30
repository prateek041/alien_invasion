import pygame as pg
from pygame.sprite import Sprite


class Bullet:

    def __init__(self, ai_game):
        super.__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # creating a bullet rect, since it does not have one to begin with.
        # Rect((top, left), (width, height))
        self.rect = pg.Rect((0, 0), (self.settings.bullet_width, self.settings.bullet_height))

        # assigning midtop of ship as mitdop of bullets.
        self.rect.midtop = ai_game.ship.rect.midtop