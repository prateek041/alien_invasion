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
        # .load, loads the targeted image and returns a surface representing that image.
        self.image = pg.image.load('images/ship.bmp')
        # accessing image's rect attribute so that we can use it later to place the ship.
        # returns a new rectangle covering the entire surface.
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        # movement flag
        self.moving_right = False

    def update(self):
        if self.moving_right:
            self.rect.x += 1

    def draw_me(self):
        # blit, draws the source on the surface at the specified position.
        self.screen.blit(self.image, self.rect)