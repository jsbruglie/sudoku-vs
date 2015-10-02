import sys

from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

class SudokuUI(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="black")
        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("SudokuVS")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(
            self, width=WIDTH, height=HEIGHT,
            highlightthickness=0
        )

def main():

    root = Tk()
    root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
    app = SudokuUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
