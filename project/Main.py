import pygame, sys
from Level import Level
from Settings import *
from Event import *
from UI import Text,debug,PlayMusic
from Global import*

class Game:
      def __init__(self):
            pygame.init()
            self.screen = screen
            self.clock = pygame.time.Clock()
            self.level = Level()
            
       
      def Run(self):
             self.run = True
             while self.run:
                   #FILLING-SCREEN----]
                   self.screen.fill((255, 255, 0))
                   self.dt = self.clock.tick() / 1000
                   
                   #RENDERING LEVEL--]
                   self.level.run(self.dt)
                   
                   for event in pygame.event.get():
                         #EVENTHANDLER----]
                         MouseButtonEvent(self,event)
                         DiaEvent(self,event)
                         FaceEvent(self,event)
                         MouseEvent(self,event)
                         
                         if event.type == pygame.QUIT or self.run == False:
                               pygame.quit()
                               sys.exit()
                   
                   GenericEvent(self)
                   TileEvent(self,self.dt)
                   #self.level.tree.health -= 1
                   #self.text_l = Text(ScreenSizes["center"][0], ScreenSizes["center"][1]-260,"Font2", 32, f"v: {self.level.tree.showMask}", ("blue"), self.screen)
                   #debug(f"{self.level.object_overlay.pos},{self.level.player.inventory}",self.screen)
                   pygame.display.flip()
                    
if __name__ == "__main__":
    game = Game()
    game.Run()
    