import pygame
from Settings import *
from Object import Object
from Global import *

class ObjectOverlay:
    def __init__(self, player, z=LAYER["OBJECT"]):
        self.tilesize = 48
        self.player = player
        self.objects = []  # Liste, um die platzierten Objekte zu speichern
        self.offset = pygame.math.Vector2()
        self.test = False

    def draw_grid(self, width, height, tilesize, screen):
        for x in range(0, width, self.tilesize):
            pygame.draw.line(screen, "white", (x, 0), (x, height))
        for y in range(0, height, self.tilesize):
            pygame.draw.line(screen, "white", (0, self.offset.y+y), (width, y))

    def place_object(self, selected_object):
        self.offset.x -= CameraGroup["SPRITES"].offset.x
        self.pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            self.grid_x = self.pos[0] // self.tilesize
            self.grid_y = self.pos[1] // self.tilesize
            if selected_object in self.player.inventory:
                if self.player.inventory[selected_object] > 0:
                    # Überprüfen, ob die Kachel bereits besetzt ist
                    if not self.is_tile_occupied(self.grid_x, self.grid_y):
                        self.player.inventory[selected_object] -= 1
                        self.test = True
                        self.obj = Object(f"../graphics/object/tile/{selected_object}.png", (self.grid_x*self.tilesize, self.grid_y*self.tilesize), [CameraGroup["SPRITES"],Group["COLLISION"]], 3)
                        self.objects.append(self.obj)
                        

    def is_tile_occupied(self, x, y):
        # Überprüfen, ob die Kachel besetzt ist
        for obj in self.objects:
            if obj.rect.x == x * self.tilesize and obj.rect.y == y * self.tilesize:
                return True
        return False
    
    