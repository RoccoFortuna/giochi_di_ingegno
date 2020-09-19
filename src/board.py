"""
Define Game object containing a board to insert Pieces and solve the game.
"""

from typing import List

# define type Piece that is a 2D array (list of lists of ints)
Piece = List[List[int]]

class PositionException(Exception):
    pass

class Game():
    """
    The game object holds the bord state,
    allows for insertion and removal of pieces.
    """
    def __init__(self, size: int = 7):
        self.size = size
        # initialize square board
        self.board = [[0 for _ in range(size)] for _ in range(size)]


    def is_insertable(self, piece: Piece, y: int, x: int) -> bool:
        """Check whether a piece can be inserted at a position (y, x)

        Check whether the given piece fits in the board boundaries
        at position (y, x), and whether it does not overlap with
        any previously inserted piece.


        Args:
            piece (Piece): the piece to be inserted
            y (int): the vertical position at which the piece would be inserted
            x (int): the horizontal position at which the piece would be inserted

        Returns:
            bool: True if the piece can be inserted at (y, x), False otherwise.
        """

        height = len(piece)
        width = len(piece[0])

        # Check if piece fits within board boundaries
        if x + width > self.size: # check if piece exceeds width of board
            return False
        if y + height > self. size: # check if piece exceeds height of board
            return False

        # Check if piece does not overlap with other pieces
        for i, row in enumerate(piece):
            for j, element in enumerate(row):
                if self.board[y+i][x+j] > 0 and piece[y][x] == 1:
                    return False

        return True



    def __str__(self):
        s = ''
        for row in self.board:
            s += (str(row) + '\n')
        return s


if __name__ == "__main__":
    # instantiate game
    g = Game()

    # display current board state
    print(g)
