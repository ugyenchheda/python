from tkinter import *
import random

class Game(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title("Ugyen")
        self.main_grid = Frame(self, bg='Black', bd=3, width=500,height=500)
        self.main_grid.grid()
      
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
