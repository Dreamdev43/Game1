import pygame
from Global import*

class Object(pygame.sprite.Sprite):
    def __init__(self,image,pos,group,scale,z = LAYER["MAIN"]):
        super().__init__(group)
        self.damage = 5
        self.group = group
        self.showMask = False
        self.scale = scale
        self.z = z
        
        #IMAGE---------------]
        self.image = pygame.image.load(image).convert_alpha()
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(self.width * scale), int(self.height * scale)))
        
        #RECT----------------]
        self.rect = self.image.get_rect(topleft= pos)
        self.hitbox = self.rect.copy().inflate((-6,-6))
        
        #MASK----------------]
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_image = self.mask.to_surface()
        self.mask_image.set_colorkey((0,0,0)) 
        
     
    def kill(self):
        super().kill()
        
    #OUTLINE----------------------------]
    def outline(self, surf):
	   	surf.blit(self.mask_image, self.group[0].offset_rect)
	   	
	   	for point in self.mask.outline():
	   	   x = point[0]-2.5+ self.rect[0]
	   	   y = point[1]-2.5+ self.rect[1]
	   	   rect = pygame.Rect(x, y, self.scale+3, self.scale+3)
	   	   pygame.draw.rect(surf, ("white"), rect)
    
    def draw(self,surf):
    	surf.blit(self.image,self.rect)