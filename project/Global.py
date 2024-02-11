import pygame
from Settings import *
from Camera import CameraGroup

pygame.init()

#[------------------------------virable-----------------------------------]
diaDict={"show_dia1": False, "show_dia2": False, "show_dia3": False,
                 "show_dia4": False, "show_dia5": False, "show_dia6": False}
FaceDict={"face1": False}
                                              
#[---------screen------------]
ScreenSizes={"center": (game_screen_width // 2, game_screen_height // 2),"bottommid": (screen_rect.midbottom),
                         "topleft": (screen_rect.topleft), "topright": (screen_rect.topright), "bottomright": (screen_rect.bottomright), 
                         "bottomleft": (screen_rect.bottomleft)}

Group={"UI_GROUP": pygame.sprite.Group(), "MENU_UI_GROUP": pygame.sprite.Group(), "FACE_UI_GROUP": pygame.sprite.Group(),
              "TILE": pygame.sprite.Group(), "SPRITE": pygame.sprite.Group(), "OBJECT": pygame.sprite.Group(),
              "COLLISION": pygame.sprite.Group(), "DIA_GROUP": pygame.sprite.Group(),"TREE": pygame.sprite.Group()}
              
CameraGroup={"SPRITES": CameraGroup()}

Price = {"planks": 2,"crate": 12}

Placement = False 

Overlay_items = ["wood"]
Overlay_selected_item = "wood"
OverlayDict = {"show_item": False}