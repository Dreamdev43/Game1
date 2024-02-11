import pygame
from Settings import*
from Timer import Timer
from random import choice
from Global import*
import random

#GENERIC------------------------]
class Generic(pygame.sprite.Sprite):
	def __init__(self,img,pos,groups,scale,z = LAYER["MAIN"]):
		super().__init__(groups)
		#IMAGE-----------------]
		self.image = pygame.image.load(img).convert_alpha()
		self.width, self.height = self.image.get_width(), self.image.get_height()
		
		#SCALING--------------]
		self.image=pygame.transform.scale(self.image,(int(self.width*scale),int(self.height*scale)))
		
		#RECT-------------------]
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.copy().inflate((-128,-96))
		self.z = z
		

#TREE-----------------------------]
class Tree(Generic):
    def __init__(self, img, pos, groups, scale,target):
        super().__init__(img,pos,groups,scale)
        self.surf = pygame.display.get_surface()
        self.group = groups
        self.scale = scale
        self.health = 5
        self.alive = True
        self.showMask = False
        self.invul_Timer = Timer(200)
        self.item_timer = Timer(700)
        self.target = target
                
        #IMAGE-----------------]
        self.image = pygame.image.load(img).convert_alpha()
        self.width, self.height = self.image.get_width(), self.image.get_height()
        
        #SCALING--------------]
        self.image=pygame.transform.scale(self.image,(int(self.width*scale),int(self.height*scale)))
                
        #RECT-------------------]
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.copy().inflate((-128,-96))
        self.collisionbox = self.rect.copy()
        
        #MASK------------------]
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_image = self.mask.to_surface()
        self.mask_image.set_colorkey((0,0,0))
        
    def kill(self):
        self.health -= 1
        
    def check_death(self,target):
    	if self.health <= 0:
    		self.alive = False
    		self.r_a = choice((10,20))
    		super().kill()
    		target.add_item("wood", self.r_a)
    		Overlay_selected_item = "wood"
    
    #OUTLINE----------------------------]
    def outline(self, surf):
    	surf.blit(self.mask_image, self.group[0].offset_rect)
    	for point in self.mask.outline():
	   	   x = point[0]-2.5+ self.group[0].offset_rect[0]
	   	   y = point[1]-2.5+ self.group[0].offset_rect[1]
	   	   rect = pygame.Rect(x, y, self.scale+3, self.scale+3)
	   	   pygame.draw.rect(surf, ("white"), rect)	
    	
    
    
    def update(self,dt):
    	self.check_death(self.target)
    	self.item_timer.update()
	
#Grass-----------------------------]
class Grass(Generic):
    def __init__(self, img, pos, group, scale):
        super().__init__(img,pos,group,scale)
        self.group = group
        self.scale = scale
        self.health = 5
        self.showMask = False
                
        #IMAGE-----------------]
        self.image = pygame.image.load(img).convert_alpha()
        self.width, self.height = self.image.get_width(), self.image.get_height()
        
        #SCALING--------------]
        self.image=pygame.transform.scale(self.image,(int(self.width*scale),int(self.height*scale)))
                
        #RECT-------------------]
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.copy().inflate((-128,-96))
        
        #MASK------------------]
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_image = self.mask.to_surface()
        self.mask_image.set_colorkey((0,0,0))
        
    def kill(self):
    	super().kill()
    	
    	
    	
#PARTICLES-----------------------]
class LeafParticle(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__()
        self.image = pygame.Surface((random.randint(5, 10), random.randint(5, 10)))
        self.image.fill((random.randint(50, 100), random.randint(100, 255), random.randint(50, 100)))  # Grüntöne
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity_x = random.uniform(-0.5, 0.5)
        self.velocity_y = random.uniform(1, 3)
        self.group = group
        self.z = LAYER["MAIN"]

    def update(self,dt):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        self.rect.width -= 0.05

        if self.rect.y > 600 or self.rect.width <= 0:
            self.kill()

    def kill(self):
        self.group.remove(self)
        super().kill()
    
    def draw(self,surf):
    	surf.blit(self.image,self.rect)
    	
class Effect(pygame.sprite.Sprite):
	def __init__(self,x, y, path, size, group, speed, index):
		pygame.sprite.Sprite.__init__(self)
		super().__init__(group)
		self.images = []
		self.speed = speed
		for num in range(0, index):
		  	IMG = pygame.image.load(f"../graphics/particle/{path}/{num}.png").convert_alpha()
		  	IMG = pygame.transform.scale(IMG, (size))
		  	self.images.append(IMG)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect(center = (x,y))
		self.counter = 0
		
	def update(self):
	 	speed = self.speed
	 	self.counter += 1
	 	
	 	if self.counter >= speed and self.index < len(self.images) -1:
	 		self.counter = 0
	 		self.index += 1
	 		self.image = self.images[self.index]
	 		
	 	if self.index >= len(self.images) - 1 and self.counter >= speed:
	 		self.kill()    	