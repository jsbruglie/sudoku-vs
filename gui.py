import sys
from math import sqrt
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

from game import *

MARGIN = 20  # Pixels around the board
SIDE = 35  # Width of every board cell.
EMPTY = 0 # The numerical code for an empty square

class SudokuUI(Frame):

    def __init__(self, parent, game):

        Frame.__init__(self, parent, background = "black")
        self.parent = parent
        self.game = game
        self.width = self.heigth = MARGIN * 2 + SIDE * game.dim
        self.initUI()

    def initUI(self):

        self.parent.title("SudokuVS")
        self.pack(fill = BOTH, expand = 1)
        self.canvas = Canvas(
            self, width = self.width, height = self.heigth,
            highlightthickness = 0
        )
        self.canvas.pack(fill = BOTH, side = TOP)
        self.drawGrid()
        self.drawNumbers()

    def drawGrid(self):
        for i in range(self.game.dim + 1):
            self.canvas.create_line(
                MARGIN + i * SIDE, MARGIN,
                MARGIN + i * SIDE, self.heigth - MARGIN,
                fill = "black" if i % self.game.sqrt == 0 else "gray"
            )

            self.canvas.create_line(
                MARGIN, MARGIN + i * SIDE,
                self.width - MARGIN, MARGIN + i * SIDE,
                fill = "black" if i % self.game.sqrt == 0 else "gray"
            )

    def drawNumbers(self):
        for row in range(self.game.dim):
            for col in range(self.game.dim):
                answer = self.game.board[row][col]
                if answer != EMPTY:
                    self.canvas.create_text(
                        MARGIN + col * SIDE + SIDE / 2,
                        MARGIN + row * SIDE + SIDE / 2,
                        text = answer, tags = "numbers",
                    )

def main():

    game = Game()

    width = height = MARGIN * 2 + SIDE * game.dim

    root = Tk()
    root.geometry("%dx%d" % (width, height))
    app = SudokuUI(root, game)

    while game.activePlayers() >= 1:
        for player in game.playerList:

            if player.isActive():
                app.drawNumbers()
                try:
                    x, y, answer = input('{}: What is your move? '.format(player.name)).split(' ')
                    if game.changeCell(int(x), int(y), int(answer)):
                        player.addMove(int(x),int(y), int(answer))
                    else:
                        game.eliminatePlayer(player)
                except ValueError :
                    print('Please input your move as follows:[x] [y] [number] (0 indexed coordinates)')

    quit()

if __name__ == "__main__":
    main()
