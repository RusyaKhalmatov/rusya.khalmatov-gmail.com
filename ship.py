import pygame
class Ship():
    def __init__(self,ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        #loading the ship image and getting the rectangle
        self.image = pygame.image.load('img/ship3.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #each new ship appears at the bottom of the screen 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        #flag of moving 
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        #draws the ship in current position
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx