from math import sqrt

class PlayerMove:

    def __init__ (self, x, y, answer):
        self.x = x
        self.y = y
        self.answer = answer

class Player:

    def __init__ (self, name):
        self.name = name
        self.active = True
        self.moves = []

    def addMove(self, x, y, answer):
        self.moves.append(PlayerMove(x, y, answer))

    def lose(self):
        self.active = False
        print('Player',self.name,'lost')

    def isActive(self):
        return self.active

    def printPlayer(self):
        print('Name: ', self.name, ' Lives: ', self.lives)

class SudokuBoard(object):

    def __init__ (self, dim):
        self.board =[]
        self.dim = dim
        self.sqrt = int(sqrt(dim))

        for i in range (dim):
            self.board.append([])
            for j in range (dim):
                self.board[-1].append(int(0))

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
            if self.board[x][y] == 0:
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

    players = 0
    dim = 0
    while players < 2:
        players = int(input ('How many players? '))

    while dim not in [4,9,16,25]:
        dim = int(input('What is the dimension of the side? '))

    playerList = []
    for i in range (1, players + 1):
        name = input('Player {}: What is your name? '.format(i))
        playerList.append(Player(name))

    b = SudokuBoard(dim)

    # While there are active players - not working yet
    while True:
        for player in playerList:
            if player.isActive:
                b.printBoard()
                try:
                    x, y, answer = input('{}: What is your move? '.format(player.name)).split(' ')
                    if b.changeCell(int(x), int(y), int(answer)):
                        player.addMove(int(x),int(y), int(answer))
                    else:
                        player.lose()
                except ValueError :
                    print('Please input your move as follows: [x] [y] [number]')

if __name__ == "__main__":
    main()
