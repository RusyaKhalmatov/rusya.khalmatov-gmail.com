import pygame
from pygame.sprite import Sprite

class Alient(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alient, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings 
        #loading alient image and getting the rectangle parameters
        self.image = pygame.image.load('img/alient4.bmp')
        self.rect = self.image.get_rect()

        #each new alient appears in the top left corner of the window
        self.rect.x = self.rect.width #interval from the left that is equals to the width of the image alient
        self.rect.y = self.rect.height #interval from the top that is equal to the height of the image alient

        #saving the exact position of an alient
        self.x = float(self.rect.x)

    def blitme(self):
        #show the alient in current position
        self.screen.blit(self.image, self.rect)

    def update(self):
        #moves the aliens to the right 
        self.x += (self.ai_settings.alient_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x 

    def check_edge(self):
        #returns true if alien has reached the edge of a screen 
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
