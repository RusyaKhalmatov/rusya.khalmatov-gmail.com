import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stat import GameStats

def run_game():
	#инициализирует игру и создает объект экрана
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alient invasion")
	#creation of an object to keep the statistics
	stats = GameStats(ai_settings)
	#background color
	bg_color = (230,230,230)
	ship = Ship(ai_settings, screen)
	#creation of a group to save the bullets
	bullets = Group()
	alients = Group()

	gf.create_fleet(ai_settings, screen,ship, alients)

#start of the main cycle of a program
	while True:
		#seaking for pressing the button from the keyboard
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update() #update the screen because the ship was moved to another place by pressing the button
		gf.update_bullets(ai_settings,screen,ship, alients, bullets)
		gf.update_alients(ai_settings,stats, screen, ship, alients, bullets)
		#update screen
		gf.update_screen(ai_settings,screen,ship,alients, bullets)
		


run_game()
