import sys
import pygame
from bullet import Bullet 
from alient import Alient
from time import sleep

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

def update_bullets(ai_settings, screen,ship, alients, bullets):
    #updates the position and deletes old bullets 
    bullets.update()
    bullet_delete(bullets)
    #checking if the bullet collides with the alient
    # in case of collision delete both objects
    check_bullets_alien_collision(ai_settings, screen,ship, alients, bullets)

def check_bullets_alien_collision(ai_settings, screen,ship, alients, bullets):
    collisions = pygame.sprite.groupcollide(bullets,alients,True,True)
    if len(alients) == 0:
        bullets.empty()
        create_fleet(ai_settings,screen,ship,alients)

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

def create_alient(ai_settings, screen, alients, alient_number, row_number):
    alient = Alient(ai_settings,screen)
    alient_width = alient.rect.width
    alient.x = alient_width + 2 * alient_width * alient_number
    alient.rect.x = alient.x
    alient.rect.y = alient.rect.height + 2 * alient.rect.height * row_number
    alients.add(alient)

def get_number_rows(ai_settings, ship_height, alient_height):
    #defines the number of rows that can be displayed on the screen 
    available_space_y = (ai_settings.screen_height - (3 * alient_height) - ship_height)
    number_rows = int(available_space_y/(2*alient_height))
    return number_rows  

def create_fleet(ai_settings, screen, ship, alients):
    alient = Alient(ai_settings,screen)
    number_alient_x = get_number_of_aliens_x(ai_settings,alient.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alient.rect.height)
    #creation of the first raw of aliens
    for row_number in range(number_rows):
        for alient_number in range(number_alient_x):
            create_alient(ai_settings,screen, alients,alient_number,row_number)
    


def check_fleet_edges(ai_settings, alients):
    #reacts if the alien reaches the edge
    for alient in alients.sprites():
        if alient.check_edge():
            change_fleet_direction(ai_settings,alients)
            break

def change_fleet_direction(ai_settings, alients):
    for alient in alients.sprites():
        alient.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_alients(ai_settings,stats, screen, ship, alients, bullets):
    check_fleet_edges(ai_settings, alients)
    alients.update()
    if pygame.sprite.spritecollideany(ship,alients):
        ship_hit(ai_settings, stats, screen, ship, alients, bullets)

def ship_hit(ai_settings, stats, screen, ship, alients, bullets):
    #processes the collision ship and alien
    stats.ships_left -= 1
    
    #clean the list of alients and bullets
    alients.empty()
    bullets.empty()

    #creation of a new fleet and center the ship
    create_fleet(ai_settings,screen,ship,alients)
    ship.center_ship()

    #Pause
    sleep(0.5)

    

