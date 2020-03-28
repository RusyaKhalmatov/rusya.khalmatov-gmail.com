import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
	#инициализирует игру и создает объект экрана
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alient invasion")
	#background color
	bg_color = (230,230,230)
	ship = Ship(ai_settings, screen)
	#creation of a group to save the bullets
	bullets = Group()
	alients = Group()

	gf.create_fleet(ai_settings, screen, alients)

#start of the main cycle of a program
	while True:
		#seaking for pressing the button from the keyboard
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update() #update the screen because the ship was moved to another place by pressing the button
		gf.update_bullets(bullets)
		#update screen
		gf.update_screen(ai_settings,screen,ship,alients, bullets)
		


run_game()
