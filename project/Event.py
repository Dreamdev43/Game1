import pygame
from Level import Level
from Settings import*
from Global import*

def MouseButtonEvent(self, event):
		if event.type==pygame.MOUSEBUTTONDOWN and self.level.showGUI:
					
			#CONTROLLER------]
			if self.level.btn2.rect.collidepoint(event.pos) and self.level.TorchControl:
				self.level.player.direction.x = -1
				self.level.camera.offset.x = -1
			elif self.level.btn1.rect.collidepoint(event.pos) and self.level.TorchControl:
			    self.level.player.direction.x = 1
			    self.level.camera.offset.x = 1
			elif self.level.btn4.rect.collidepoint(event.pos) and self.level.TorchControl:
				self.level.player.direction.y = 1
				self.level.camera.offset.y = 1
			elif self.level.btn3.rect.collidepoint(event.pos) and self.level.TorchControl:
			    self.level.player.direction.y = -1
			    self.level.camera.offset.y = -1
			
			#BUTTON-EVENT----------------------]
			if self.level.btn["btn2"].rect.collidepoint(event.pos):
			    diaDict["show_dia1"] = True
			if self.level.btn["btn1"].rect.collidepoint(event.pos):
				self.level.player.timers['tool use'].activate()
				self.direction = pygame.math.Vector2()
				self.level.player.frame_index = 0
			if self.level.selecter.rect.collidepoint(event.pos):
				self.level.player.switch_item()  
			    			    
		if event.type==pygame.MOUSEBUTTONUP and self.level.showGUI:
			if self.level.btn1.rect.collidepoint(event.pos) and self.level.TorchControl:
				self.level.player.direction.x = 0
			if self.level.btn2.rect.collidepoint(event.pos) and self.level.TorchControl:
			    self.level.player.direction.x = 0
			if self.level.btn3.rect.collidepoint(event.pos) and self.level.TorchControl:
				self.level.player.direction.y = 0
			if self.level.btn4.rect.collidepoint(event.pos) and self.level.TorchControl:
			    self.level.player.direction.y = 0

def MouseEvent(self, event):
    #PLAYER-MASK----------------]
    if event.type==pygame.MOUSEBUTTONDOWN:
        if self.level.player.collisionbox.collidepoint(event.pos):
            self.level.player.showMask = True
            self.level.tree.showMask = True
        else:
            self.level.player.showMask = False
            
        #OBJECT-MASK----------------]

def GenericEvent(self):
	if OverlayDict["show_item"]:
		self.level.overlay.draw_overlay_item()
	# OBJECT-EVENT-----------]
	for grass1 in self.level.grass.values():
	       for grass2 in self.level.grass.values():
	           if grass1 != grass2 and grass1.rect.colliderect(grass2.rect):
	           	grass1.kill()
	           	grass2.kill()

def PlayerEvent(self):
    if self.level.player.group.offset_rect.x == self.level.World.offset[0]:
        self.level.player.group.offset_rect.x = self.level.World.offset[0]

def TileEvent(self,dt):
    #HORIZONTICAL-DIRECTION-----------]
    if self.level.player.direction.x== -1:
       self.level.World.move_map((self.level.player.speed,0),dt)
    elif self.level.player.direction.x== 1:
       self.level.World.move_map((-self.level.player.speed,0),dt)       

    #VERTICAL-DIRECTION-----------]
    if self.level.player.direction.y == -1:
       self.level.World.move_map((0,self.level.player.speed),dt)
    if self.level.player.direction.y == 1:
       self.level.World.move_map((0,-self.level.player.speed),dt)
       
    #TILE-COLLISION-----------------]
    """"""""""""""""""
            
#DIALOUGE-EVENTHANDLER-------------------------------------------]
def DiaEvent(self,event):
	#DIA1-EVENT----------------------------]
	if event.type==pygame.MOUSEBUTTONDOWN and self.level.showGUI:
		
		if diaDict["show_dia1"] == True:
			if self.level.dia1["btn"].rect.collidepoint(event.pos):
				diaDict["show_dia1"], FaceDict["face1"] = False,False
			if self.level.dia1["btn1"].rect.collidepoint(event.pos):
				FaceDict["face1"] = True
				
def FaceEvent(self,event):
	#FACE1-EVENT--------------------------]
	if event.type==pygame.MOUSEBUTTONDOWN and self.level.showGUI:
		
		if FaceDict["face1"] == True:
			if self.level.face1["dia1"].rect.collidepoint(event.pos):
				if "wood" in self.level.player.inventory:
					if self.level.player.inventory["wood"] >= 2:
						self.level.player.inventory["wood"] -= 2
						self.level.player.add_item("plank", 4)

		if FaceDict["face1"] == True:
			if self.level.face1["dia2"].rect.collidepoint(event.pos):
				if "plank" in self.level.player.inventory:
					if self.level.player.inventory["plank"] >= 12:
						self.level.player.inventory["plank"] -= 12
						self.level.player.add_item("crate", 2)		