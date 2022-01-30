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
        # setting up display full screen.
        # passing (0,0) tells pygame to figure out screen size in runtime.
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        # in the above line when the screen is created, setting are updated as per the screen size created.
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pg.display.set_caption("ALIEN INVASION")

        # instance created from ship class.
        self.ship = Ship(self)

        # defining an attribute storing bg color of screen.
        self.bg_color = self.settings.bg_color

    # main game loop.
    def run_game(self):
        # the surface returned by display.set mode is refreshed repeatedly by this loop.
        while True:
            # for checking the events.
            self._check_events()
            # after  checking the event, movement details updated. changing the ship's position.
            self.ship.update()
            # for updating screen.
            self._update_screen()

    # This is a helper method.
    def _check_events(self):
        # this condition is used for clearing the event queue and "get" all the commands.
        # An event is an action that the user performs while playing the game. moving mouse etc.
        # to access the events we use .event.get which returns a list of events performed since this function
        # was last.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                # checking which keydown event performed
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                # checking which keyup event performed
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pg.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
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