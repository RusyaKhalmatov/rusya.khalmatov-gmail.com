class Settings():
    #a class for storring all settings of a game 
    def __init__(self):
        #param of a screen
        self.screen_width = 960
        self.screen_height = 600 
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #bullet's parameters
        self.bullet_speed_factor = 3 
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3 

        #aliens parameteres 
        self.alient_speed_factor = 1 
        self.fleet_drop_speed = 10 
        self.fleet_direction = 1 



