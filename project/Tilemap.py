import pygame
from Map import *
from Global import *
from Settings import*

class Tiles(pygame.sprite.Sprite):
    def __init__(self, image,scale,layer):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(self.width * scale), int(self.height * scale)))
        self.mask = pygame.mask.from_surface(self.image)
        self.layer = layer

Tile = []
tile_lines = []

tsize = 4
          
tile_images = {
        #GRASS-TILE---------------------]
        1: Tiles("../graphics/Tiles/grass/1.png", tsize, LAYER["GRASS"]), 2: Tiles("../graphics/Tiles/grass/2.png", tsize, LAYER["GRASS"]),
        3: Tiles("../graphics/Tiles/grass/3.png", tsize, LAYER["GRASS"]), 4: Tiles("../graphics/Tiles/grass/4.png", tsize, LAYER["GRASS"]),
        5: Tiles("../graphics/Tiles/grass/5.png", tsize, LAYER["GROUND"]), 6: Tiles("../graphics/Tiles/grass/6.png", tsize, LAYER["GROUND"]),
        7: Tiles("../graphics/Tiles/grass/7.png", tsize, LAYER["GROUND"]), 8: Tiles("../graphics/Tiles/grass/8.png", tsize, LAYER["GROUND"]),
        9: Tiles("../graphics/Tiles/grass/9.png", tsize, LAYER["GROUND"]), 10: Tiles("../graphics/Tiles/grass/10.png", tsize, LAYER["GROUND"]),
        11: Tiles("../graphics/Tiles/grass/11.png", tsize, LAYER["GROUND"]), 12: Tiles("../graphics/Tiles/grass/12.png", tsize, LAYER["GROUND"]), 
        13: Tiles("../graphics/Tiles/grass/13.png", tsize, LAYER["GROUND"]), 14: Tiles("../graphics/Tiles/grass/14.png", tsize, LAYER["GROUND"]),
        15: Tiles("../graphics/Tiles/grass/15.png", tsize, LAYER["GROUND"]), 16: Tiles("../graphics/Tiles/grass/16.png", tsize, LAYER["GROUND"]),
        17: Tiles("../graphics/Tiles/grass/17.png", tsize, LAYER["GROUND"]), 18: Tiles("../graphics/Tiles/grass/18.png", tsize, LAYER["GROUND"]),
        19: Tiles("../graphics/Tiles/grass/19.png", tsize, LAYER["GROUND"]), 20: Tiles("../graphics/Tiles/grass/20.png", tsize, LAYER["GRASS"]),
        21: Tiles("../graphics/Tiles/grass/21.png", tsize, LAYER["GRASS"]), 22: Tiles("../graphics/Tiles/grass/22.png", tsize, LAYER["GRASS"]),
        23: Tiles("../graphics/Tiles/grass/23.png", tsize, LAYER["GRASS"]), 24: Tiles("../graphics/Tiles/grass/24.png", tsize, LAYER["GROUND"]), 16: Tiles("../graphics/Tiles/grass/16.png", tsize, LAYER["GROUND"]),
        25: Tiles("../graphics/Tiles/grass/25.png", tsize, LAYER["GROUND"]), 26: Tiles("../graphics/Tiles/grass/26.png", tsize, LAYER["GROUND"]),
        27: Tiles("../graphics/Tiles/grass/27.png", tsize, LAYER["GROUND"]), 28: Tiles("../graphics/Tiles/grass/28.png", tsize, LAYER["GRASS"]),
        29: Tiles("../graphics/Tiles/grass/29.png", tsize, LAYER["HILL"]), 30: Tiles("../graphics/Tiles/grass/30.png", tsize, LAYER["GRASS"]),
        31: Tiles("../graphics/Tiles/grass/31.png", tsize, LAYER["GRASS"]),32: Tiles("../graphics/Tiles/grass/32.png", tsize, LAYER["GRASS"]), 
        33: Tiles("../graphics/Tiles/grass/33.png", tsize, LAYER["GRASS"]),34: Tiles("../graphics/Tiles/grass/34.png", tsize, LAYER["HILL"]),
        35: Tiles("../graphics/Tiles/grass/35.png", tsize, LAYER["HILL"]),36: Tiles("../graphics/Tiles/grass/36.png", tsize, LAYER["HILL"]),
        
        #FENCE-TILE----------------------]
        110: Tiles("../graphics/Tiles/fence/1.png", tsize, LAYER["OBJECT"]), 220: Tiles("../graphics/Tiles/fence/2.png", tsize, LAYER["OBJECT"]),
        330: Tiles("../graphics/Tiles/fence/3.png", tsize, LAYER["OBJECT"]), 440: Tiles("../graphics/Tiles/fence/4.png", tsize, LAYER["OBJECT"]),
        550: Tiles("../graphics/Tiles/fence/5.png", tsize, LAYER["OBJECT"]), 660: Tiles("../graphics/Tiles/fence/6.png", tsize, LAYER["OBJECT"]),
        770: Tiles("../graphics/Tiles/fence/7.png", tsize, LAYER["OBJECT"]), 880: Tiles("../graphics/Tiles/fence/8.png", tsize, LAYER["OBJECT"]),
        
        #WATER-TILE---------------------]
        100: Tiles("../graphics/Tiles/water/1.png", tsize, LAYER["WATER"]), 200: Tiles("../graphics/Tiles/water/2.png", tsize, LAYER["WATER"]),
        300: Tiles("../graphics/Tiles/water/3.png", tsize, LAYER["WATER"]), 400: Tiles("../graphics/Tiles/water/4.png", tsize, LAYER["WATER"]),
        500: Tiles("../graphics/Tiles/water/5.png", tsize, LAYER["WATER"]), 600: Tiles("../graphics/Tiles/water/6.png", tsize, LAYER["WATER"]),
        700: Tiles("../graphics/Tiles/water/7.png", tsize, LAYER["WATER"]), 800: Tiles("../graphics/Tiles/water/8.png", tsize, LAYER["WATER"]), 
        900: Tiles("../graphics/Tiles/water/9.png", tsize, LAYER["WATER"]),
        
}
    
tile_size = 64
CHUNK = 6
CHUNK_SIZE = CHUNK * tile_size
CHUNK_W, CHUNK_H = 6, 3

def draw_chunk(x, y):
    pygame.draw.rect(screen, ("green"), (x, y, CHUNK_SIZE, CHUNK_SIZE), 2)

class WorldTile:
    def __init__(self, map_data):
        self.tile_list = []
        self.offset = pygame.math.Vector2()
        
        #TILEMAP-LOGIC------]
        for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                tile_image = tile_images.get(tile)
                if tile_image:
                        self.tile_rect = tile_image.image.get_rect(bottomleft=(x * tile_size, y * tile_size))
                        tile_mask = pygame.mask.from_surface(tile_image.image)
                        tile_image_mask = tile_mask.to_surface()
                        tile_image_mask.set_colorkey((0, 0, 0))
                        self.tile = (tile_image.image, self.tile_rect, tile_image_mask, tile_mask, tile_image.layer)
                        self.tile_list.append(self.tile)
                        self.map_y = y*tile_size
                        self.map_x = x*tile_size
    
                  
                               
    # ... (dein bisheriger Code bleibt unverändert)

    # MOVE-MAP ---------------]
    def move_map(self, offset,dt):
        self.offset.x = offset[0]*dt
        self.offset.y = offset[1]*dt
        for tile in self.tile_list:
        	tile[1].move_ip(offset[0]*dt,offset[1]*dt)

    # RENDERING --------------]
    def render(self, surf, rect):
        sorted_tiles = sorted(self.tile_list, key=lambda tile: tile[4])
        for tile in sorted_tiles:
        		surf.blit(tile[0], (tile[1]))