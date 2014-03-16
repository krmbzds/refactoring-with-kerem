from Parameters import *
from Grid import *
from Robby import *
from enum import *
import Tkinter as tk
import time


class Alien:
    running = True
    grid = None
    cSize = 600.0
    cellW = cSize / 12.0
    counter = 0

    def __init__(self, grid):
        self.grid = grid
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.cSize, height=self.cSize)
        self.create_widgets()
        self.canvas.pack()
        self.root.after(0, self.animate)
        self.root.mainloop()

    def create_widgets(self):
        self.grid_indexes = []
        w = self.cellW
        for i in range(len(self.grid.matrix)):
            temp = []
            for j in range(len(self.grid.matrix[i])):
                temp.append(self.canvas.create_rectangle(j*w, i*w, (j+1)*w, (i+1)*w, fill='blue'))
            self.grid_indexes.append(temp)
        rr = self.grid.robby.get_r()
        rc = self.grid.robby.get_c()
        self.robby = self.canvas.create_oval(rc * w, rr * w, (rc + 1) * w, (rr + 1) * w, fill='red')
        self.txt_counter = self.canvas.create_text(self.cSize / 2 - 40, self.cellW / 2, fill="red")
        self.txt_action = self.canvas.create_text(self.cSize / 2 + 40, self.cellW / 2, fill="red")

    def draw_frame(self, rr, rc, action, counter):
        w = self.cellW
        for i in range(len(self.grid.matrix)):
            for j in range(len(self.grid.matrix[i])):
                color = None
                if self.grid.matrix[i][j] == OBSTACLES.WALL:
                    color = 'black'
                elif self.grid.matrix[i][j] == OBSTACLES.EMPTY:
                    color = 'white'
                elif self.grid.matrix[i][j] == OBSTACLES.CAN:
                    color = 'blue'
                self.canvas.itemconfig(self.grid_indexes[i][j], fill=color)  # change color
        self.canvas.coords(self.robby, rc * w, rr * w, (rc + 1) * w, (rr + 1) * w)
        self.canvas.itemconfig(self.txt_action, text=action)
        self.canvas.itemconfig(self.txt_counter, text=str(counter))

    def animate(self):
        if self.running:
            action = ACTIONS.reverse_mapping[self.grid.robby.get_next_action()]
            self.draw_frame(self.grid.robby.get_r(), self.grid.robby.get_c(), action, self.grid.robby.moveCount)
            self.root.after(ANIMATION_DELAY, self.animate)
            score = self.grid.robby.move()

            if self.grid.robby.moveCount > NUM_ACTIONS_PER_SESSION:
                self.quit()

    def quit(self):
        self.running = False
        self.root.quit()
