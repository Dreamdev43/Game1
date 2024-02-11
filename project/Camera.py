import pygame
from Global import*
from Settings import*
from UI import Text 

class CameraTile:
    def __init__(self,tile_size,target, size):
        self.surf = pygame.display.get_surface()
        
        #CAMERA-OFSET---]
        self.offset = pygame.math.Vector2()
        self.pos = pygame.math.Vector2()
        self.w, self.h = self.surf.get_width(), self.surf.get_height()
        self.rect = pygame.Rect(0,0, size[0]*tile_size,size[1]*tile_size)
    
    def draw(self):
            pass
            #pygame.draw.rect(self.surf, ("red"), self.rect, 5)
    
    def update(self, target):
                self.offset.x = target.rect.centerx-game_screen_width//2
                self.offset.y = target.rect.centery-game_screen_height//2
                
        
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.surf = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        
    def draw(self,target,tree):
        self.offset.x = target.rect.centerx-game_screen_width//2
        self.offset.y = target.rect.centery-game_screen_height//2
        
        for layer in LAYER.values():
            for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            	if sprite.z == layer:
            		self.offset_rect = sprite.rect.copy()
            		self.offset_rect.center -= self.offset
            		self.surf.blit(sprite.image,self.offset_rect)
            		
            		if sprite == target:
            			self.player_offset_rect = target.rect.copy()
            			self.player_offset_rect.center -= self.offset
            			#pygame.draw.rect(self.surf, 'red', self.offset_rect, 5)