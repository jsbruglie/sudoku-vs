from math import sqrt

class PlayerMove:

    def __init__ (self, x, y, answer):
        self.x = x
        self.y = y
        self.answer = answer

class Player:

    def __init__ (self, name, lives):
        self.name = name
        self.lives = lives
        self.active = True
        self.moves = []

    def addMove(self, x, y, answer):
        self.moves.append(PlayerMove(x,y,answer))

    def loseLife(self):
        self.lives -= 1
        if self.lives == 0 :
            self.active = False

    def isActive(self):
        return self.active

    def printPlayer(self):
        print('Name: ', name, ' Lives: ', lives)

class SudokuBoard(object):

    def __init__ (self, dim):
        self.board =[]
        self.dim = dim
        for i in range (0, dim):
            self.board.append([])
            for j in range (0, dim):
                self.board[-1].append(int(0))

    def isMoveValid(self, x, y, answer):
        pass

    def printBoard (self):
        print(self.board)

def main():

    players = 0
    dim = 0
    while players < 2:
        players = int(input ('How many players? '))

    while dim < 4:
        dim = int(input('What is the dimension of the side? '))

    playerList = []
    for i in range (1, players + 1):
        name = input('Player {}: What is your name? '.format(i))
        playerList.append(Player(name,2))

    b = SudokuBoard(dim)
    b.printBoard()

    while True:
        for player in playerList:
            if player.isActive:
                try:
                    x, y, answer = input('{}: What is your move? '.format(player.name))
                    player.addMove(x,y,answer)
                except ValueError :
                    print('Please input your move as follows: [x][y][number]')

if __name__ == "__main__":
    main()
