import sys
import pygame
from bullet import Bullet 
from alient import Alient

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_keydown_events(event, ai_settings,screen,ship, bullets):
    if event.key == pygame.K_RIGHT:
         #move the ship to the right 
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_events(ai_settings,screen,ship, bullets):
    #processing keypad or mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
	        sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings, screen, ship, alients, bullets):
    #updates the image on the screen and displays new screen 
    screen.fill(ai_settings.bg_color)
    #all the bullets are displayed behind the picture of a ship and alients
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alients.draw(screen)
	#displaying the last rendered display 
    pygame.display.flip()

def bullet_delete(bullets):
    for bullet in bullets.copy():
        if bullet.rect.y <=0:
            bullets.remove(bullet)

def update_bullets(bullets):
    #updates the position and deletes old bullets 
    bullets.update()
    bullet_delete(bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    #Shot the bullet
    if len(bullets) < ai_settings.bullets_allowed: 
        #creation of a new bullet and addition it to the group bullets
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet) 

def get_number_of_aliens_x(ai_settings,alient_width):
    available_space_x = ai_settings.screen_width - (2 * alient_width)
    number_alient_x = int(available_space_x/(2*alient_width))
    return number_alient_x

def create_alient(ai_settings, screen, alients, alient_number):
    alient = Alient(ai_settings,screen)
    alient_width = alient.rect.width
    alient.x = alient_width + 2 * alient_width * alient_number
    alient.rect.x = alient.x
    alients.add(alient)

def create_fleet(ai_settings, screen, alients):
    alient = Alient(ai_settings,screen)
    number_alient_x = get_number_of_aliens_x(ai_settings,alient.rect.width)
    #creation of the first raw of aliens
    for alient_number in range(number_alient_x):
        create_alient(ai_settings,screen, alients,alient_number)
    