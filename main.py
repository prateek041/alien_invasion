import sys
import pygame as pg
from settings import Settings
from ship import Ship


# this is the class managing all the basic functionalities of the program.
class AlienInvasion:
    # self initialisation of the class
    def __init__(self):
        # initialising all the pygame modules.
        pg.init()
        # instance created from setting class.
        self.settings = Settings()
        # setting up display screen
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("ALIEN INVASION")

        # instance created from ship class.
        self.ship = Ship(self)

        # defining an attribute storing bg color of screen.
        self.bg_color = self.settings.bg_color

    # main game loop.
    def run_game(self):
        # the surface returned by display.set mode is refreshed repeatedly by this loop.
        while True:
            # this condition is used for clearing the event queue and "get" all the commands.
            # An event is an action that the user performs while playing the game. moving mouse etc.
            # to access the events we use .event which returns a list of events performed since this function
            # was last.
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            # setting the background color to the previously saved attribute. fill, fills a particular surface with
            # selected color.
            self.screen.fill(self.bg_color)

            # drawing the ship on the screen.
            self.ship.draw_me()
            # for refreshing the display screen i.e. to display the most recently drawn image.
            pg.display.flip()


if __name__ == '__main__':
    # make a game instance, run the game.
    ai = AlienInvasion()
    ai.run_game()