"""
Define Game object containing a board to insert Pieces and solve the game.
"""

from typing import List
# define type Piece that is a 2D array (list of lists of ints)
Piece = List[List[int]]

class PositionException(Exception):
    pass

class RemovalException(Exception):
    pass

class Game():
    """
    The game object holds the bord state,
    allows for insertion and removal of pieces.
    """
    def __init__(self, size: int = 7):
        self.size = size
        # initialize square board
        self.board = [[-1 for _ in range(size)] for _ in range(size)]


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
                if self.board[y+i][x+j] > 0 and piece[i][j] == 1:
                    return False

        return True

    def insert_piece(self, piece: Piece, y: int, x: int, identifier: str):
        """Inserts piece in the game board at position (y, x)

        The shape of the piece is inserted in the board by changing
        the value of the board in the shape of the piece to the identifier

        Identifiers are strings of the form: 'p0'...'p9'

        Args:
            piece (Piece): the piece to insert on the board
            y (int): the vertical position at which the piece is inserted
            x (int): the horizontal position at which the piece is inserted
        """
        for i, row in enumerate(piece):
            for j, element in enumerate(row):
                if element == 1:
                    self.board[y+i][x+j] = identifier

    def remove_piece(self, piece: Piece, y: int, x: int, identifier: str):
        """[summary]

        Args:
            piece (Piece): the piece to remove from the board
            y (int): the vertical position from which the piece is removed
            x (int): the horizontal position from which the piece is removed
        """
        for i, row in enumerate(piece):
            for j, element in enumerate(row):
                if element == 1:
                    if self.board[y+i][x+j] != identifier:
                        raise RemovalException(\
                            f'Removing inexistent piece:\n{piece}\nfrom \
                                (y, x) = ({y}, {x}) in board:\n{self.board}')
                    self.board[y+i][x+j] = 0 # reset board value to empty

    def __str__(self):
        s = ' '+'__'*self.size+'\n'
        for row in self.board:
            printed_row = '|'
            for element in row:
                printed_row += ' ' + str(element) if int(element) >= 0 else ' ' + '-'
            s += (str(printed_row) + '|\n')
        return s + ' ' + '¯¯'*self.size


if __name__ == "__main__":
    from pieces import pieces, display_piece

    # instantiate game
    g = Game()

    # display current board state
    print(g)

    # insert a piece
    piece_id = 2
    display_piece(pieces[piece_id])
    g.insert_piece(pieces[piece_id], 2, 3, f'{piece_id}')

    # display new board state
    print(g)

    # try to remove piece from wrong position, then remove at right one
    try:
        g.remove_piece(pieces[piece_id], 3, 3, f'{piece_id}')
    except RemovalException as e:
        print(f'Exception occurred: {e}')
        print(g)
        g.remove_piece(pieces[piece_id], 2, 3, f'{piece_id}')
        print(g)