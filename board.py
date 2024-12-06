import pygame
from sudoku_generator import *
from cell import *

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected = None
        self.og_board = generate_sudoku(difficulty)  # Initialize the original board
        self.cells = []  # This will store all Cell objects

        # Initialize the cells grid (9x9)
        for r in range(9):
            row = []
            for c in range(9):
                value = self.og_board[r][c]  # Get the value from the generated board
                row.append(Cell(value=value, row=r, col=c, screen=self.screen))
            self.cells.append(row)

    def draw(self):
        # Draw all cells
        for r in range(9):
            for c in range(9):
                self.cells[r][c].draw()

        # Draw the grid lines
        for i in range(10):
            # Set line thickness for bold lines
            if i % 3 == 0:
                width = 3
            else:
                width = 1

            # Draw horizontal lines
            pygame.draw.line(
                self.screen, 
                BLACK, 
                (0, self.height // 9 * i), 
                (self.width, self.height // 9 * i), 
                width
            )
            # Draw vertical lines
            pygame.draw.line(
                self.screen, 
                BLACK, 
                (self.width // 9 * i, 0), 
                (self.width // 9 * i, self.height), 
                width
            )

    def select(self, row, col):
        # Unselect the last selected cell if any
        if self.selected:
            self.selected.outline_col = BLACK
        # Select the new cell and highlight it
        self.selected = self.cells[row][col]
        self.selected.outline_col = RED

    def clear(self):
        # Clear the value of the currently selected cell
        if self.selected and self.og_board[self.selected.row][self.selected.col] == 0:
            self.selected.set_cell_value(0)
            self.selected.set_sketched_value(0)

    def place_number(self, value):
        # Place a number in the selected cell if it's editable
        if self.selected and self.og_board[self.selected.row][self.selected.col] == 0:
            self.selected.set_cell_value(value)
            return True
        return False

    def reset_to_original(self):
        # Reset all cells to their original values
        for r in range(9):
            for c in range(9):
                if self.og_board[r][c] == 0:
                    self.cells[r][c].set_cell_value(0)
                    self.cells[r][c].set_sketched_value(0)

    def is_full(self):
        # Check if the board is full
        for r in range(9):
            for c in range(9):
                if self.cells[r][c].value == 0:
                    return False
        return True

    def update_board(self):
        # Update the underlying board based on current cell values
        updated_board = []
        for r in range(9):
            row = []
            for c in range(9):
                row.append(self.cells[r][c].value)
            updated_board.append(row)
        self.board = updated_board

    def find_empty(self):
        # Find an empty cell and return its row and column
        for r in range(9):
            for c in range(9):
                if self.cells[r][c].value == 0:
                    return r, c
        return None

    def check_board(self):
        # Check rows
        for row in range(9):
            row_values = []
            for col in range(9):
                row_values.append(self.cells[row][col].value)
            if not self.is_unique(row_values):
                return False

        # Check columns
        for col in range(9):
            col_values = []
            for row in range(9):
                col_values.append(self.cells[row][col].value)
            if not self.is_unique(col_values):
                return False

        # Check 3x3 subgrids
        for box_row in range(3):
            for box_col in range(3):
                grid_values = []
                for row in range(box_row * 3, box_row * 3 + 3):
                    for col in range(box_col * 3, box_col * 3 + 3):
                        grid_values.append(self.cells[row][col].value)
                if not self.is_unique(grid_values):
                    return False

        return True

    def is_solved(self):
        # Check if the board is completely filled and valid
        return self.is_full() and self.check_board()

    def is_unique(self, values):
        # Helper function to check if a list of values contains unique numbers (ignoring zeros)
        nums = []
        for value in values:
            if value != 0:
                nums.append(value)
        return len(nums) == len(set(nums))
