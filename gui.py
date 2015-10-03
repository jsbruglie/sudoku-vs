import sys
from math import sqrt
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

MARGIN = 20  # Pixels around the board
SIDE = 35  # Width of every board cell.

class SudokuUI(Frame):

    def __init__(self, parent, dimensions):
        Frame.__init__(self, parent, background = "black")
        self.parent = parent
        self.initUI(dimensions)

    def initUI(self, dimensions):

        self.parent.title("SudokuVS")
        self.pack(fill = BOTH, expand = 1)
        self.canvas = Canvas(
            self, width = dimensions['width'], height = dimensions['height'],
            highlightthickness = 0
        )
        self.canvas.pack(fill = BOTH, side = TOP)
        self.draw_grid(dimensions)

    def draw_grid(self, dimensions):
        for i in range(dimensions['side'] + 1):
            self.canvas.create_line(
                MARGIN + i * SIDE, MARGIN,
                MARGIN + i * SIDE, dimensions['height'] - MARGIN,
                fill="black" if i % dimensions['sqrt'] == 0 else "gray"
            )

            self.canvas.create_line(
                MARGIN, MARGIN + i * SIDE,
                dimensions['width']- MARGIN, MARGIN + i * SIDE,
                fill="black" if i % dimensions['sqrt'] == 0 else "gray"
            )

def main():

    dim = 9
    width = height = MARGIN * 2 + SIDE * dim

    dimensions = {'width': width, 'height': height, 'side': dim, 'sqrt': int(sqrt(dim))}

    root = Tk()
    root.geometry("%dx%d" % (width, height))
    app = SudokuUI(root, dimensions)
    root.mainloop()

if __name__ == '__main__':
    main()
