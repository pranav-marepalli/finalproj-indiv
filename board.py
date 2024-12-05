from sudoku_generator import*
from cell import*
import pygame


BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)


pygame.init()

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width=width
        self.height=height
        self.screen=screen
        self.difficulty=difficulty
        self.cells=[]


    def initialize_cells(self, board_values):
        self.cells = []
        for row in range(9):
            cell_row = []
            for col in range(9):
                value = board_values[row][col]
                cell_row.append(Cell(value, row, col, self.screen, self.width//9, self.height//9))
            self.cells.append(cell_row)
        
        for x in self.cells:
            for y in x:
                y.draw()



    def draw(self):

        for i in range(10):
            if i%3==0:
                thickness=3
            else:
                thickness=1
            pygame.draw.line(self.screen, BLACK, (0, i*self.height//9), (self.width, i*self.height//9), thickness)
            pygame.draw.line(self.screen, BLACK, (i*self.width//9, 0), (i*self.width//9, self.height), thickness)




            
                

                
