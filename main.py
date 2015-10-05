import sys
from math import sqrt
from tkinter import Tk

from gui import *

MARGIN = 20  # Pixels around the board
SIDE = 35  # Width of every board cell.
EMPTY = 0 # The numerical code for an empty square

#Input related functions - should not be in final version
def getPuzzleDimension():
    dim = 0
    while dim not in [4,9,16,25]:
        try:
            dim = int(input('What is the dimension of the side? '))
        except ValueError :
            print('Please input a valid integer!')
    return dim

def getPlayerList():
    players = 0
    while players < 2:
        try:
            players = int(input ('How many players? '))
        except ValueError :
            print('Please input a valid integer!')

    playerList = []
    for i in range (1, players + 1):
        name = input('Player {}: What is your name? '.format(i))
        playerList.append(Player(name))
    return players, playerList

class PlayerMove:

    def __init__ (self, x, y, answer):
        self.x = x
        self.y = y
        self.answer = answer

    def printMove(self):
        print('Placed {} in ({},{})'.format(self.answer, self.x, self.y))

class Player(object):

    def __init__ (self, name):
        self.name = name
        self.active = True
        self.moves = []

    def printMoves(self):
        for move in self.moves:
            move.printMove()

    def addMove(self, x, y, answer):
        self.moves.append(PlayerMove(x, y, answer))

    def lose(self):
        self.active = False
        print('Player',self.name,'lost!')

    def isActive(self):
        return self.active

    def printPlayer(self):
        print('Name: ', self.name, ' Lives: ', self.lives)
        self.printMoves()

class Game(object):

    def __init__ (self):

        dim = getPuzzleDimension()
        players, playerList = getPlayerList()

        self.players = self.active = players
        self.playerList = playerList

        self.board =[]
        self.dim = dim
        self.sqrt = int(sqrt(dim))

        for i in range (dim):
            self.board.append([])
            for j in range (dim):
                self.board[-1].append(int(EMPTY))

    def activePlayers(self):
        return self.active

    def eliminatePlayer(self, player):
        player.lose()
        self.active -= 1

    def checkCell (self, x, y, answer):
        return self.board[x][y] == answer

    def checkRow (self, x, answer):
        for i in range (self.dim):
            if self.checkCell(x,i, answer):
                return True
        return False

    def checkColumn (self, y, answer):
        for i in range (self.dim):
            if self.checkCell(i, y, answer):
                return True
        return False

    def checkSquare (self, x, y, answer):
        square_x = int(x / self.sqrt)
        square_y = int(y / self.sqrt)
        for x in range (self.sqrt):
            for y in range (self.sqrt):
                if self.checkCell(square_x * self.sqrt + x, square_y * self.sqrt + y, answer):
                    return True
        return False

    def moveIsValid(self, x, y, answer):
        if 0 <= x < self.dim and 0 <= y < self.dim and 0 < answer <= self.dim:
            print('Valid Dimensions')
            # If the cell has not been filled yet
            if self.board[x][y] == EMPTY:
                if self.checkRow(x, answer) or self.checkColumn(y, answer) or self.checkSquare(x, y, answer):
                    print('...But invalid context.')
                    return False
                return True

    def changeCell(self, x, y, answer):
        if self.moveIsValid( x, y, answer):
            self.board[x][y] = answer
            return True
        return False

    def printBoard (self):
        for row in self.board:
            print(row)

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
