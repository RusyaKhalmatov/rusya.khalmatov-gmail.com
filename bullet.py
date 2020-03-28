import pygame
from pygame.sprite import Sprite 

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        #creates the bullet object in current position
        super().__init__()
        self.screen = screen

        #creaton of a bullet in position (0,0) and assigning correct position
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y) # positon of a bullet
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        #moving the bullet to the top on the screen
        #updating the position of a bullet in floating format
        self.y -= self.speed_factor
        #updating the position of a rectangle
        self.rect.y = self.y 

    def draw_bullet(self):
        #draw the bullet on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)