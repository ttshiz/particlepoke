import numpy as np

class GameOfLife:
    """ a mini game of Conway's Game Life """
    def __init__(self):
        """ Initializes a game of Conway's Game of Life on a finite playing
        field, using dead edges.
        """
        self.bsize = 23
        self.rngseed = 2695
        self.rng = np.random.default_rng(self.rngseed)
        self.board = np.ones((self.bsize, self.bsize), np.int64)

    def randomize(self):
        self.board = self.rng.integers(low=0, high=2, size=(self.bsize, self.bsize))

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
        out = np.zeros((self.bsize, self.bsize), np.int8)
        for i in range(self.bsize):
            for j in range(self.bsize):
                out[i][j] = self.num_neighbors(i,j)
        print(out)
        
    def life_step(self):
        for i in range(self.bsize):
            for j in range(self.bsize):
                neighs = self.num_neighbors(i,j)
                if self.board[i][j] == 1:
                    if neighs < 2 or neighs > 3:
                        self.board[i][j] = 0
                else:
                    if neighs == 3:
                        self.board[i][j] = 1
        return