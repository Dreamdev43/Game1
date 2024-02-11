import pygame
from Tilemap import WorldTile, tile_size, tsize
from Map import *
from Global import *
from UI import UI,randomly,Text
from Settings import*
from Player import Player
from Camera import CameraTile
from Sprite import Tree,Grass
from random import randint
from overlay import  Overlay
from Object import Object
from Interaction import ObjectOverlay
from Item import Item


class Level():
	def __init__(self):
		self.surface = pygame.display.get_surface()
		self.showGUI = True
		self.GuiSize = 4				
		
		#TILMAP------]
		self.World = WorldTile(terrain1)
		
		#CONTROLL----]
		self.TorchControl = True
		
		#SPRITESS------]
		self.player = Player(ScreenSizes["center"][0], ScreenSizes["center"][1], CameraGroup["SPRITES"],Group["COLLISION"],Group["TREE"], tsize)
		self.overlay = Overlay(self.player)
		
		#INTERACTION]
		self.object_overlay = ObjectOverlay(self.player)
		
		#CAMERA------]
		self.camera = CameraTile(tile_size,self.player,(30, 22))
		self.selecter = UI("../graphics/item/selecter.png",ScreenSizes["bottomright"][0] - 45, ScreenSizes["bottomright"][1] - 100, self.GuiSize+2, Group["UI_GROUP"])
		
		self.test = pygame.Rect(self.player.x+TOOL_OFFSET["left"][0], self.player.y+TOOL_OFFSET["left"][1], 20, 20)
		
		#UI-------------]
		self.btn = {"btn1": UI("../graphics/UI/UI/btn1.png", 12*self.GuiSize,12*self.GuiSize, self.GuiSize, Group["UI_GROUP"]),
		                  "btn2": UI("../graphics/UI/UI/btn2.png", 28*self.GuiSize,10*self.GuiSize, self.GuiSize, Group["UI_GROUP"])}
		
		
		self.dia1 = {"dia": UI("../graphics/UI/UI/dia/dia1/dia1.png", ScreenSizes["center"][0], ScreenSizes["center"][1]-32, self.GuiSize, Group["DIA_GROUP"]),
		                    "btn": UI("../graphics/UI/UI/dia/dia1/btn1.png", ScreenSizes["center"][0]+354, ScreenSizes["center"][1]-258, self.GuiSize, Group["DIA_GROUP"]),
		                    "btn1": UI("../graphics/UI/UI/dia/dia1/btn2.png", ScreenSizes["center"][0]-340, ScreenSizes["center"][1]-244, self.GuiSize, Group["DIA_GROUP"])}
		
		                   
		self.face1 = {"dia1": UI("../graphics/UI/UI/dia/dia1/face1/1.png", 470, 250, self.GuiSize, Group["FACE_UI_GROUP"]),
		                      "dia2": UI("../graphics/UI/UI/dia/dia1/face1/1.png", 470, 320, self.GuiSize, Group["FACE_UI_GROUP"])}
		
		self.items1 = {"1": Item(330,250,"../graphics/item/wood.png",3),"2": Item(600,250,"../graphics/item/plank.png",3),
		                         "3": Item(330,320,"../graphics/item/plank.png",3),"4": Item(600,320,"../graphics/item/crate.png",3)}
		
		self.Text = {"planks": Text(470, 250,"Font2", 34, f"{Price['planks']}x", "white", self.surface),
		                    "crate": Text(470, 320,"Font2", 34, f"{Price['crate']}x", "white", self.surface)}
		
		#OBJECTS----------]
		for i in range(10):
			self.tree = Tree( "../graphics/object/tree.png",(randomly(4*tile_size,51*tile_size,4*tile_size,27*tile_size)),[CameraGroup["SPRITES"],Group["COLLISION"], Group["TREE"]], tsize,self.player)
		
		#RANDOM FLOWER-]
		for i in range(10):
			self.flowers = {"1":Grass( "../graphics/object/grass/4.png",(randomly(7*tile_size,49*tile_size,7*tile_size,26*tile_size)),CameraGroup["SPRITES"], tsize),
			                            }
			
		
		#RANDOM-GRASS--]
		self.grass_list = []
		for i in range(50):
		    r_x = randint(1*tile_size, 53*tile_size)
		    r_y = randint(1*tile_size, 53*tile_size)
		    if r_x >= 0 and r_x <= self.World.map_x and r_y >= 0 and r_y <= self.World.map_y-tile_size:
		        self.grass = {"1":Grass( "../graphics/object/grass/0.png",(r_x, r_y),CameraGroup["SPRITES"], tsize),
		                              "2":Grass( "../graphics/object/grass/1.png",(r_x+tile_size,r_y+tile_size),CameraGroup["SPRITES"], tsize),
		                              "3":Grass( "../graphics/object/grass/2.png",(randomly(2*tile_size,51*tile_size,2*tile_size,26*tile_size)),CameraGroup["SPRITES"], tsize),		                              "4":Grass( "../graphics/object/grass/8.png",(randomly(3*tile_size,51*tile_size,3*tile_size,26*tile_size)),CameraGroup["SPRITES"], tsize)
		        }
		self.grass_list.append(self.grass)
		  		    	    
		#MOUSE-------------]
		self.mouse_scale = 2
		self.cursor = pygame.image.load("../graphics/Mouse/0.png").convert_alpha()
		self.cursor = pygame.transform.scale(self.cursor,(24, 36))
		pygame.mouse.set_visible(False)
		
		#DRAW-CONTROLL--]
		if self.TorchControl == True:
		    self.Controller()
	#CONTROLLER-]
	def Controller(self):
		self.btn1 = UI("../graphics/UI/Controller/1.png", 300, 650, 8, Group["UI_GROUP"])
		self.btn2 = UI("../graphics/UI/Controller/2.png", 100, 650, 8, Group["UI_GROUP"])
		self.btn3 = UI("../graphics/UI/Controller/3.png", 200, 578, 8, Group["UI_GROUP"])
		self.btn4 = UI("../graphics/UI/Controller/4.png", 200, 650, 8, Group["UI_GROUP"])
	
	def draw_dia(self):
		if diaDict["show_dia1"] == True:
			 for dia in self.dia1.keys():
			 		self.dia1[dia].draw(self.surface, False)
	
	def draw_item_ui(self):
		for item in self.items1.keys():
			self.items1[item].draw(self.surface, False)
		self.Text["planks"].draw(self.surface)
		self.Text["crate"].draw(self.surface)
	
	def draw_face(self):
		if FaceDict["face1"] == True:
			for Face in self.face1.keys():
				self.face1[Face].draw(self.surface, False)
			self.draw_item_ui()
						
	def run(self,dt):
		self.Pos = pygame.mouse.get_pos()
		#RENDER TILMAP-----]
		self.World.render(self.surface, self.player.rect)
		#self.World.move_map((0, 0))
		
		#PLAYER-RENDER----]
		if self.player.showMask:
		    self.player.outline(self.surface)
		    		    
		CameraGroup["SPRITES"].draw(self.player,self.tree)
		CameraGroup["SPRITES"].update(dt)		
		#OBJECT-RENDER---]
		#pygame.draw.rect(self.surface, ("blue"), self.test)
				
								
		#RENDER-CAMERA--]
		self.camera.draw()
		self.camera.update(self.player)
		#RENDER-UI-----------]
		
		Group["UI_GROUP"].draw(self.surface)
		if Placement:
			self.object_overlay.draw_grid(self.World.map_x, self.World.map_y,tile_size,self.surface)
		if diaDict["show_dia1"] == False:
			self.object_overlay.place_object("crate")
		self.draw_dia()
		self.draw_face()
		self.overlay.draw_item()
		#self.overlay.draw_overlay_item()
		self.overlay.update()
		self.surface.blit(self.cursor, (self.Pos[0], self.Pos[1]))