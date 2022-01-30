import pygame as pg


# defining a class to manage ship.
class Ship:

    # ai_game is the reference of the current object created.
    def __init__(self, ai_game):
        # all pygame elements are treated as rectangles.

        # assigning all the properties of game screen to ship screen therefore it can be accessed throughout
        # the program.
        self.screen = ai_game.screen
        # assigning settings to the variable setting. settings of every instance is special for that ship.
        self.settings = ai_game.settings
        # accessing the screen's rect attribute so that we can place our ship anywhere on the screen.
        self.screen_rect = ai_game.screen.get_rect()
        # .load, loads the targeted image and returns a surface representing that image.
        self.image = pg.image.load('images/ship.bmp')
        # accessing image's rect attribute so that we can use it later to place the ship.
        # returns a new rectangle covering the entire surface.
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        # storing a decimal value for x coordinates of ship rect because pygame rect cannot store float value.
        self.x = float(self.rect.x)
        # Right movement flag
        self.moving_right = False

        # left movement flag
        self.moving_left = False

    def update(self):
        # updating the position on the basis of input.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # updating rect position to the new position.
        self.rect.x = self.x

    def draw_ship(self):
        # blit, draws the source on the surface at the specified position.
        self.screen.blit(self.image, self.rect)