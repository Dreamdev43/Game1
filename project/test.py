import pygame
import sys

pygame.init()

# FenstergrÃ¶Ãe
width, height = 800, 600

# Farben
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Initialisierung des Fensters
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tilemap')

# TilegrÃ¶Ãe
tile_size = 50

rect = pygame.Rect(50, 650, 50, 50)
rect1 = pygame.Rect(150, 650, 50, 50)
player = pygame.Rect(350, 350, 60, 60)
world_rect = pygame.Rect(player.centerx - 100, player.centery - 50, 200, 100)

# Gitterparameter
grid_size = 20

# Chunk-Parameter
chunk_size = 4
loaded_chunks = set()

# Tilemap (Beispiel: 1 steht fÃ¼r ein rotes Tile, 0 fÃ¼r leeres Tile)
tilemap = [
    [1, 1, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 1, 1]
]

class Tilemap:
    def __init__(self, tilemap_data):
        self.tilemap_data = tilemap_data

    def draw_chunk(self, chunk_x, chunk_y):
        start_x = chunk_x * chunk_size
        start_y = chunk_y * chunk_size

        for row_index in range(start_y, min(start_y + chunk_size, len(self.tilemap_data))):
            for col_index in range(start_x, min(start_x + chunk_size, len(self.tilemap_data[row_index]))):
                tile = self.tilemap_data[row_index][col_index]
                if tile == 1:
                    pygame.draw.rect(screen, red, (col_index * tile_size, row_index * tile_size, tile_size, tile_size))

def load_chunk(chunk_x, chunk_y):
    if (chunk_x, chunk_y) not in loaded_chunks:
        tilemap_instance.draw_chunk(chunk_x, chunk_y)
        loaded_chunks.add((chunk_x, chunk_y))

# Erstelle eine Tilemap-Instanz
tilemap_instance = Tilemap(tilemap)

# Haupt-Event-Schleife
running = True
while running:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                player.x -= 1
                world_rect.x -= 1

        if event.type == pygame.MOUSEBUTTONUP:
            if rect.collidepoint(event.pos):
                player.x -= 0

    # ÃberprÃ¼fe Kollision mit Linien des Gitters
    for x in range(0, width, grid_size):
        if world_rect.colliderect(pygame.Rect(x, 0, grid_size, height)):
            print("Kollision erkannt, lade Chunks...")
            chunk_x = x // chunk_size
            for i in range(chunk_x - 1, chunk_x + 2):  # Lade benachbarte Chunks
                for j in range(-1, 2):
                    load_chunk(i, j)

    for y in range(0, height, grid_size):
        if world_rect.colliderect(pygame.Rect(0, y, width, grid_size)):
            print("Kollision erkannt, lade Chunks...")
            chunk_y = y // chunk_size
            for i in range(-1, 2):
                for j in range(chunk_y - 1, chunk_y + 2):  # Lade benachbarte Chunks
                    load_chunk(i, j)

    # Zeichnen des Gitters
    for x in range(0, width, grid_size):
        pygame.draw.line(screen, white, (x, 0), (x, height))
    for y in range(0, height, grid_size):
        pygame.draw.line(screen, white, (0, y), (width, y))

    pygame.draw.rect(screen, red, rect)
    pygame.draw.rect(screen, red, rect1)
    pygame.draw.rect(screen, red, player)
    pygame.draw.rect(screen, red, world_rect, 5)
    pygame.display.flip()

pygame.quit()
sys.exit()