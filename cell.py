import pygame
from sudoku_generator import*



BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED=(255, 0, 0)





pygame.init()
font = pygame.font.Font(None, 36)
cell_surface=pygame.display.set_mode((640,512))
class Cell:
    def __init__(self, value, row, col, screen, width, height):
        self.value=value
        self.row=row
        self.col=col
        self.sketched_value=0
        self.screen=screen
        self.cell_width=width
        self.cell_height=height
        self.selected=False
        
       


    def set_cell_value(self, value):
        self.value=value

    def set_sketched_value(self, value):
        self.sketched_value=value

    def draw(self):
        width=self.screen.get_width()
        length=self.screen.get_height()

        if self.value==0:
            return
        
        text=font.render(str(self.value), True, BLACK)
        textRect=text.get_rect()
        position=[(self.col*width//9), (self.row*length//9)]
        textRect.center=((position[0]+width//9)//2, (position[1]+length//9)//2)
        self.screen.blit(text, textRect)

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), textRect, 3)  # Red border




                
            
                
            
