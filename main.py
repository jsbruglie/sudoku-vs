import pprint

class Player:

    def __init__ (self, name, lives):
        self.name = name
        self.lives = lives

    def printPlayer(self):
        print("Name: ", name, " Lives: ", lives)

class SudokuBoard(object):

    def __init__ (self, dim):
        self.board =[[]]
        self.dim = dim
        for i in range (0, dim):
            self.board[-1].append([])
            for j in range (0, dim):
                self.board[-1][-1].append(int(0))

    def printBoard (self):
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(self.board)

def main():

    players = 0
    dim = 0
    while players < 2:
        players = int(input ('How many players? '))

    while dim < 4:
        dim = int(input('What is the dimension of the side? '))

    playerList = []
    for i in range (1, players+1):
        name = input('Player {}: What is your name? '.format(i))
        playerList.append(Player(name,2))

    b = SudokuBoard(dim)
    b.printBoard()

if __name__ == "__main__":
    main()
