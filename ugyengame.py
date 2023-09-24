from tkinter import *
import random

class Game(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title("Ugyen")
        self.main_grid = Frame(self, bg='Black', bd=3, width=500,height=500)
        self.main_grid.grid()
 
#crete board     
def gameboard(self):
        self.tiles = []
        for i in range(4):
            row = []
            for j in range(4):
                tile_frame = Frame(
                    self.main_grid,
                    bg='white',
                    width='50',
                    height='50'
                )
                tile_frame.grid(
                    row=i, column=j, 
                    padx=3, pady=3
                )
                tile_number = Label(
                    self.main_grid, 
                    bg='white'
                )
                tile_number.grid(row=i, column=j)
                tile_data = 
                {
                   "frame": tile_frame, 
                   "number": tile_number
                }
                row.append(tile_data)
            self.tiles.append(row)
            
#function to move left
def moveToLeft(self):
        new_board = [[0 for col in range(4)] for row in range(4)]
        for i in range(4):
            fill_position = 0
            for j in range(4):
                if self.board[i][j] != 0:
                    new_board[i][fill_position] = self.board[i][j]
                    fill_position += 1
        self.board = new_board

#merge function
def merge(self):
for i in range(4):
    for j in range(3):
        if self.board[i][j] != 0 and self.board[i][j] == self.board[i][j+1]:
            self.board[i][j] *= 2
            self.board[i][j+1] = 0
                
#function to reverse the rows of the board                 
def reverse(self):
    new_board = []
    for i in range(4):
        new_board.append([])
        for j in range(4):
            new_board[i].append(self.board[i][3-j])
    self.board = new_board

#change the values diagonally
def transpose(self):
    new_board = [[0 for col in range(4)] for row in range(4)]
    for i in range(4):
        for j in range(4):
            new_board[i][j] = self.board[j][i]
    self.board = new_board
    
#function that randomly generates row and column number for a random tile that is empty and available for inserting a value.
def pickNewValue(self):
    row = col = 0
    while self.board[row][col] != 0:
        row = random.randint(0, 3)
        col = random.randint(0, 3)

    if random.randint(1, 5) == 1:
        self.board[row][col] = 4
    else:
        self.board[row][col] = 2
