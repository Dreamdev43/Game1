import pygame
from os import walk

def import_folder(path, scale):
	 surface_list = []
	
	 for _, __, img_files in walk(path):
		 for image in img_files:
			 full_path = path + '/' + image
			 image_surf = pygame.image.load(full_path).convert_alpha()
			 width = image_surf.get_width()
			 height = image_surf.get_height()
			 image_surf = pygame.transform.scale(image_surf, (int(width * scale), int(height * scale)))
			 surface_list.append(image_surf)
	 return surface_list