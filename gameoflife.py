import numpy as np

class GameOfLife:
    """ a mini game of Conway's Game Life """
    def __init__(self):
        """ Initializes a game of Conway's Game of Life on a finite playing
        field, using dead edges.
        """
        self.bsize = 23
        self.board = np.ones((self.bsize, self.bsize))

    def print_board(self):
        """ Prints a representation of the board """
        print(self.board)

    def num_neighbors(self, x, y):
        """ Calculates the number of neighbors a given tile has """
        # catch negatives if x or y are zero
        if x == 0 and y == 0:
            neighbors = np.sum(self.board[x:x+2, y:y+2]) - self.board[x][y]
        elif x == 0:
            neighbors = np.sum(self.board[x:x+2, y-1:y+2]) - self.board[x][y]
        elif y == 0:
            neighbors = np.sum(self.board[x-1:x+2, y:y+2]) - self.board[x][y]
        else:
            neighbors = np.sum(self.board[x-1:x+2, y-1:y+2]) - self.board[x][y]
        return neighbors

    def print_neighbors(self):
        for i in self.board:
            for j in i:
                print(self.num_neighbors(i,j))
                
    def life_step(self):
        return