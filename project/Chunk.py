import pygame
import sys

class Chunk():
    def __init__(self, Pos, length, pixelsize, chunksize, target):
        self.pixelsize = pixelsize
        self.chunksize = chunksize
        self.Pos = Pos
        self.length = length
        self.list = []
        self.player_chunk_x = target.x // self.pixelsize * self.pixelsize
        self.player_chunk_y = target.y // self.pixelsize * self.pixelsize

    def load(self):
        for x in range(self.length[0]):
            for y in range(self.length[1]):
                self.chunk_x = x * self.pixelsize
                self.chunk_y = y * self.pixelsize
                self.rect = pygame.Rect(self.chunk_x, self.chunk_y, self.chunksize * self.pixelsize, self.chunksize * self.pixelsize)
                self.list.append(self.rect)

    def remove_chunks_behind_player(self, player_rect):
        self.list = [rect for rect in self.list if rect.x + rect.width > player_rect.x]

    def draw(self, surf, target):
        for rect in self.list:
            pygame.draw.rect(surf, ("white"), rect, 5)

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 1280
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.chunk = Chunk((0, 0), (3, 3), 32, 2, self.rect)
        self.chunk.load()

    def run(self):
        while True:
            self.screen.fill((255, 0, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.rect.x += 1
            self.chunk.remove_chunks_behind_player(self.rect)
            
            # Lade Chunks erneut vor dem Spieler
            if not self.chunk.list:
                self.chunk.load()
                
            self.chunk.draw(self.screen, self.rect)
            pygame.draw.rect(self.screen, ("red"), self.rect)
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()