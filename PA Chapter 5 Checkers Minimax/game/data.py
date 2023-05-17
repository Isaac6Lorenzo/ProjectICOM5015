import pygame

WIDTH = 600
HEIGHT = 600
COLUMNS = 8
ROWS = 8
SIZE = WIDTH // COLUMNS

RED = pygame.Color(255, 0, 0)
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
YELLOW = pygame.Color(255, 255, 0)
TIE = pygame.Color(255,0,100)

Black_Piece = pygame.transform.scale(pygame.image.load('resources/black.png'), (SIZE, SIZE))
BlackQueen = pygame.transform.scale(pygame.image.load('resources/blackqueen.png'), (SIZE, SIZE))
White_Piece = pygame.transform.scale(pygame.image.load('resources/white.png'), (SIZE, SIZE))
WhiteQueen = pygame.transform.scale(pygame.image.load('resources/whitequeen.png'), (SIZE, SIZE))

background = pygame.transform.scale(pygame.image.load('resources/board.png'), (WIDTH, HEIGHT))