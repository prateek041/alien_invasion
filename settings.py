class Settings:
    # a class to store all the setting for game.

    def __init__(self):
        # attributes containing setting which can be changed throughout the program.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship setting, updated as per need.
        self.ship_speed = 1.5

        # bullet settings.
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)