import pygame, time
from sudoku_generator import*
from cell import*

pygame.init()
WHITE = (255,255,255)
WIDTH = 640
HEIGHT = 512
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sudoku Game!")


def scale(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

INTRO_BKG = scale(pygame.image.load('jerry-pointing-1.jpg'),1.25)
EASY = scale(pygame.image.load('easy.png'),0.20)
MEDIUM = scale(pygame.image.load('medium.png'),0.20)
HARD = scale(pygame.image.load('hard.png'),0.20)
font = pygame.font.Font(None, 50) 
text_surface = font.render("Sudoku Game", True, WHITE)
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - 50))

def draw(win, images, text_surface, text_rect):
    for img, pos in images:
        win.blit(img, pos)
    win.blit(text_surface, text_rect)
    pygame.display.update()
images = [(INTRO_BKG, (0,0)),(EASY,(40,100)),(MEDIUM,(40,150)),(HARD,(40,200))]

FPS = 60
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(FPS)
    draw(win, images, text_surface, text_rect)
    win.blit(text_surface, text_rect)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if 41<=x<=200 and 100<=y<=135:
                generate_sudoku(9, 30)
            if 41<=x<=200 and 152<=y<=188:
                generate_sudoku(9, 40)
            if 41<=x<=200 and 200<=y<=235:
                generate_sudoku(9, 50)
    