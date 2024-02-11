import pygame
from Global import *
from Item import Item

class Overlay:
    def __init__(self, player):
        # general setup
        self.display = pygame.display.get_surface()
        self.player = player

        # INVENTORY_ITEMS------------]
        path = "../graphics/item/"
        self.item_surf = {item: Item(ScreenSizes["bottomright"][0] - 100, ScreenSizes["bottomright"][1] - 100,
                                     f"{path}{item}.png", 6) for item in player.items}
       
        # OVERLAY_ITEMS------------]
        overlay_path = "../graphics/item/"
        self.overlay_item_surf = {item: Item(self.player.collisionbox.x+25, self.player.collisionbox.y-20,
                                     f"{path}{item}.png", 2) for item in Overlay_items}
       
    def draw_item(self):
        item_surf = self.item_surf[self.player.selected_item]
        item_surf.outline(screen)
        self.display.blit(item_surf.image, item_surf.rect)
    
    def draw_overlay_item(self):
    	self.overlay_surf = self.overlay_item_surf[Overlay_selected_item]
    	self.display.blit(self.overlay_surf.image,self.overlay_surf.rect)

    def update(self):
        self.overlay_surf = self.overlay_item_surf[Overlay_selected_item]
        #self.overlay_surf.rect.x += 1