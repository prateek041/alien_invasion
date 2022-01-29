import pygame as pg


# defining a class to manage ship.
class Ship:

    # ai_game is the reference of the current object created.
    def __init__(self, ai_game):
        # all pygame elements are treated as rectangles.

        # assigning all the properties of game screen to ship screen therefore it can be accessed throughout
        # the program.
        self.screen = ai_game.screen
        # accessing the screen's rect attribute so that we can place our ship anywhere on the screen.
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pg.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):

        self.screen.blit(self.image, self.rect)