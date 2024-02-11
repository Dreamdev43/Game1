import pygame 

class Item:
	def __init__(self, x, y, image, scale):
	       self.image = pygame.image.load(image).convert_alpha()
	       self.width = self.image.get_width()
	       self.height = self.image.get_height()
	       self.image = pygame.transform.scale(self.image, (int(self.width * scale), int(self.height * scale)))
	       self.rect = self.image.get_rect(center=(x, y))
	       self.offset = pygame.math.Vector2()
	       self.item = 0
	       self.scale = scale
	       
	       #MASK----]
	       self.mask = pygame.mask.from_surface(self.image)
	       self.mask_image = self.mask.to_surface()
	       self.mask_image.set_colorkey((0,0,0))
	 
	def draw(self,surf,outline=False):
		surf.blit(self.image,self.rect)
		
	#OUTLINE----] 
	def outline(self, surf):
	   	surf.blit(self.mask_image, self.rect)
	   	
	   	for point in self.mask.outline():
	   	   x = point[0]-4+ self.rect.x
	   	   y = point[1]-4+ self.rect.y
	   	   rect = pygame.Rect(x, y, self.scale+3, self.scale+3)
	   	   pygame.draw.rect(surf, ("white"), rect)
		