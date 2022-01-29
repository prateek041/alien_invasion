import sys
# importing pygame module.
import pygame as pg
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800


# this is the class managing all the basic functionalities of the program.
class AlienInvasion:
    # self initialisation of the class
    def __init__(self):
        # initialising all the pygame modules.
        pg.init()
        # setting up display screen
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("ALIEN INVASION")

        # defining an attribute storing bg color of screen.
        self.bg_color = (150, 150, 150)

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
            # for refreshing the display screen i.e. to display the most recently drawn image.
            pg.display.flip()


if __name__ == '__main__':
    # make a game instance, run the game.
    ai = AlienInvasion()
    ai.run_game()