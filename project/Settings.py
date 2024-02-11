import pygame
from pygame.math import Vector2
from UI import PlayMusic
from random import choice

# Bildschirmgröße
pygame.init()
game_screen_info = pygame.display.Info()
game_screen_width = 1280#game_screen_info.current_w
game_screen_height = 800#game_screen_info.current_h
screen = pygame.display.set_mode((game_screen_width, game_screen_height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RLEACCEL)
pygame.display.set_caption("EvergreenMeadows V1.0")
screen_rect = screen.get_rect()

LAYER ={"GROUND": 0,
               "WATER": 1,
               "GRASS": 2,
               "HILL": 3,
               "OBJECT": 4,
               "MAIN": 5
               }

TOOL_OFFSET = {"left": Vector2(-40,0),
                              "right": Vector2(20,0),
                            }
                            
#MUSIC----------]
random = choice((0,1))
PlayMusic(random)