import numpy as np

class GameOfLife:
    """ a mini game of Conway's Game Life """
    def __init__(self):
        """ Initializes a game of Conway's Game of Life on a finite playing
        field, using dead edges.
        """
        self.bsize = 23
        self.board = np.zeros((self.bsize, self.bsize))

    def print_board(self):
        """ Prints a representation of the board """
        print(self.board)

    def num_neighbors(self, x, y):
        """ Calculates the number of neighbors a given tile has """
        neighbors = 0
        if x == 0:
            if y == 0:
                #check only right and down
                neighbors += self.board[x+1][y]
                neighbors += self.board[x+1][y+1]
                neighbors += self.board[x][y+1]
            if y == 22: # only check left and down
                neighbors += self.board[x+1][y]
                neighbors += self.board[x+1][y-1]
                neighbors += self.board[x][y-1]
            else:
                neighbors += self.board[x-1][y-1]
                neighbors += self.board[x-1][y]
                neighbors += self.board[x-1][y+1]
                neighbors += self.board[x][y+1]
                neighbors += self.board[x][y-1]
                neighbors += self.board[x+1][y-1]
                neighbors += self.board[x+1][y]
                neighbors += self.board[x+1][y+1]
        elif x == 22: # only check up
            if y == 0:
                #check only right and down
                neighbors += self.board[x-1][y]
                neighbors += self.board[x-1][y+1]
                neighbors += self.board[x][y+1]
            if y == 22: # only check left and down
                neighbors += self.board[x-1][y]
                neighbors += self.board[x-1][y-1]
                neighbors += self.board[x][y-1]
            else:
                neighbors += self.board[x-1][y-1]
                neighbors += self.board[x-1][y]
                neighbors += self.board[x-1][y+1]
                neighbors += self.board[x][y+1]
                neighbors += self.board[x][y-1]
                neighbors += self.board[x+1][y-1]
                neighbors += self.board[x+1][y]
                neighbors += self.board[x+1][y+1]
        else:
            neighbors += self.board[x-1][y-1]
            neighbors += self.board[x-1][y]
            neighbors += self.board[x-1][y+1]
            neighbors += self.board[x][y+1]
            neighbors += self.board[x][y-1]
            neighbors += self.board[x+1][y-1]
            neighbors += self.board[x+1][y]
            neighbors += self.board[x+1][y+1]
        return neighbors

    def print_neighbors(self):
        for i in self.board:
            for j in i:
                print(self.num_neighbors(i,j))
                
    def life_step():
        return