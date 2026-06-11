class GameOfLife:
    """ a mini game of Conway's Game Life """
    def __init__(self):
        """ Initializes a game of Conway's Game of Life on a finite playing
        field.
        """
        self.bsize = 23
        self.board = [[None]*self.bsize]*self.bsize
        return

    def print_board(self):
        """ Prints a representation of the board """
        for i in self.board:
            print(i)
        
    def life_step():
        return