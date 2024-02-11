#pylint:disable=C0304
import pygame
import os
from os import walk
import random

pygame.init()

class UI(pygame.sprite.Sprite):   
    def __init__(self, image_filename, x, y, scale, group):
        super().__init__(group)
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(self.width * scale), int(self.height * scale)))
        self.rect = self.image.get_rect(center=(x, y))
        self.clicked = False
        self.offset = pygame.math.Vector2()
        
    def Event(self):
        action = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True 
                
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
               
        return action
        
    def draw(self, surface,draw_rect=True):
        surface.blit(self.image, self.rect)
        if draw_rect:
            pygame.draw.rect(surface, (255, 255, 255), self.rect, 5)
                
            
    #schreiben(wen du vergessen hast :)
    #b1 = UI("game/graphics/button/menu_button.png", 0, 0, 1)
    #b1.draw(game_screen, False)
    
    #b2 = UI("game/graphics/button/map_button.png", game_screen_width // 1.071, 0, 1)
    #b2.draw(game_screen, False)

    #b3 = UI("game/graphics/button/post_button.png", game_screen_width // 1.071, 100, 1)
    #b3.draw(game_screen, False)
    
          
                
                      
                            
                                  
class Text:
    def __init__(self, x, y, Font, size, text, color, surf):
        Font = f"../graphics/Font/{Font}.ttf"
        font_size = size
        font = pygame.font.Font(Font, font_size)
        self.text_surface = font.render(text, True, color)
        self.rect = self.text_surface.get_rect(center = (x, y))
        surf.blit(self.text_surface, self.rect)
        
    def draw(self,surf):
    	surf.blit(self.text_surface,self.rect)


class DiaText:
    def __init__(self, x, y, Font, size, text, color):
        Font = f"../graphics/Font/{Font}.ttf"
        font_size = size
        font = pygame.font.Font(Font, font_size)
        self.text_surface = font.render(text, True, color)
        self.rect = self.text_surface.get_rect(center = (x, y))
        
    def draw(self, surf):
        surf.blit(self.text_surface, self.rect)





def CreateFile(name):
	file = f"{name}"
	os.makedirs(file, exist_ok=True)
	
def CreateData(name, path):
	with open(f"{name}.txt", "w") as Data:
		Data.write("hey")
		

def list_and_count_folders_in_path(path):
    folders = []
    for _, dirs, _ in walk(path):
        folders.extend(dirs)
    return len(folders), folders

# Beispielaufruf
#folderpath = "../../Android/data/com.EscapeArena"
#folder_count, folder_names = list_and_count_folders_in_path(folderpath)

#print(f"Anzahl der Ordner in {folderpath}: {folder_count}")

#for i in range(folder_count):
	#print("ball")

#for folder in folder_names:
    #print(folder)	
	
def PlayMusic(index):
	musik_list = [f"../Audio/Music/{index}.mp3"]
	
	music= pygame.mixer.Sound(musik_list[0])
	music.play(1)
	

def PlaySound(index, loop, volume, Stop=False):
	musik_list = [f"../Audio/sound/{index}.mp3"]
		
	music= pygame.mixer.Sound(musik_list[0])
	music.play(loop)
	
	music.set_volume(volume)
	
	
	if Stop == True:
		music.stop()

def PlayVoice(index, loop, Stop=False):
	musik_list = [f"../Audio/voice/{index}.mp3"]
		
	music= pygame.mixer.Sound(musik_list[0])
	music.play(loop)
	

def blend_of(surf, speed):
	alpha = 0
	surf.set_alpha(alpha)
	alpha += speed

def randomly(x1, x2, y1, y2):
    random_x = random.randint(x1, x2)
    random_y = random.randint(y1, y2)
    return random_x, random_y
            
def debug(text,surf):
        font = f"../graphics/Font/Font2.ttf"
        font_size = 20
        font = pygame.font.Font(font, font_size)
        text_surface = font.render(text, True, ("red"))
        rect = text_surface.get_rect(topleft = (0, 0))
        surf.blit(text_surface, rect)