import pygame as pg
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # creating a bullet rect, since it does not have one to begin with.
        # Rect((top, left), (width, height))
        self.rect = pg.Rect((0, 0), (self.settings.bullet_width, self.settings.bullet_height))

        # assigning midtop of ship as mitdop of bullets.
        self.rect.midtop = ai_game.ship.rect.midtop

        # saving y cor of bullet in float form.
        self.y = float(self.rect.y)

    # for moving the bullet vertically on the screen.
    def update(self):
        # update decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # updating the position of bullet rectangle.
        self.rect.y = self.y

    # drawing the bullet on the screen
    def draw_bullet(self):
        pg.draw.rect(self.screen, self.color, self.rect)