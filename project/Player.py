import pygame
from Support import import_folder
from Settings import*
from Global import *
from Timer import Timer

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, group, collision_group,tree_sprites, scale):
		super().__init__(group)
		
		#SETUP--------------]
		self.scale = scale
		self.x, self.y = x, y
		self.graphics()
		self.group = group
		
		#LAYER--------------]
		self.z = LAYER["MAIN"]
		
		#FRAME-STATE------]
		self.status = "left_idle"
		self.frame_index = 0
		self.animation_speed = 4
		
		#IMAGE---------------]
		self.image = self.animations[self.status][self.frame_index]
		self.rect = self.image.get_rect(center = (x, y))
		self.hitbox = self.rect.copy().inflate((0,-32))
		
		#COLIDE-BOX--------]
		self.collisionbox = self.rect.copy()
		
		#MASK---------------]
		self.showMask = False
		
		#MOVEMENT---------]
		self.direction = pygame.math.Vector2()
		self.pos = pygame.math.Vector2(self.rect.center)
		self.speed = 200
		
		#INVENTORY--------]
		self.inventory = {"watering can": 1,"axe": 1,"hoe": 1, "pickaxe": 1}
		self.items = ["axe"]
		self.update_inventory()		
		self.item_index = 0
		self.selected_item = self.items[self.item_index]
		
		#INTERACTON-----]
		self.tree_sprites = tree_sprites
		
		#COLLISION--------]
		self.collision_sprites = collision_group
		self.direction_v_x = False
		self.direction_v_y = False
		
		#TIMERS-----------]
		self.timers = {
		       "tool use": Timer(605, self.use_tool)
		}
		
		
	#OUTLINE----------------------------]
	def outline(self, surf):
	   	surf.blit(self.mask_image, self.collisionbox)
	   	
	   	for point in self.mask.outline():
	   	   x = point[0]-2.5+ self.group.player_offset_rect[0]
	   	   y = point[1]-2.5+ self.group.player_offset_rect[1]
	   	   rect = pygame.Rect(x, y, self.scale+4, self.scale+4)
	   	   pygame.draw.rect(surf, ("white"), rect)
	
	#ADD_ITEMS-----------------]	
	def add_item(self,item,amount):
	    if item not in self.inventory:
	        self.inventory[item] = amount
	    elif item in self.inventory:
	        if self.inventory[item] <= 75:
	            self.inventory[item] += amount
	        else:
	            if self.inventory[item] >= 75:
	                index = 2
	            self.inventory[f"{item}{index}"] = amount
	
	#USE_TOOL------]
	def use_tool(self):
	    if self.selected_item == "axe":
	    	for tree in self.tree_sprites.sprites():
	    		if tree.rect.collidepoint(self.target_pos):
	    			tree.kill()
	
	#GET_TARGET_POS-]
	def get_target_pos(self):
		self.target_pos= self.rect.center + TOOL_OFFSET[self.status.split('_')[0]]
	
	#SWITCH-ITEM------]
	def switch_item(self):
		self.item_index += 1
		self.item_index = self.item_index if self.item_index < len(self.items) else 0
		self.selected_item = self.items[self.item_index]		
	
	#GET_STATUS------]
	def get_status(self):
	       #IDLE1-CHECKER----------]
	       if self.direction.magnitude() == 0:
	           self.status = self.status.split('_')[0] + '_idle'
	       else:
	           if self.direction.x == 1:
	               self.status = 'right'
	           if self.direction.x == -1:
	               self.status = 'left'
	           #elif self.direction.y > 0:
	               #self.status = 'down'
#	           elif self.direction.y < 0:
#	               self.status = 'up'

	       #TOOL-CHECKER-----------]
	       if self.selected_item == "axe":
	             if self.timers['tool use'].active:
	             	self.status = self.status.split('_')[0] + '_' + self.selected_item	           	       
	        
#	       #IDLE-CHECKER-----------]     		       
#	       if self.direction.magnitude() == 0 and self.showMask == False:
#	           self.status = self.status.split('_')[0] + '_idle'

	       	           
	             	           

	#GRAPHICS-------------------------]	
	def graphics(self):
	    self.animations = {'left': [], 'right': [],'right_idle': [], 'left_idle': [],
	                                   'right_idle_1': [], 'left_idle_1': [], 'left_axe': [],
	                                   'right_axe': []
	    }
	    for animation in self.animations.keys():
	           full_path = '../graphics/player/' + animation
	           self.animations[animation] = import_folder(full_path, self.scale)
	           
	def animate(self,dt):
	       self.frame_index += self.animation_speed *dt
	       if self.frame_index >= len(self.animations[self.status]):
	           self.frame_index = 0
	       
	       self.image = self.animations[self.status][int(self.frame_index)]
	       self.mask = pygame.mask.from_surface(self.image)
	       self.mask_image = self.mask.to_surface()
	       self.mask_image.set_colorkey((0,0,0))
        
    
	def Keyinput(self):
		key = pygame.key.get_pressed()
		
		#DIRECTIONS------------]
		if not self.timers['tool use'].active:
			if key[pygame.K_UP]:
			    self.direction.y = -1
			elif key[pygame.K_DOWN]:
			    self.direction.y = 1
			else:
			   self.direction.y = 0
			if key[pygame.K_LEFT]:
			   self.direction.x = -1
			   self.status = 'left'
			elif key[pygame.K_RIGHT]:
			   self.direction.x = 1
			   self.status = 'right'
			else:
			   self.direction.x = 0
			#TOOL-USE---------]
			if key[pygame.K_e]:
			    self.timers['tool use'].activate()
			    self.direction = pygame.math.Vector2()
			    self.frame_index = 0
			
			#TOOL-SWITCH----]
			if key[pygame.K_i]:
				self.item_index += 1
				self.item_index = self.item_index if self.item_index < len(self.items) else 0
				self.selected_item = self.items[self.item_index]
				
				
				
			
	def move(self,dt):
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()
			
		self.pos.x += self.direction.x * self.speed*dt
		self.hitbox.centerx = round(self.pos.x)
		self.rect.centerx = self.hitbox.centerx
		self.collision("horizontal")
		
		
		self.pos.y += self.direction.y * self.speed*dt
		self.hitbox.centery = round(self.pos.y)
		self.rect.centery = self.hitbox.centery
		self.collision("vertical")
	
	def collision(self, direction):
	    #TILE-COLLISION---------]
	    
	    #HITBOX-COLLISION-----]
	    for sprite in self.collision_sprites.sprites():
	         if hasattr(sprite, 'hitbox'):
	            if sprite.hitbox.colliderect(self.hitbox):
	               self.direction_v_x = True
	               if direction == "horizontal":
	                   if self.direction.x > 0:
	                       self.hitbox.right = sprite.hitbox.left
	                   if self.direction.x < 0:
	                       self.hitbox.left = sprite.hitbox.right
	                   self.rect.centerx = self.hitbox.centerx
	                   self.pos.x = self.hitbox.centerx
	               if direction == "vertical":
	                   if self.direction.y > 0:
	                       self.hitbox.bottom = sprite.hitbox.top
	                   if self.direction.y < 0:
	                       self.hitbox.top = sprite.hitbox.bottom
	                   self.rect.centery = self.hitbox.centery
	                   self.pos.y = self.hitbox.centery
	                   	                 
	def update_timers(self):
	    for timers in self.timers.values():
	        timers.update()
	 
	def update_inventory(self):
	    for items in self.inventory.keys():
	    	self.items.append(items)
	
	def update_collisionbox(self):
		self.collisionbox = self.group.player_offset_rect
	
	    
	def update(self,dt):
		#self.Keyinput()				
		self.get_status()		
		self.move(dt)
		self.animate(dt)
		
		self.update_collisionbox()
		self.update_timers()
		self.get_target_pos()
		
		#pygame.draw.rect(screen,("blue"), self.rect, 1)