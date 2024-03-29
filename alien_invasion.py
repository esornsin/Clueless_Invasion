import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    a1_settings = Settings()
    screen = pygame.display.set_mode(
        (a1_settings.screen_width, a1_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make the Play button.
    play_button = Button(a1_settings, screen, "As If!")
    
    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(a1_settings)
    sb = Scoreboard(a1_settings, screen, stats)
    
    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(a1_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # Create a fleet of aliens.
    gf.create_fleet(a1_settings, screen, ship, aliens)
    
    # Start the main loop for the game.
    while True:
        gf.check_events(a1_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:    
            ship.update()
            gf.update_bullets(a1_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(a1_settings, screen, stats, sb, ship, aliens, bullets)
            
        gf.update_screen(a1_settings, screen, stats, sb, ship, aliens, bullets, play_button)
       
        
run_game()