import pygame
from .buttons import *

pygame.init()

HOMEWIDTH = 650
HOMEHEIGHT = 650
logged_in = False
home_page_running = True
game_running = False
display_surface = pygame.display.set_mode((HOMEWIDTH, HOMEHEIGHT))
pygame.display.set_caption('Bach-man: HomePage')
font = pygame.font.SysFont('Comic Sans MS', 32)
play_img = pygame.image.load('assets/Play_button.png').convert_alpha()
highscore_img = pygame.image.load('assets/Highscore_button.png').convert_alpha()
background_img = pygame.transform.scale(pygame.image.load('assets/Home_design.png').convert_alpha(),(HOMEWIDTH,HOMEHEIGHT))

play_button = Button((HOMEWIDTH//2),((4 * HOMEHEIGHT)//6),play_img,0.5)
highscore_button = Button((HOMEWIDTH//2),((5 * HOMEHEIGHT)//6),highscore_img,0.4)
background_rect = background_img.get_rect()
